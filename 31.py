kecepatan = [60, 40, 80, 60, 90, 30, 110, 20]
ambang_batas = 100
###################################################
# CONVENTIONAL WAY
###################################################
laju_normal = True
for laju in kecepatan:
    if laju > ambang_batas:
        laju_normal = False
        print('kecepatan melampaui ambang batas')
        break
if laju_normal:
    print('laju kendaraan normal')
###################################################
# PYTHONIC WAY
###################################################
for laju in kecepatan:
    if laju > ambang_batas:
        print('kecepatan melampaui ambang batas')
        break
else:
    print('laju kendaraan normal')
