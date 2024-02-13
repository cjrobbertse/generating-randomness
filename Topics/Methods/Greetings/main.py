class Person:
    def __init__(self, name):
        self.name = name

    # create the method greet here
    def greet(self):
        return f"Hello, I am {self.name}!"
        pass


person = Person(input())
print(person.greet())
