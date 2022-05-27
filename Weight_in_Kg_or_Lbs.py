# Python Simple Weight Calculator in Kg or Lbs
# James Mitra - Project 1 - 05/23/2022

weight = int(input("Please enter your weight: "))
count = 0
count_max = 3

while count < count_max:
    k_or_l = input("(K)g or (L)bs: ")
    count += 1
    if k_or_l.upper() == 'L':
        print(count)
        weight = round((weight / 2.2), 2)
        print("You're weight in kilograms is " + str(weight))
        break
    elif k_or_l.upper() == 'K':
        weight = round((weight * 2.2), 2)
        print("You're weight in pounds is " + str(weight))
        break
else:
    print("Try again")