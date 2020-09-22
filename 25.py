###################################################
# CONVENTIONAL WAY
###################################################
siswa = [('001', 'bejo', 3.25),
         ('002', 'karti', 2.33),
         ('003', 'tejo', 1.88)]
nim = []
nama = []
ipk = []
for data in siswa:
    nim.append(data[0])
    nama.append(data[1])
    ipk.append(data[2])
print(f'nim: {nim}')
print(f'nama: {nama}')
print(f'ipk: {ipk}')
###################################################
# PYTHONIC WAY
###################################################
siswa = [('001', 'bejo', 3.25),
         ('002', 'karti', 2.33),
         ('003', 'tejo', 1.88)]
nim, nama, ipk = zip(*siswa)
print(f'nim: {nim}')
print(f'nama: {nama}')
print(f'ipk: {ipk}')
