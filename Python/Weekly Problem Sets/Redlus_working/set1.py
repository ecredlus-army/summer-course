
#------------------------------------------------------------------
##### ------------------------ PROBLEM 1 -------------------- #####

# x = 1

# current_name = str(input("What's your name? "))
# fav_num = int(input("What's your favorite number? "))
# marker = "*"
# border = ""

# while x < fav_num:
#     border += marker
#     x += 1

# print(border)
# print(f"* Hello, {current_name}!. *")
# print(f"* Your favorite number is {fav_num} *")
# print(f"* Your number is a {type(fav_num)} *")
# print(f"* As a float it would be {float(fav_num)} *")
# print(border)


#------------------------------------------------------------------
##### ------------------------ PROBLEM 2 -------------------- #####

# num_start = int(input("Pick a start value: "))
# num_stop = int(input("Pick an ending value: "))
# num_step = int(input("Set a step value: "))
# num_type = str(input("EVEN, ODD, or ALL? ")).lower()
# direction = str(input("Count UP or DOWN? ")).lower()

# x = range(num_start, num_stop + 1, num_step)
# if direction == "down":
#     x = range(num_start, num_stop - 1, -num_step)

# # print(x)

# for i in x:
#     if num_type == "all":
#         print(i, end=' ')
#     elif num_type == "even":
#         if i % 2 == 0:
#             print(i, end=' ')
#     else:
#         if i % 2 == 1:
#             print(i, end=' ')

#------------------------------------------------------------------
##### ------------------------ PROBLEM 3 -------------------- #####

# soldier_n = str(input("What's your name, Soldier? "))
# soldier_r = str(input("What's your rank? "))
# pushups = int(input("How many pushups? "))
# runtime = float(input("2-mile run time (mm:ss)? "))
# runtime_m = int(runtime)
# runtime_s = int((runtime - runtime_m) * 100)
# runtime_t = runtime_m * 60 + runtime_s
# runtime_per_mile_m = int((runtime_t / 2) / 60)
# runtime_per_mile_s = int((runtime_t / 2) % 60)

# print(f"""
# == AFTER-ACTION REPORT ===
# Soldier: {soldier_r} {soldier_n}
# Push-ups: {pushups}
# 2-mile run: {runtime_m}:{runtime_s:02} minutes
# Average pace: {runtime_per_mile_m}:{runtime_per_mile_s:02} mimnutes per mile
# DISMISSED.
# """)

#------------------------------------------------------------------
##### ------------------------ PROBLEM 4 -------------------- #####

distance = int(input("Total distance of the trip in miles? "))
mpg = int(input("Car's fuel efficiency in miles per gallon (MPG)? "))
cur_price = float(input("Current price of gas per gallon ($x.xx)? "))
total_cents = round(cur_price * 100)

gallons_needed = float(distance / mpg)
cost_cents = gallons_needed * total_cents
total_costs = cost_cents / 100

print(f"""
--- Road Trip Fuel Estimate ---
Distance:         {distance} miles
Fuel efficiency:  {mpg} MPG
Gas price:        ${cur_price} / gallon

Gallons needed:   {gallons_needed:.2f}
Total fuel costs: ${total_costs:.2f}

--- Price Scenarios ---""")

cost_range = range(total_cents, total_cents +101, 50)
for i in cost_range:
    per_cost = i / 100
    print(f"Gas @ ${(per_cost):.2f}/gal: Total = ${(gallons_needed * per_cost):.2f}")