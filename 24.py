###################################################
# CONVENTIONAL WAY
###################################################
nim = ['001', '002', '003']
nama = ['bejo', 'karti', 'tejo']
ipk = [3.25, 2.33, 1.88]
siswa = []
for i in range(len(nim)):
    siswa.append((nim[i], nama[i], ipk[i]))
print(f'siswa: {siswa}')
###################################################
# PYTHONIC WAY
###################################################
nim = ['001', '002', '003']
nama = ['bejo', 'karti', 'tejo']
ipk = [3.25, 2.33, 1.88]
siswa = list(zip(nim, nama, ipk))
print(f'siswa: {siswa}')
