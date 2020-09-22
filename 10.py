###################################################
# CONVENTIONAL WAY
###################################################
listku = []
for i in range(50):
    listku.append(i+1)
print(f'listku={listku}')

###################################################
# PYTHONIC WAY
###################################################
listku = [i+1 for i in range(50)]
print(f'listku={listku}')
