class MyBaseClass:
    def __init__(self, value):
        self.__value = value

    def get_value(self):
        return self.__value


class MyStringClass(MyBaseClass):
    def get_value(self):
        return str(super().get_value())


class MyIntegerSubclass(MyStringClass):
    def get_value(self):
        return int(self._MyStringClass__value)  # Not updated


foo = MyIntegerSubclass(5)
print(
    foo.get_value()
)  # AttributeError: 'MyIntegerSubclass' object has no attribute '_MyStringClass__value'
