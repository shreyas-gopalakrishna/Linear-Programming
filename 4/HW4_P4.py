import pulp
my_lp_problem = pulp.LpProblem("P4", pulp.LpMinimize)

n = 10
k = 4

objective = []
x = []

A = [[1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
	 [0, 1, 0, 0, 0, 0, 1, 1, 0, 0],
	 [1, 0, 0, 0, 0, 0, 0, 1, 1, 0],
	 [1, 0, 1, 0, 1, 1, 0, 0, 0, 0]
	]

# Objective function and Variables
for i in range(0, n):
	variable = pulp.LpVariable('x'+str(i+1), cat='Binary')
	x.append(variable)
	objective += (i+1)*variable

my_lp_problem += objective

# Constraints
for i in range(k):
	temp = None
	for j in range(n):
		temp += A[i][j] * x[j]
	my_lp_problem += temp >= 1

print(my_lp_problem)

my_lp_problem.solve()
print("Solution - ", pulp.LpStatus[my_lp_problem.status])


for variable in my_lp_problem.variables():
    print("{} = {}".format(variable.name, variable.varValue))

print("Objective value: ", pulp.value(my_lp_problem.objective))