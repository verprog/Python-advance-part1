# a = 'test'
# print(type(str))
#
# class My:
#     pass
#
# print(type(My))

def my_func():
    pass


a = type('MyClass',(), {'attr1': 1,
                        'attr2': 2,
                        'func_1': my_func})
print(a)
print(dir(a))
print(a.attr1)
print(a.attr2)

