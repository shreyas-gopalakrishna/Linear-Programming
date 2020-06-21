import pulp
import csv
import numpy as np
import matplotlib.pyplot as plt

# reading the conversion rates and computing b - 60 X 1
with open('euro-usd-data.csv', newline='') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	next(reader, None)
	bTemp = []
	for row in reader:
		bTemp.append(float(row[2]))

b = np.array(bTemp)

# computing A - 60 X 124
ATemp = []
for t in range (1,61):
	ATempRow = []
	ATempRow.append(1)
	ATempRow.append(t)
	ATempRow.append(t**2)
	ATempRow.append(t**3)
	for j in range (1,61):
		ATempRow.append(np.cos((2*(np.pi)*t)/j))
	for j in range (1,61):
		ATempRow.append(np.sin((2*(np.pi)*t)/j))
	ATemp.append(ATempRow)
A = np.array(ATemp)

# histogram
output, residual, rank, singular = np.linalg.lstsq(A, b, rcond=None)

# Printing output
print("Output:")
for i in range(0,4):
	print("c"+str(i), output[i])

for i in range(4,64):
	print("a"+str(i-3), output[i])

for i in range(64,124):
	print("b"+str(i-63), output[i])

residual = np.subtract(b,np.dot(A,np.array(output)))

print("Residuals:")
for i in range(0,len(residual)):
	print("residual_"+str(i), residual[i])

num_bins = 10
plt.hist(residual, num_bins, edgecolor='black')
plt.xlabel('Residuals')
plt.ylabel('Frequency')
plt.title('Histogram of Residuals. Bins - ' + str(num_bins))
plt.show()

# comparison
fig, ax = plt.subplots()
months = [i for i in range(1,61)]
bHat = np.dot(A,np.array(output))
l1 = ax.plot(months, b, label='Original rate')
l1 = ax.plot(months, bHat, label='Predicted rate')
ax.set(xlabel="Months t", ylabel="Conversion Rate", title="Original v/s Predicted")
plt.legend(loc='best')
plt.show()