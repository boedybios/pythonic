def jumlahkan(p_satu, p_dua):
    return p_satu + p_dua


listku = [10, 20]
dictku = {'p_satu': 100, 'p_dua': 200}
###################################################
# CONVENTIONAL WAY
###################################################
hasil_list = jumlahkan(listku[0], listku[1])
hasil_dict = jumlahkan(dictku['p_satu'], dictku['p_dua'])
print(f'hasil_list: {hasil_list}')
print(f'hasil_dict: {hasil_dict}')
###################################################
# PYTHONIC WAY
###################################################
hasil_list = jumlahkan(*listku)
hasil_dict = jumlahkan(**dictku)
print(f'hasil_list: {hasil_list}')
print(f'hasil_dict: {hasil_dict}')
