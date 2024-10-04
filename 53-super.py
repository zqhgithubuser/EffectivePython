class MyBaseClass:

    def __init__(self, value):
        self.value = value


# class TimesSeven(MyBaseClass):

#     def __init__(self, value):
#         MyBaseClass.__init__(self, value)
#         self.value *= 7

# class PlusNine(MyBaseClass):

#     def __init__(self, value):
#         MyBaseClass.__init__(self, value)
#         self.value += 9

# 菱形继承
# class ThisWay(TimesSeven, PlusNine):

#     def __init__(self, value):
#         TimesSeven.__init__(self, value)
#         PlusNine.__init__(self, value)

# foo = ThisWay(5)
# print("Should be (5 * 7) + 9 = 44 but is", foo.value)


class TimesSevenCorrect(MyBaseClass):

    def __init__(self, value):
        super().__init__(value)
        self.value *= 7


class PlusNineCorrect(MyBaseClass):

    def __init__(self, value):
        super().__init__(value)  # super确保MyBaseClass类的__init__初始化函数仅运行一次
        self.value += 9


class GoodWay(TimesSevenCorrect, PlusNineCorrect):

    def __init__(self, value):
        super().__init__(value)


foo = GoodWay(5)
print("Should be 7 * (5 + 9) = 98 and is", foo.value)

for cls in GoodWay.__mro__:
    print(cls)

# <class '__main__.GoodWay'>
# <class '__main__.TimesSevenCorrect'>
# <class '__main__.PlusNineCorrect'>
# <class '__main__.MyBaseClass'>
# <class 'object'>
