#beginning salary 입력
salary = int(input("Enter beginning salary:"))
print(salary)

#change 수식 계산하기
change = 1
for i in range(4) :
    change *= 1.05

salary*= change

#New salary와 Change 출력하기
print("New salary:,${:,.2f}".format(salary))
print("Change:{:,.2%}".format(change-1))
