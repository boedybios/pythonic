def one():
    print('satu-one')


def two():
    print('dua-two')


def three():
    print('tiga-three')


case = 'dua'
###################################################
# CONVENTIONAL WAY
###################################################
if case == 'satu':
    one()
elif case == 'dua':
    two()
elif case == 'tiga':
    three()
###################################################
# PYTHONIC WAY
###################################################
switch = {
    'satu': one,
    'dua': two,
    'tiga': three
}
switch[case]()
