import numpy as np

class LPSolver:
	def __init__(self, A, b, C, basicIndices, nonbasicIndices):
		self.A = A
		self.b = b
		self.C = C
		self.basicIndices = basicIndices
		self.nonbasicIndices = nonbasicIndices
		self.A_b = self.getColumns(A,basicIndices)
		self.A_n = self.getColumns(A,nonbasicIndices)
		self.C_b = self.getColumns(C,basicIndices)
		self.C_n = self.getColumns(C,nonbasicIndices)
		self.b_hat = self.compute_b_hat()
		self.objective = self.computeObjective()
		self.objectiveRow = self.computeObjectiveRow()
		self.indexOfEnteringVariable = self.getIndexOfEnteringVariable()
		self.enteringVariableColumn = self.computeEnteringVariableColumn()
		self.allColumns = self.computeAllColumns()
		self.indexOfLeavingVariable = self.getIndexOfLeavingVariable()

	# Takes in a list of indices
	def getColumns(self, matrix, indices):
		return matrix[np.ix_([i for i in range(0,len(matrix))], indices)]

	def compute_b_hat(self):
		return np.linalg.solve(self.A_b, self.b)

	def computeObjective(self):
		return self.C_b * self.b_hat

	def computeObjectiveRow(self):
		y = np.linalg.solve(np.transpose(self.A_b), np.transpose(self.C_b))
		return self.C_n - (np.transpose(y) * self.A_n)

	def getResult(self):
		print("B column for dictionary ", self.b_hat.shape)
		print(self.b_hat)
		print("Objective value for dictionary ", self.objective)
		print("Objective row for dictionary ", self.objectiveRow.shape)
		print(self.objectiveRow)
		print("Index of entering variable in original dictionary - ", self.indexOfEnteringVariable)
		print("Entering Variable Column for dictionary ", self.enteringVariableColumn.shape)
		print(self.enteringVariableColumn)
		print("All Columns for the dictionary ", self.allColumns.shape)
		print(self.allColumns)
		print("Index of leaving variable in original dictionary - ", self.indexOfLeavingVariable)
		return (self.b_hat, self.objective, self.objectiveRow, self.indexOfEnteringVariable, self.enteringVariableColumn, self.indexOfLeavingVariable)

	def getIndexOfEnteringVariable(self):
		L = self.objectiveRow[0].tolist()[0]
		index = L.index(max(L))
		return self.nonbasicIndices[index]

	def computeEnteringVariableColumn(self):
		return np.linalg.solve(-self.A_b, self.A[:,self.indexOfEnteringVariable])

	def computeAllColumns(self):
		return np.linalg.solve(-self.A_b, self.A_n)

	def getIndexOfLeavingVariable(self):
		L = []
		for i in range(len(self.enteringVariableColumn)):
			if(self.enteringVariableColumn[i] < 0):
				L.append(self.b_hat[i]/-self.enteringVariableColumn[i])
			else:
				L.append(float('inf'))
		index = L.index(min(L))
		print(index)
		return self.basicIndices[index]



A = np.matrix([
	[1, -1, 0, 0, 0, -1, 1, 0, 0, 0, 0, 0],
	[1, 0, 0, -1, -1, 0, 0, 1, 0, 0, 0, 0],
	[0, 0, -1, 0, 0, -1, 0, 0, 1, 0, 0, 0],
	[0, -1, -1, 1, 0, 1, 0, 0, 0, 1, 0, 0],
	[1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0],
	[-1, 0, 0, -1, 1, -1, 0, 0, 0, 0, 0, 1],
	])
b = np.matrix([[3], [-1], [-2], [4], [6], [-2]])
C = np.matrix([-2, -3, -1, -1, 0, 1, 0, 0, 0, 0, 0, 0])

# x1 = 0, x2 = 1, x3 = 2, x4 = 3, x5 = 4, x6 = 5, 
# w1 = 6, w2 = 7, w3 = 8, w4 = 9, w5 = 10, w6 = 11 

print("Problem 4.A.1") #x1,x2,x3,w1,w2,w3
lp  = LPSolver(A, b, C, [0,1,2,6,7,8], [3,4,5,9,10,11])
lp.getResult()

print("Problem 4.A.2") #x1,x2,x5,w3,w5,w6
lp  = LPSolver(A, b, C, [0,1,4,8,10,11], [2,3,5,6,7,9])
lp.getResult()


print("Problem 4.A.3") #x1,x2,x6,w4,w5,w6
lp  = LPSolver(A, b, C, [0,1,5,9,10,11], [2,3,4,6,7,8])
lp.getResult()


print("Problem 4.B") #x3, x4, x5, w1, w2, w6}
lp  = LPSolver(A, b, C, [2,3,4,6,7,11], [0,1,5,8,9,10])
lp.getResult()


print("Problem 4.C") #x_5,x_6,w_1,w_3,w_5,w_6
lp  = LPSolver(A, b, C, [4,5,6,8,10,11], [0,1,2,3,7,9])
lp.getResult()

