import pulp
my_lp_problem = pulp.LpProblem("P2", pulp.LpMaximize)

x1 = pulp.LpVariable('x1', lowBound=-2, upBound = 2, cat='Continuous')
x2 = pulp.LpVariable('x2', lowBound=-1, upBound = 1, cat='Continuous')
x3 = pulp.LpVariable('x3', lowBound=0, upBound = 1, cat='Continuous')
x4 = pulp.LpVariable('x4', lowBound=-1, upBound = 1, cat='Continuous')

# Objective function
my_lp_problem += 2 * x1 + 3 * x3 + 1 * x4, "Z"

# Constraints
my_lp_problem += 1 * x1 - 1 * x2 + 1 * x4 <= 1
my_lp_problem += 2 * x2 - 1 * x4 <= 2
my_lp_problem += 1 * x1 - 1 * x3 - 2 * x4 <= -1
my_lp_problem += -1 * x1 + 1 * x4 <= 1

print(my_lp_problem)

my_lp_problem.solve()
print("Solution - ", pulp.LpStatus[my_lp_problem.status])


for variable in my_lp_problem.variables():
    print("{} = {}".format(variable.name, variable.varValue))

print("Objective value: ", pulp.value(my_lp_problem.objective))

print("------------------ Branching on variable x4 ----------------")

print("------------------ Branching on variable x4: Case 1 ----------------")
my_lp_problem = pulp.LpProblem("P2", pulp.LpMaximize)

x1 = pulp.LpVariable('x1', lowBound=-2, upBound = 2, cat='Continuous')
x2 = pulp.LpVariable('x2', lowBound=-1, upBound = 1, cat='Continuous')
x3 = pulp.LpVariable('x3', lowBound=0, upBound = 1, cat='Continuous')
x4 = pulp.LpVariable('x4', lowBound=-1, upBound = 1, cat='Continuous')

# Objective function
my_lp_problem += 2 * x1 + 3 * x3 + 1 * x4, "Z"

# Constraints
my_lp_problem += 1 * x1 - 1 * x2 + 1 * x4 <= 1
my_lp_problem += 2 * x2 - 1 * x4 <= 2
my_lp_problem += 1 * x1 - 1 * x3 - 2 * x4 <= -1
my_lp_problem += -1 * x1 + 1 * x4 <= 1

# New Constraint
my_lp_problem += 1 * x4 <= 0

print(my_lp_problem)

my_lp_problem.solve()
print("Solution - ", pulp.LpStatus[my_lp_problem.status])


for variable in my_lp_problem.variables():
    print("{} = {}".format(variable.name, variable.varValue))

print("Objective value: ", pulp.value(my_lp_problem.objective))


print("------------------ Branching on variable x4: Case 2 ----------------")
my_lp_problem = pulp.LpProblem("P2", pulp.LpMaximize)

x1 = pulp.LpVariable('x1', lowBound=-2, upBound = 2, cat='Continuous')
x2 = pulp.LpVariable('x2', lowBound=-1, upBound = 1, cat='Continuous')
x3 = pulp.LpVariable('x3', lowBound=0, upBound = 1, cat='Continuous')
x4 = pulp.LpVariable('x4', lowBound=-1, upBound = 1, cat='Continuous')

# Objective function
my_lp_problem += 2 * x1 + 3 * x3 + 1 * x4, "Z"

# Constraints
my_lp_problem += 1 * x1 - 1 * x2 + 1 * x4 <= 1
my_lp_problem += 2 * x2 - 1 * x4 <= 2
my_lp_problem += 1 * x1 - 1 * x3 - 2 * x4 <= -1
my_lp_problem += -1 * x1 + 1 * x4 <= 1

# New Constraint
my_lp_problem += 1 * x4 >= 1

print(my_lp_problem)

my_lp_problem.solve()
print("Solution - ", pulp.LpStatus[my_lp_problem.status])


for variable in my_lp_problem.variables():
    print("{} = {}".format(variable.name, variable.varValue))

print("Objective value: ", pulp.value(my_lp_problem.objective))


# # Direct ILP
# my_lp_problem = pulp.LpProblem("P2", pulp.LpMaximize)

# x1 = pulp.LpVariable('x1', lowBound=-2, upBound = 2, cat='Integer')
# x2 = pulp.LpVariable('x2', lowBound=-1, upBound = 1, cat='Integer')
# x3 = pulp.LpVariable('x3', lowBound=0, upBound = 1, cat='Integer')
# x4 = pulp.LpVariable('x4', lowBound=-1, upBound = 1, cat='Integer')

# # Objective function
# my_lp_problem += 2 * x1 + 3 * x3 + 1 * x4, "Z"

# # Constraints
# my_lp_problem += 1 * x1 - 1 * x2 + 1 * x4 <= 1
# my_lp_problem += 2 * x2 - 1 * x4 <= 2
# my_lp_problem += 1 * x1 - 1 * x3 - 2 * x4 <= -1
# my_lp_problem += -1 * x1 + 1 * x4 <= 1

# print(my_lp_problem)

# my_lp_problem.solve()
# print("Solution - ", pulp.LpStatus[my_lp_problem.status])


# for variable in my_lp_problem.variables():
#     print("{} = {}".format(variable.name, variable.varValue))

# print("Objective value: ", pulp.value(my_lp_problem.objective))