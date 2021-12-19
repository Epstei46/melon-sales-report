# Working on the exercise at https://ed.devmountain.com/materials/data-bp-1/exercises/melon-sales-report/

SALESPERSON_INDEX = 0 # relating to line 28, BUT WRONG
INTERNET_INDEX = 1 # relating to line 28, BUT WRONG
DORKY_LINE_LENGTH = 3 # only used on line 7, not 26 or 41

print("*" * DORKY_LINE_LENGTH) # spacer line
f = open("orders-by-type.txt") # opens the file and saves it to a .txt object
melon_tallies = {"Musk":0, "Hybrid":0, "Watermelon":0, "Winter": 0} # sets initial count for each melon in a dictionary, melon type is the key and and integer is the value

for l in f: # iterates through each line in .txt file
    data = l.split("|") # split each line on "|", split into a list
    melon_type = data[1] # saves second value in list to melon_type object
    melon_count = int(data[2])# saves second value in list as an integer to melon_count object
    melon_tallies[melon_type] += melon_count # uses the above objects to increase the melon_count (value) for that melon_type (key) in melon_tallies

f.close() # closes the open .txt file
melon_prices = { "Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00 } # sets price per melon for each melon type in a dictionary
total_revenue = 0 # sets initial total_revenue at 0
for melon_type in melon_tallies: # iterates through each melon_type (key) in melon_tallies dictionary
    price = melon_prices[melon_type] # price per melon for this particular melon_type
    revenue = price * melon_tallies[melon_type] # revenue for this particular melon_type
    total_revenue += revenue # adds revenue to total_revenue
    # print("We sold %d %s melons at %0.2f each for a total of %0.2f" % (melon_tallies[melon_type], melon_type, price, revenue))
    print(f"We sold {melon_tallies[melon_type]} {melon_type} melons at {price:.2f} each for a total of {revenue:.2f}") # prints readable information in the terminal
print("******************************************") # spacer line
f = open("orders-with-sales.txt") # opens the file and saves it to a .txt object
sales = [0, 0] # sets initial sales to 0, with first relating to salespeople and second relating to internet sales
for line in f: # iterates through each line in .txt file
    d = line.split("|") # split each line on "|", split into a list
    if d[1] == "0": # if second value == "0"
        sales[0] += float(d[3]) # then add fourth value to sales[0]
    else:
        sales[1] += float(d[3]) # add fourth value to sales[1]
print(f"Salespeople generated ${sales[1]:.2f} in revenue.") # prints readable information in the terminal
print(f"Internet sales generated ${sales[0]:.2f} in revenue.") # prints readable information in the terminal
if sales[1] > sales[0]: # if salesperson sales is greater than internet sales
    print("Guess there's some value to those salespeople after all.")
else:
    print("Time to fire the sales team! Online sales rule all!")
print("******************************************") # spacer

# Possible refactoring:
#   Delete lines 3-5.
#   'spacer' lines could be combined into a spacer() function.
#   lines 7-17 could be combined into a function that takes the .txt file as an argument/parameter and returns the melon_tallies dictionary. Delete line 13-14 and change line 12 => _, melon_type, melon_count = l.split("|"). And line 15, change melon_count => int(melon_count)
#   lines 18-25 could be combined into a function that takes a dictionary (melon_tallies) as an argument/parameter.
# lines 27-40 could be combined into a function takes the .txt file as an argument/parameter.