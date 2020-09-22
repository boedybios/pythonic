###################################################
# CONVENTIONAL WAY
###################################################
listmu = [30, 60, 10, 55]
listku = []
for nilai in listmu:
    if nilai > 50:
        listku.append(nilai)
print(f'listku={listku}')

###################################################
# PYTHONIC WAY
###################################################
listmu = [30, 60, 10, 55]
listku = [nilai for nilai in listmu if nilai > 50]
# listku = [nilai if nilai > 50 else 'wee' for nilai in listmu]
print(f'listku={listku}')
