#List Comprehensions

# var = []   added item for item in an iterrable 

students = [1,2,3]
shirt_list = [num * 2 for num in students]
print(shirt_list)

other_list = []
for num in students:
    other_list.append(num * 2)
print(other_list)

nums = [1,2,3,4,5,6,7,8,9,10]

evens = [num for num in nums if num % 2 == 0]
print(evens)

even2 = []
for num in nums:
    if num % 2 == 0:
        even2.append(num)
print(even2)


          


