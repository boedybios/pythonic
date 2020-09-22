def cetak_nama(f_name, l_name):
    print(f'{f_name} {l_name}')


###################################################
# POSITITIONAL ARGUMENT
###################################################
cetak_nama('Karti', 'Susanti')
cetak_nama('Susanti', 'Karti')
###################################################
# KEYWORD ARGUMENT
###################################################
cetak_nama(f_name='Karti', l_name='Susanti')
cetak_nama(l_name='Susanti', f_name='Karti')
