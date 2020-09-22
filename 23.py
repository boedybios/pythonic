###################################################
# CONVENTIONAL WAY
###################################################
def fungsiku():
    nim = '007'
    nama = 'asep'
    ipk = 1.25
    siswa = (nim, nama, ipk)
    return siswa


hasil = fungsiku()
print(f'hasil1: {hasil[0]}')
print(f'hasil2: {hasil[1]}')
print(f'hasil2: {hasil[2]}')
###################################################
# PYTHONIC WAY
###################################################
def fungsimu():
    nim = '007'
    nama = 'asep'
    ipk = 1.25
    return nim, nama, ipk


a, b, c = fungsimu()
print(f'hasil1: {a}')
print(f'hasil2: {b}')
print(f'hasil2: {c}')
