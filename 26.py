###################################################
# CONVENTIONAL WAY
###################################################
fileku = open('pesan.txt', 'w')
fileku.write('Ayo Belajar Pythoic\n')
fileku.write('Di Channel Indonesia Belajar\n')
fileku.close()
###################################################
# PYTHONIC WAY
###################################################
with open('pesan.txt', 'w') as fileku:
    fileku.write('Ayo Belajar Pythoic\n')
    fileku.write('Di Channel Indonesia Belajar\n')
