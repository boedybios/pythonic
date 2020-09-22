###################################################
# CONVENTIONAL WAY
###################################################
listku = [10, 20, 30, 40, 50]
dicari = 30
keetemu = False
for x in listku:
    if x == dicari:
        ketemu = True
        break
if ketemu:
    print('ditemukan')
else:
    print('tidak ditemukan')
###################################################
# PYTHONIC WAY
###################################################
if dicari in listku:
    print('ditemukan')
else:
    print('tidak ditemukan')
