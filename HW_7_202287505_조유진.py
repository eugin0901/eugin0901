def main():
    list_of_number = eval(input("Enter the numbers:"))
    list_of_number.sort(key=sum_of_digits)
    print("the sorting result is {}".format(str(list_of_number)))

def sum_of_digits(number):
    # the return value of this function should be
    # hint: (10, 7) > (10, 5) is True
    sum_digits = 0
    for i in str(number):
        sum_digits += int(i)
    return sum_digits, number
        
main()