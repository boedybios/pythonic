###################################################
# CONVENTIONAL WAY
###################################################
a = 10
b = 20
print('sebelum pertukaran')
print(f'a={a} dan b={b}')
c = a
a = b
b = c
print('setelah pertukaran')
print(f'a={a} dan b={b}')
###################################################
# PYTHONIC WAY
###################################################
x = 10
y = 20
print('sebelum pertukaran')
print(f'x={x} dan y={y}')
x, y = y, x
print('setelah pertukaran')
print(f'x={x} dan y={y}')
