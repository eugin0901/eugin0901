#클래스를 선언한다.
class Student:
	#생략
	def __eq__(self, value):
		if not isinstance(value, Student):
			raise TypeError("Student 클래스의 인스턴스만 비교할 수 있습니다.")
		returen self.get_sum() == value.get_sum()
	#생략

#학생을 선언합니다.
student_a = Student("윤인성", 87, 98, 88, 95)

#비교합니다.
student_a == 10