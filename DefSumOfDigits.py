import csv
def sum_of_digits(number):
    if len(number) >=1 and len(number) <=10:
        sum = 0
        for digit in number:
            try:
                digit = int(digit)
            except ValueError:
                print('be careful!')
                break
            sum += digit
        if sum == 0:
            return "non coorect or 0"
        return sum

with open("test_numbers.csv", 'r') as f:
    reader = csv.reader(f)
    for string in reader:
        for num in string:
            print('input value: ', string, 'output result: ', num)