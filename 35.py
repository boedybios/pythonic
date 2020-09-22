###################################################
# CONVENTIONAL WAY
###################################################
siswa = ['karti susanti', 'tejo purnawan', 'bejo rahmadi']
print(f'siswa: {siswa}')
for i in range(len(siswa)-1):
    for j in range(i+1, len(siswa)):
        if siswa[i].split()[-1] > siswa[j].split()[-1]:
            siswa[i], siswa[j] = siswa[j], siswa[i]
print(f'terurut: {siswa}')


###################################################
# PYTHONIC WAY
###################################################
def custom_key(nama):
    return nama.split()[-1]


siswa = ['karti susanti', 'tejo purnawan', 'bejo rahmadi']
terurut = sorted(siswa, key=custom_key)
# terurut = sorted(siswa, key=lambda x: x.split()[-1])
print(f'siswa: {siswa}')
print(f'terurut: {terurut}')
