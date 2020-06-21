# Source - http://benalexkeen.com/linear-programming-with-python-and-pulp-part-2/
import pulp
my_lp_problem = pulp.LpProblem("P3", pulp.LpMaximize)

x1 = pulp.LpVariable('x1', lowBound=0, cat='Continuous')
x2 = pulp.LpVariable('x2', lowBound=0, cat='Continuous')
x3 = pulp.LpVariable('x3', lowBound=0, cat='Continuous')
x4 = pulp.LpVariable('x4', lowBound=0, cat='Continuous')
x5 = pulp.LpVariable('x5', lowBound=0, cat='Continuous')
x6 = pulp.LpVariable('x6', lowBound=0, cat='Continuous')
x7 = pulp.LpVariable('x7', lowBound=0, cat='Continuous')
x8 = pulp.LpVariable('x8', lowBound=0, cat='Continuous')
x9 = pulp.LpVariable('x9', lowBound=0, cat='Continuous')
x10 = pulp.LpVariable('x10', lowBound=0, cat='Continuous')
x11 = pulp.LpVariable('x11', lowBound=0, cat='Continuous')
x12 = pulp.LpVariable('x12', lowBound=0, cat='Continuous')
x13 = pulp.LpVariable('x13', lowBound=0, cat='Continuous')
x14 = pulp.LpVariable('x14', lowBound=0, cat='Continuous')
x15 = pulp.LpVariable('x15', lowBound=0, cat='Continuous')

# Objective function
my_lp_problem += 1.451 * x1 + 2.683 * x2 + 5.898 * x3 + 2.102 * x4 + 5.709 * x5 + 4.519 * x6 + 7.176 * x7 + 6.075 * x8 + 5.718 * x9 + 7.442 * x10 + 1.234 * x11 + 4.680 * x12 + 7.229 * x13 + 9.589 * x14 + 6.497 * x15, "Z"

# Constraints
my_lp_problem += 2.563 * x1 + 4.307 * x2 + 6.422 * x3 + 3.488 * x4 + 6.581 * x5 + 8.993 * x6 + 11.481 * x7 + 11.730 * x8 + 9.270 * x9 + 10.160 * x10 + 1.961 * x11 + 9.300 * x12 + 11.672 * x13 + 10.877 * x14 + 12.137 * x15 <= 10000
my_lp_problem += 2.563 * x1 + 4.307 * x2 + 6.422 * x3 + 3.488 * x4 + 6.581 * x5 + 8.993 * x6 + 11.481 * x7 + 11.730 * x8 + 9.270 * x9 + 10.160 * x10 + 1.961 * x11 + 9.300 * x12 + 11.672 * x13 + 10.877 * x14 + 12.137 * x15 >= 0

# Risk
my_lp_problem += 2.563 * x1 + 3.488 * x4 + 10.160 * x10 + 11.672 * x13 <= 3500
my_lp_problem += 2.563 * x1 + 3.488 * x4 + 10.160 * x10 + 11.672 * x13 >= 1500
my_lp_problem += 4.307 * x2 + 6.581 * x5 + 11.730 * x8 + 9.270 * x9 + 10.877 * x14 <= 6500
my_lp_problem += 4.307 * x2 + 6.581 * x5 + 11.730 * x8 + 9.270 * x9 + 10.877 * x14 >= 4500
my_lp_problem += 6.422 * x3 + 7.176 * x7 + 1.961 * x11 + 12.137 * x15 <= 3000
my_lp_problem += 6.422 * x3 + 7.176 * x7 + 1.961 * x11 + 12.137 * x15 >= 1000
my_lp_problem += 8.993 * x6 + 9.300 * x12 <= 2500
my_lp_problem += 8.993 * x6 + 9.300 * x12 >= 500

# Market
my_lp_problem += 2.563 * x1 + 11.730 * x8 + 1.961 * x11 <= 3000
my_lp_problem += 2.563 * x1 + 11.730 * x8 + 1.961 * x11 >= 0
my_lp_problem += 4.307 * x2 + 6.422 * x3 + 6.581 * x5 + 8.993 * x6 + 11.481 * x7 + 12.137 * x15 <= 4000
my_lp_problem += 4.307 * x2 + 6.422 * x3 + 6.581 * x5 + 8.993 * x6 + 11.481 * x7 + 12.137 * x15 >= 0
my_lp_problem += 3.488 * x4 + 9.270 * x9 + 11.672 * x13 <= 5000
my_lp_problem += 3.488 * x4 + 9.270 * x9 + 11.672 * x13 >= 0
my_lp_problem += 10.160 * x10 + 9.300 * x12 + 10.877 * x14 <= 7000
my_lp_problem += 10.160 * x10 + 9.300 * x12 + 10.877 * x14 >= 0

# eco-friendly
my_lp_problem += 2.563 * x1 + 4.307 * x2 + 6.422 * x3 + 8.993 * x6 + 11.481 * x7 + 11.730 * x8 + 9.270 * x9 + 10.160 * x10 + 1.961 * x11 + 11.672 * x13 <= 10000
my_lp_problem += 2.563 * x1 + 4.307 * x2 + 6.422 * x3 + 8.993 * x6 + 11.481 * x7 + 11.730 * x8 + 9.270 * x9 + 10.160 * x10 + 1.961 * x11 + 11.672 * x13 >= 2000

print(my_lp_problem)

my_lp_problem.solve()
print("Solution - ", pulp.LpStatus[my_lp_problem.status])


for variable in my_lp_problem.variables():
    print("{} = {}".format(variable.name, variable.varValue))

print("Profit: ", pulp.value(my_lp_problem.objective))

