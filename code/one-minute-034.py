def f(pos1, pos2, /, pos_kwd, *, kwd):
    print('Valores:')
    print(f'pos1: {pos1}, pos2: {pos2}, pos_kwd: {pos_kwd}, kwd: {kwd}')


f(1, 2, 3, kwd=4)
f(1, 2, pos_kwd=3, kwd=4)
f(1, 2, 3, 4)
