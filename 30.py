###################################################
# CONVENTIONAL WAY
###################################################
nama = 'bejo'

if nama == 'bejo' or nama == 'tejo' or nama == 'karti':
    print('Siswa teladan')
else:
    print('Siswa reguler')
###################################################
# PYTHONIC WAY
###################################################
if nama in ('bejo', 'tejo', 'karti'):
    print('Siswa teladan')
else:
    print('Siswa reguler')
