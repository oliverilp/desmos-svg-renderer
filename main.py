data = """
M4.24076 15.6508
C4.60018 16.0701 5.23148 16.1187 5.65081 15.7593
L12 10.3171
L18.3492 15.7593
C18.7686 16.1187 19.3999 16.0701 19.7593 15.6508
C20.1187 15.2315 20.0701 14.6002 19.6508 14.2407
L12.6508 8.24074
C12.2763 7.91975 11.7237 7.91975 11.3492 8.24074
L4.34923 14.2407
C3.9299 14.6002 3.88134 15.2315 4.24076 15.6508
Z"""

print()
data_list = data.split('\n')

m = None
x_list = []
y_list = []

i = 0
for row in data_list:
  if len(row) == 0:
    continue

  args = list(map(float, row[1:].split()))

  if row.startswith('M'):
    m = args
    continue
  if row.startswith('C'):
    print()
    print(args)
    command_x = f"C_{{x{i}}}=\\left(1-\\frac{{[1...N]}}{{N}}\\right)^{{3}}\\cdot{m[0]}+\\left(1-\\frac{{[1...N]}}{{N}}\\right)^{{2}}\\cdot3\\frac{{[1...N]}}{{N}}\\cdot{args[0]}+\\left(1-\\frac{{[1...N]}}{{N}}\\right)\\cdot3\\left(\\frac{{[1...N]}}{{N}}\\right)^{{2}}\\cdot {args[2]}+\\left(\\frac{{[1...N]}}{{N}}\\right)^{{3}}{args[4]}"
    x_list.append(command_x)
    command_y = f"C_{{y{i}}}=\\left(1-\\frac{{[1...N]}}{{N}}\\right)^{{3}}\\cdot{m[1]}+\\left(1-\\frac{{[1...N]}}{{N}}\\right)^{{2}}\\cdot3\\frac{{[1...N]}}{{N}}\\cdot{args[1]}+\\left(1-\\frac{{[1...N]}}{{N}}\\right)\\cdot3\\left(\\frac{{[1...N]}}{{N}}\\right)^{{2}}\\cdot {args[3]}+\\left(\\frac{{[1...N]}}{{N}}\\right)^{{3}}{args[5]}"
    x_list.append(command_y)

  print(f'{ {i} } {row}')
  i += 1

print(m)

with open('data.txt', 'w') as file:
  file.write('\n\n'.join(x_list))

# PYTHON

# x_list = # [
#  [1, 2, 4...],
#  [1, 2, 4...],
#  [123],
#  [1, 2, 4...],
# ]

# y_list = # [
#  [1, 2, 4...],
#  [1, 2, 4...],
#  [123],
#  [1, 2, 4...],
# ]

# DESMOS

# N = 50

# Cx1 = [(1 - t) ...]
# Cy1 = [(1 - t) ...]
# Lx1 = [123]
# Ly1 = [123]

# Px1 = join(X1, X2, ...)
# Py1 = join(Y1, Y2, ...)
# polygon(Px1, Py1)
