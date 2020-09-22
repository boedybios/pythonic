def tambah(a, b):
    return a + b


def kali(a, b):
    return a * b


x, y = 10, 20
kondisi = True
###################################################
# CONVENTIONAL WAY
###################################################
if kondisi:
    hasil = tambah(x, y)
else:
    hasil = kali(x, y)
print(f'hasil: {hasil}')
###################################################
# PYTHONIC WAY
###################################################
hasil = (tambah if kondisi else kali)(x, y)
print(f'hasil: {hasil}')
