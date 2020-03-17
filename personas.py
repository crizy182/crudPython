class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f'Hello, my name is: {self.name} and I\'m { self. age} years old')

if __name__ == '__main__':

    name = input('¿what\'s your name?')
    age = input('¿How old are you?')

    person = Person(name,age)
    # print(f'hola {age}')
    person.say_hello()