def menu():
    #You should display a menu here! Make it look pretty!
    print("----------- MENU -----------\n")
    print("[ #1. Mo's Special --- $16.30 ]\n - Random toppings; You get a surprise!\n")
    print("[ #2. Peperroni --- $12.50 ]\n - Classic Peperroni Pizza\n")
    print("[ #3. Cheese --- $9.99 ]\n - Classic Pizza with no toppings\n")
    print("[ #4. Skibidi Slicers --- $19.99 ]\n - a Pizza with all the toppings!\n")
    print("[ #5. Meat Lovers --- $14.99 ]\n - Lots of meaty mo's\n")
    print("[ #6. Vegetarian --- $12.99 ]\n - Vegetarian Option")
    start()
	
def orders():
    print(f"Your current order is: {order}")
    #Ask the user what they want, and add it into a list
    #until the user types -1
    x = 0
    while x != -1:
        if x != -1:
            x = int(input("Enter which Pizzas you would like to order. Type -1 to finish: "))
            order.append(x)
            print(f"Your current order contains: {order}")
    order.pop()
    print(f"--- Order Complete! --- \nYour current order contains: {order}")
    start()


def total(order_list):
    #look through their order list and calculate the cost
    cost = 0
    return cost
    
def start():
    user_exit = False
    while user_exit != True:

        print("---------------------\n- 1. Menu \n- 2. Order \n- 3. Calculate Total \n- 4. Exit\n--------------------")
        user_input = int(input("Choose what you want: \n"))
        if user_input == 1:
            menu()
        if user_input == 2:
            orders()
        if user_input == 4:
            print("\nThanks for stopping by!\n")
        user_input = True


    #Your code can go here
    #You may want to add to this if statement 

print("Welcome to the Pizza Store")
print("Please pick what you would like to do!")
start()
order = []
