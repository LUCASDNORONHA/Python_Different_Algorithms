
x = 2

def escopo():
    global x
    x = 10

    def outra_funcao():
        global x
        y = x
        print(x, y)
    outra_funcao()
    print(x)

print(x)
escopo()
print(x)