###################################################
# CONVENTIONAL WAY
###################################################
listmu = [10, 20, 30, 40, 50, 60]
listku = []
for i in range(len(listmu)):
    reverse_i = len(listmu) - 1 - i
    listku.append(listmu[reverse_i])
print(f'listmu={listmu}')
print(f'listku={listku}')

###################################################
# PYTHONIC WAY
###################################################
listmu = [10, 20, 30, 40, 50, 60]
listku = listmu[::-1]
print(f'listmu={listmu}')
print(f'listku={listku}')

kata = 'BELAJAR'
print(kata[::-1])
