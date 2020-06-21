import pulp
import csv
import numpy as np
import matplotlib.pyplot as plt
import math

class LpProblem():
	def __init__(self, A, b):
		self.lpProb = pulp.LpProblem("LpProblem-3B", pulp.LpMinimize)
		self.A = A
		self.b = b
		self.xVariable, self.uVariable, self.vVariable = self.createVariables()

	def createVariables(self):
		objective = None
		x, u, v = [],[], []
		for i in range(60):
			uTemp = pulp.LpVariable('u'+str(i+1), lowBound=0, cat='Continuous')
			u.append(uTemp)
			objective += uTemp

		for i in range(124):
			x.append(pulp.LpVariable('x'+str(i+1), cat='Continuous'))
			vTemp = pulp.LpVariable('v'+str(i+1), lowBound=0, cat='Continuous')
			v.append(vTemp)
			objective += vTemp

		self.lpProb += objective
		return x, u, v

	def solveLP(self): # also adds constraints
		# for variable u
		for i in range(60):
			# 2 constraints for modulus
			c1,c2 = None, None
			for j in range(len(self.A[i])):
				c1 += (self.A[i][j] * self.xVariable[j])
				c2 += - (self.A[i][j] * self.xVariable[j])
			c1 += (self.A[i][j] * self.xVariable[j]) - self.b[i] - self.uVariable[i]
			c2 += - (self.A[i][j] * self.xVariable[j]) + self.b[i] - self.uVariable[i]

			self.lpProb += c1 <= 0
			self.lpProb += c2 <= 0

		#for variable v
		for i in range(124):
			# 2 constraints for modulus
			c1,c2 = None, None
			c1 += self.xVariable[i] - self.vVariable[i] <=0
			c2 += - self.xVariable[i] - self.vVariable[i] <=0
			self.lpProb += c1
			self.lpProb += c2
		# print(self.lpProb)
		self.lpProb.solve()

	def getResult(self):
		print("Objective value: ", pulp.value(self.lpProb.objective))
		for v in self.lpProb.variables():
			print(v.name, " = ", v.varValue)

	def getPlot(self):
		# histogram
		residual = np.subtract(self.b,np.dot(self.A,[pulp.value(self.xVariable[i]) for i in range(len(self.xVariable))]))
		num_bins = 10
		plt.hist(residual, num_bins, edgecolor='black')
		plt.xlabel('Residuals')
		plt.ylabel('Frequency')
		plt.title('Histogram of Residuals. Bins - ' + str(num_bins))
		plt.show()

		# comparison
		fig, ax = plt.subplots()
		months = [i for i in range(1,61)]
		bHat = np.dot(self.A,np.array([pulp.value(self.xVariable[i]) for i in range(len(self.xVariable))]))
		l1 = ax.plot(months, self.b, label='Original rate')
		l1 = ax.plot(months, bHat, label='Predicted rate')
		ax.set(xlabel="Months t", ylabel="Conversion Rate", title="Original v/s Predicted")
		plt.legend(loc='best')
		plt.show()

# reading the conversion rates and computing b - 60 X 1
with open('euro-usd-data.csv', newline='') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	next(reader, None)
	bTemp = []
	for row in reader:
		bTemp.append(float(row[2]))

b = np.array(bTemp)

# computing A - 60 X 124
A = []
for t in range (1,61):
	ATempRow = [1, t, t**2, t**3]
	for j in range (1,61):
		ATempRow.append(math.cos((2*(math.pi)*t)/j))
	for j in range (1,61):
		ATempRow.append(math.sin((2*(math.pi)*t)/j))
	A.append(ATempRow)

problem = LpProblem(A,b)
problem.solveLP()
problem.getResult()
problem.getPlot()