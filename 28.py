###################################################
# CONVENTIONAL WAY
###################################################
nama = 'bejo'
usia = 25
print('nama saya ' + nama + ' usia saya ' + str(usia) + ' tahun ')
print('nama saya %s usia saya %d tahun' % (nama, usia))
###################################################
# PYTHONIC WAY
###################################################
print('nama saya {} usia saya {} tahun'.format(nama, usia))
print('nama saya {1} usia saya {0} tahun'.format(usia, nama))
siswa = {
    'nim': '001',
    'nama': 'bejo',
    'usia': 25,
    'ipk': 3.75
}
print('nama:{nama} usia:{usia}'.format(**siswa))
print(f'nama:{nama} usia:{usia}')
