class Student:

    cls = 10
    sec = 'A'

    def __call__(self, *args, **kwds):
        print('Under call method')

    def __format__(self, format_spec):
        if format_spec == "name":
            return f"Person's Name: {self.name}"
        elif format_spec == "age":
            return f"Person's Age: {self.age}"
        else:
            return f"{self.name}, {self.age} years old"
    
    def __dir__(self):
        return ['msg']

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('New Student created')

    @staticmethod
    def msg():
        print('Hi, I am a student!')


s1 = Student('Dinesh', 15)
s2 = Student('Ranjeet', 16)

s1()

print(format(s1, name))
print(f"{s1:age}") 

print(dir(s1))

s1.msg()