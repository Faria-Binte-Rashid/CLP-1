numbers = {5, 3, 8, 1, 2, 9, 4}

even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even = even + num
    else:
        odd = odd + num

print("Even sum:", even)
print("Odd sum:", odd)
