# dictionary for input
food = []

gas = []

# counter variable 
count = 1

countf = 1


# user input for the amount of people on this trip
# will prompt user until user enters a numeric value
# check to see if input is a numeric value

while True:
    travelers = input("How many people are paying for the trip: \n ")
    if (travelers.isdigit()) is True:
        traveler = int(travelers)
        print("Thanks for enterting the amount of travelers")
        break        
                                  
    if (travelers.isdigit()) is False:
        print("You did not enter an approperiate value try again")

# user input for the amount of days on this trip
# will prompt user until user enters a numeric value
# check to see if input is a numeric value

while True:
    day = input("How many days are on this trip: \n")
    if (day.isdigit()) is True:
        days = int(day)
        print("Thanks for enterting the amount of days")
        break        
                                  
    if (day.isdigit()) is False:
        print("You did not enter an approperiate value try again")   
 
                       

# takes values from days and prompt user to enter gas cost for each day.

for gasses in range(0, days):
    day_gas = float(input("Enter gas cost for day " + str(count) + str(":\n ")))
    gas.append(day_gas)
    #print(gas)
    print("Price entered for day", count, "is", f" ${day_gas}")
    count = count + 1
                      
# takes values from days and prompt user to ener food cost for each day

for foods in range(0, days):
    foods = float(input("Enter food cost for day " + str(countf) +str(": \n ")))
    food.append(foods)
    print("Price entered for day", countf, "is", f" ${foods}")
    countf = countf + 1

print("\n")

# averages food for all days
# format days to two decimal places
# displays daily food cost on average

averagess = sum(food)/len(food)
averages = "{:.2f}".format(averagess)
print("Food cost daily Average:", f" ${averages}")
#print(food)

# averages gas for all days
# format days to two decimal places
# displays daily gas cost on average

average2 = sum(gas)/len(gas)
average = "{:.2f}".format(average2)
print("Gas cost daily Average:", f" ${average}")
#print(gas)

print("\n")

# calculates the food cost for each traveler for the trip duration
# formats the cost to two decimal places

food_cost_per_traveler1 = sum(food)/traveler
food_cost_per_traveler = "{:.2f}".format(food_cost_per_traveler1)
print("Food Cost per", traveler, "travelers for the duration of the trip: ", f" ${food_cost_per_traveler}")


# calculates the gas cost for each traveler for the trip duration
# formats the cost to two decimal places

gas_cost_per_traveler1 = sum(gas)/traveler
gas_cost_per_traveler = "{:.2f}".format(gas_cost_per_traveler1)
print("Gas Cost per",traveler, "travelers for the duration of the trip: ", f" ${gas_cost_per_traveler}")


