# 实现描述符协议所需的方法
class Grade:

    def __set_name__(self, owner, name):
        self.internal_name = "_" + name

    def __get__(self, instance, instance_type): # instance: 拥有该属性的实例
        if instance is None:
            return self
        return getattr(instance, self.internal_name)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError("Grade must be between 0 and 100")
        setattr(instance, self.internal_name, value)


class Exam:
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()


first_exam = Exam()
first_exam.math_grade = 78
first_exam.writing_grade = 89
first_exam.science_grade = 94
print(
    first_exam.__dict__
)  # {'_math_grade': 78, '_writing_grade': 89, '_science_grade': 94}

second_exam = Exam()
second_exam.math_grade = 65
second_exam.writing_grade = 87
second_exam.science_grade = 99
print(
    second_exam.__dict__
)  # {'_math_grade': 65, '_writing_grade': 87, '_science_grade': 99}
