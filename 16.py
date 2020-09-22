###################################################
# CONVENTIONAL WAY
###################################################
listku = ['belajar', 'python', 'dasar']
kalimat = ''
for kata in listku:
    kalimat += kata + ' '
print(f'listku: {listku}')
print(f'kalimat: {kalimat}')
###################################################
# PYTHONIC WAY
###################################################
listku = ['belajar', 'python', 'dasar']
kalimat = ' '.join(listku)
print(f'listku: {listku}')
print(f'kalimat: {kalimat}')
