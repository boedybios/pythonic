def lipat_ganda(x):
    return x*2


###################################################
# CONVENTIONAL WAY
###################################################
listku = [10, 20, 30]
listmu = []
for item in listku:
    listmu.append(lipat_ganda(item))

print(f'listku={listku}')
print(f'listmu={listmu}')

###################################################
# PYTHONIC WAY
###################################################
listku = [10, 20, 30]
listmu = list(map(lipat_ganda, listku))
print(f'listku={listku}')
print(f'listmu={listmu}')
