###################################################
# CONVENTIONAL WAY
###################################################
data1 = {'nim': '001', 'nama': 'bejo'}
data2 = {'ipk': 3.25, 'semester': 4}
siswa = {}
for kunci in data1:
    siswa[kunci] = data1[kunci]
for kunci in data2:
    siswa[kunci] = data2[kunci]
print(f'siswa: {siswa}')
###################################################
# PYTHONIC WAY
###################################################
data3 = {'kota': 'Palembang', 'hobi': 'membaca'}
siswa = {**data1, **data2}
print(f'siswa: {siswa}')
