###################################################
# CONVENTIONAL WAY
###################################################
nim = ['001', '002', '003']
nama = ['bejo', 'karti', 'tejo']
for i in range(len(nim)):
    print(f'nim:{nim[i]} -- nama:{nama[i]}')
###################################################
# PYTHONIC WAY
###################################################
nim = ['001', '002', '003']
nama = ['bejo', 'karti', 'tejo']
for i, x in enumerate(nim):
    print(f'nim:{x} -- nama:{nama[i]}')
