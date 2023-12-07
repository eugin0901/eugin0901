measurements = input("Enter the measurements as a list:")
measurement = eval(measurements)
print(measurement)

measurement.sort()

n = len(measurement)

if n % 2 == 0:
    middle1 = measurement[n // 2 - 1]
    middle2 = measurement[n // 2]
    median = (middle1 + middle2) / 2
else:
    median = measurement[n // 2]

print(f"Median: {median}")


