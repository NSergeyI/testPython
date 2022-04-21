print(type(5))
print(type('sdsds'))
print(type('d'))
print(type([1, 1]))
print(type((3, 2)))
print(type({3, 6}))
print(type(type(3)))
print(type(3.5))
print('_______________')
class A:
    pass
class B(A):
    pass
a = A()
b = B()
b_class = b.__class__
print(type(b))
print(type(b_class))
print(type(B))
print(b_class.__bases__)
class C():
    pass
c = C()
print(isinstance(a, A))
print(isinstance(a, B))
print(isinstance(b, A))
print(isinstance(c, A))
print(isinstance(a, C))
print(isinstance(3, type(12)))
print('_______________')
print(issubclass(A, A))
print(issubclass(B, A))
print(issubclass(A, B))


class TypedList:
    def __init__(self, example_element, initial_list=[]):
        self.type = type(example_element)
        if not isinstance(initial_list, list):
            raise TypeError("Second argument of TypedList must be a list.")
        for element in initial_list:
            self.__check(element)
            self.elements = initial_list[:]
    def __check(self, element):
        if type(element) != self.type:
            raise TypeError("Attempted to add an element of incorrect type to a typed list.")
    def __setitem__(self, i, element):
        self.__check(element)
        self.elements[i] = element
    def __getitem__(self, i):
        return self.elements[i]
    def __len__(self):
        return len(self.elements)
    def __delitem__(self, key):
        del self.elements[key]
    def append(self, element):
        self.__check(element)
        self.elements.append(element)
    def __str__(self):
        return self.elements.__str__()

x = TypedList(1, [1,2,3])
print(len(x))
x.append(1)
del x[2]
print(x)

class TypedListList(list):
    def __init__(self, example_element, initial_list=[]):
        self.type = type(example_element)
        if not isinstance(initial_list, list):
            raise TypeError("Second argument of TypedList must be a list.")
        for element in initial_list:
            self.__check(element)
            super().__init__(initial_list)
    def __check(self, element):
        if type(element) != self.type:
            raise TypeError("Attempted to add an element of incorrect type to a typed list.")
    def __setitem__(self, i, element):
        self.__check(element)
        super().__setitem__(i, element)