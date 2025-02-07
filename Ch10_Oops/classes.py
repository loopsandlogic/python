class Student:
    name = 'Dinesh'
    cls = 10
    sec = 'A'
    age = 15

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('New Student created')

s1 = Student('Dinesh', 15)

print(s1.name)
print(s1.age)

s2 = Student('Ranjeet', 16)
print(s2.name)
print(s2.age)

# s1_name = 'Dinesh'
# s1_age = 15
# s1_cls = 10
# s1_sec = 'A'

# s2_name = 'Ranjeet'
# s2_age = '16'
# s2_cls = '10'
# s2_sec = 'A'

# def details(name, age):
#         print('Student detail is name:', name, 'age:', age )


# details(s1_name, s1_age)
# details(s2_name, s2_age)

# s1