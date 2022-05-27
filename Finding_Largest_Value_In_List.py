# Python Finding largest number in a list with user input

### Option 1 - Using sort function to find largest number
numbers = input("Enter numbers: ").split()
numbers_list = [numbers]
print(f'Original input numbers from user: {numbers_list}')

numbers.sort(reverse=True)
print(f'Original input number after sort: {numbers}')
print(f'Largest number in list: {numbers[0]}')

### Option 2 - Using for loop to iterate thru list and selecting largest number
largest = numbers[0]
for number in numbers:
      if number > largest:
            largest = number
print(f'Largest number using for loop {largest}')

### Return only unique values within user inputs
unique = []
for number in numbers:
      if number not in unique:
            unique.append(number)
unique.sort(reverse = True)
print(f'Only unique values: {unique}')