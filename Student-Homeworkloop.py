#

submitted = ['Alice','Bob', "Charlie", "David"]
attended = ['Charlie','Eve', 'Alice', 'Frank']


for student in attended:
    if student in submitted:
        print( student, "Good Work")
    else:
        print(student,  " You suck " )

print('=' * 50)


nums = [ 12, 234 , 567, 98 , 34 ,123567, 246 , 178, 15326]

for num in nums:
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")

for num in nums:
    if num /3 == 0:
        print(num, "is divisible by 3")
    else:
        print(num, "is not divisible by 3")
print('=' * 50)

temps = [56 , 105 , 99 ,124, 200 , 50 , 78, 779, 0 , 2541]
above_100 = []

for temp in temps:
    if temp <85:
        print(temp, "is below 85")
    elif temp > 100:
        print(temp, "is above 100")
    else:
        print( "OK, we fucked")

for temp in temps:
    if temp < 100:
        below_100.append(temp)


print(above_100)
print(below_100)

print('=' * 100)


print(above_100)



   








