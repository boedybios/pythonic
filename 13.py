###################################################
# CONVENTIONAL WAY
###################################################
listmu = [10, 20, 30, 40, 50, 60]
listku = []
for i in range(2, 5):
    listku.append(listmu[i])
print(f'listku={listku}')

###################################################
# PYTHONIC WAY
###################################################
listmu = [10, 20, 30, 40, 50, 60]
listku = listmu[2:5]
print(f'listku={listku}')

listku = listmu[4:]
print(f'listku={listku}')

listku = listmu[:3]
print(f'listku={listku}')

kata = 'PEMBELAJARAN'
print(kata[3:10])
