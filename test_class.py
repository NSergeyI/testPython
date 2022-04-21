class Rectangle:
    def __init__(self, a=1, b=1, c=1):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = (self.a + self.b + self.c) / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5


#
# rec = Rectangle(2, 2, 2)
# print(rec.area())
# rec = Rectangle()
# print(rec.area())

"""Модуль cs: демонстрация области видимости класса."""
mv = "module variable: mv"


def mf():
    return "module function (can be used like a class method in other languages): mf()"


class SC:
    scv = "superclass class variable: self.scv"
    __pscv = "private superclass class variable: no access"

    def __init__(self):
        self.siv = "superclass instance variable: self.siv (but use SC.siv for assignment)"
        self.__psiv = "private superclass instance variable: no access"

    def sm(self):
        return "superclass method: self.sm()"

    def __spm(self):
        return "superclass private method: no access"


class C(SC):
    cv = "class variable: self.cv (but use C.cv for assignment)"
    __pcv = "class private variable: self.__pcv (but use C.__pcv for assignment)"

    def __init__(self):
        SC.__init__(self)
        self.__piv = "private instance variable: self.__piv"

    def m2(self):
        return "method: self.m2()"

    def __pm(self):
        return "private method: self.__pm()"

    def m(self, p="parameter: p"):
        lv = "local variable: lv"
        self.iv = "instance variable: self.xi"
        print("Access local, global and built-in namespaces directly")
        print("local namespace:", list(locals().keys()))
        print(p)
        print(lv)
        print("global namespace:", list(globals().keys()))
        print(mv)
        print(mf())
        print("Access instance, class, and superclass namespaces through 'self'")
        print("Instance namespace:", dir(self))
        print(self.iv)
        print(self.__piv)
        print(self.siv)
        print("Class namespace:", dir(C))
        print(self.cv)
        print(self.m2())
        print(self.__pcv)
        print(self.__pm())
        print("Superclass namespace:", dir(SC))
        print(self.sm())
        print(self.scv)


# c = C()
# c.m()


class Element:
    def __init__(self, text=None, subelement=None):
        self.subelement = subelement
        self.text = text

    def __str__(self):
        value = '<{}>\n'.format(self.__class__.__name__.lower())
        if self.text:
            value += '{}\n'.format(self.text)
        if self.subelement:
            value += str(self.subelement)
        value += '</{}>\n'.format(self.__class__.__name__.lower())
        return value


class Html(Element):
    def __init__(self, text=None, subelement=None):
        super().__init__(text, subelement)

    def __str__(self):
        return super().__str__()


class Body(Element):
    def __init__(self, text=None, subelement=None):
        super().__init__(text, subelement)

    def __str__(self):
        return super().__str__()


class P(Element):
    def __init__(self, text=None, subelement=None):
        super().__init__(text, subelement)

    def __str__(self):
        return super().__str__()


para = P(text="this is some body text")
doc_body = Body(text="This is the body", subelement=para)
doc = Html(subelement=doc_body)
print(doc)
