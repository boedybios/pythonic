listku = [30, 20, 60, 40, 20, 10, 30, 20]
hitung = 20
jumlah = 0
###################################################
# CONVENTIONAL WAY
###################################################
for item in listku:
    if item == hitung:
        jumlah += 1
print(f'Ditemukan {hitung} sejumlah {jumlah} buah dalam {listku}')
###################################################
# PYTHONIC WAY
###################################################
jumlah = listku.count(20)
print(f'Ditemukan {hitung} sejumlah {jumlah} buah dalam {listku}')
