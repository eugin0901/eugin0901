import math

def main():
    list_of_numbers = eval(input("Enter the list of numbers: "))
    mean = calculate_mean(list_of_numbers)
    std = calculate_std(list_of_numbers)
    min_value, max_value = calculate_range(mean, std)
    print("The inlier ranges from {:.2f} to {:.2f}".format(min_value,max_value))
    eliminated_outlier_list = eliminate_outlier(list_of_numbers,min_value, max_value)
    print("The result is {}".format((eliminated_outlier_list)))
    
def calculate_mean(list_of_numbers):
    if len(list_of_numbers) == 0:
        return 0
    return sum(list_of_numbers) / len(list_of_numbers)


def calculate_std(list_of_numbers):
    if len(list_of_numbers) < 2:
        return 0
    mean = calculate_mean(list_of_numbers)
    variance = sum((x - mean) ** 2 for x in list_of_numbers) / len(list_of_numbers)  # Changed this line
    return math.sqrt(variance)
    
def calculate_range(mean, std):
    min_value = mean - 2 * std
    max_value = mean + 2 * std
    
    return min_value, max_value


def eliminate_outlier(list_of_numbers, min_value, max_value):
    result = [x for x in list_of_numbers if min_value <= x <= max_value]
    return result


main()