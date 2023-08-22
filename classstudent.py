#클래스를 선언합니다.
class Student:
    def __init__(self, name, korean, math, english, science): 
		self.name = name
		self.korean = korean
		self.math = math
		self.english = english
		self.science = science


# 학생 리스트를 선언합니다.
students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92)
]

# Student 인스턴트의 속성에 접근하는 방법
students[0].name
students[0].korean
students[0].math
students[0].english
students[0].science