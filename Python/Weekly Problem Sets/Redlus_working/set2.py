import math

def pizzas_needed(people: int,
                  slices_per_person: int,
                  slices_per_pizza: int ) -> int:
    tot_slices = people * slices_per_person
    pizza_needed_total = math.ceil(tot_slices / slices_per_pizza)
    return pizza_needed_total