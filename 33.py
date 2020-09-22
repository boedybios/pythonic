###################################################
# CONVENTIONAL WAY
###################################################
string_input = 'kota cirebon'
translasi = {
    'a': '4',
    'i': '1',
    'e': '3',
    'o': '0'
}
string_output = ''
for x in string_input:
    val = translasi.get(x)
    string_output += val if val else x
print(f'hasil konversi: {string_output}')
###################################################
# PYTHONIC WAY
###################################################
sumber = 'aieostb'
tujuan = '4130578'
tabel_translasi = str.maketrans(sumber, tujuan)
string_input = 'bos bajaj'
string_output = string_input.translate(tabel_translasi)
print(f'hasil konversi: {string_output}')
