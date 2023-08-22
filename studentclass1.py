from ClassStudent import Students


# 학생을 한 명씩 반복합니다.
print("이름", "총점", "평균", sep="\t")
for student in students:
    # 출력합니다.
    print(student.to_string())