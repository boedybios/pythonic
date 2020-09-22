###################################################
# CONVENTIONAL WAY
###################################################


def salam1(nama, pesan):
    print(f'Hai {nama}! {pesan}')


salam1('Karti', 'Selamat Pagi')
salam1('Tejo', 'Apa kabar?')
salam1('Bejo', '')
###################################################
# PYTHONIC WAY
###################################################


def salam2(nama, pesan=''):
    print(f'Hai {nama}! {pesan}')


salam2('Karti', 'Selamat Pagi')
salam2('Tejo', 'Apa kabar?')
salam2('Bejo')
