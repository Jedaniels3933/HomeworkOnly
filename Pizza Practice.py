pizza_type = ['deep dish' , 'sis', 'Ny style', 'Detroit']
toppings = ['pepp', 'sausage', 'ham' , 'pineapple', 'olives']

for type1 in pizza_type:
    for topping in toppings:
        print("I have a ", type1, "pizza with ", topping)

print("+" * 100)

#Loop though topping twice

for topping1 in toppings:
    for topping2 in toppings:
        if topping1 == topping2:
            print("Double", topping1)
        else:print(topping1, topping2)

pay_dirt = ['dirt', 'dirt' , 'dirt' ,'dirt','gold', 'dirt', 'dirt', 'dirt']  

for scoop in pay_dirt:
    print("Panning for gold")
    if scoop == 'gold':
        print("Found Gold, lets go") 
        break
    else:
        print("Just more dirt, keep looking")
#continues

#Square each number but only if odd

nums = [12 , 256 , 1146 , 478 , 21, 3457]

for num in nums: 
    if num % 2 == 0:
        continue
    print("Original number:",num )
    num **= 2  
    print("Squared", num)

#pass 

my_list = [1,2,3]
for item in my_list:
    pass



#While loop
# for and if compined




        
        
    
    
