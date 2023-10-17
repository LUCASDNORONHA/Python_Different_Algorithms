def soma(x, y, z=None):
    if z is not None:

        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)

soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(10, 3, 20)

soma(y=9, z=0, x=7)