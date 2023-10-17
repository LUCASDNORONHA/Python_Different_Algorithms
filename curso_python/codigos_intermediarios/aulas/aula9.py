def do_greeting(greeting):
    def greet(name):
        return f'{greeting}, {name}'
    return greet

say_goodmorning = do_greeting('Good morning, ')
say_goodnight = do_greeting('Good morning, ')

for name in ['Maria', 'Joana', 'Lucas']:
    print(say_goodmorning(name))
    print(say_goodnight(name))

