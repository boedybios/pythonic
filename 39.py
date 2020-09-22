x = '   Bahasa pemrograman python: guido van rossum '
print(f'x: {x}')
###################################################
# CONVENTIONAL WAY
###################################################
y = x.strip()
print(f'y: {y}')
y = y.upper()
print(f'y: {y}')
y = y.replace(':', ';')
print(f'y: {y}')
###################################################
# PYTHONIC WAY
###################################################
z = x.strip().upper().replace(':', ';')
print(f'z: {z}')
