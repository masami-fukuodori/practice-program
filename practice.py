class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    @classmethod
    def name(cls, lastname, firstname):
        print(f'私は{lastname} {firstname}です')
    



if __name__ == '__main__':
    p1 = Person('masami', 'fukuodori')

    print(p1.firstname, p1.lastname)
    Person.name = name()

