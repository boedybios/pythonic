###################################################
# CONVENTIONAL WAY
###################################################
nim = ['001', '002', '003']
nama = ['bejo', 'ani', 'tejo']
for i in range(len(nim)):
    print(f'nim:{nim[i]} -- nama:{nama[i]}')
###################################################
# PYTHONIC WAY
###################################################
nim = ['001', '002', '003']
nama = ['bejo', 'ani', 'tejo']
for x, y in zip(nim, nama):
    print(f'nim:{x} -- nama:{y}')
