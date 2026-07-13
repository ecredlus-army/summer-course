import math

# def pizzas_needed(people: int,
#                 slices_per_person: int,
#                 slices_per_pizza: int,
#                 buffer: str ) -> list:
#     if buffer == 'yes':
#         tot_slices = math.ceil(people * 1.15) * slices_per_person

#     tot_slices = people * slices_per_person
#     pizza_needed_total = math.ceil(tot_slices / slices_per_pizza)

#     left_over_slices = math.ceil((pizza_needed_total - tot_slices/slices_per_pizza) * slices_per_pizza)

#     return pizza_needed_total, left_over_slices



# people = int(input("How many people? "))
# slices = int(input("How many slices per person? "))
# slices_pizza = int(input("How many slices per pizza? "))
# buffer = str(input("Do you want to plan for extra (YES/NO)?")).lower()

# results = pizzas_needed(people,slices, slices_pizza, buffer)
# print(f"{results[0]} pizzas needed and {results[1]} slices left over for {people} guests")


def o2_status(reading: int) -> str:
    if reading > 23:
        return "HIGH"
    elif reading > 19:
        return "NORMAL"
    elif reading >= 15:
        return "LOW"
    else:
        return "CRITICAL"

low_cnt = 0
normal_cnt = 0
high_cnt = 0
critical_cnt = 0

readings = [21, 20, 19, 17, 16, 14, 12, 15, 17, 21, 22, 21]

for index, value in enumerate(readings):
    result = o2_status(value)
    print(f"Hour {index + 1}: {value}% - {result}")
    if result == "LOW":
        low_cnt += 1
    elif result == "NORMAL":
        normal_cnt += 1
    elif result == "HIGH":
        high_cnt += 1
    else:
        critical_cnt += 1
        print("** ALERT: TAKE ACTION IMMEDIATELY **")

print("")
print(f"""=== STATUS SUMMARY ===
NORMAL: {normal_cnt} hours
LOW:    {low_cnt} hours
CRITICAL: {critical_cnt} hours
HIGH:       {high_cnt} hours      
      """)