class Lonely(object):
    instance = None

    def __new__(cls, name, surname):
        if cls.instance is None:
            cls.instance = object.__new__(cls)
        return cls.instance

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return 'Lonely(My name is {}, my surname is {})'.format(self.name, self.surname)


q = Lonely('Nazar', 'Koblay')
print (q)
