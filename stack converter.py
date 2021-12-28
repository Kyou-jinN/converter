calculation_to_units = 64
name_of_unit = "items"


def stacks_to_units(num_of_stacks):
    return f"{num_of_stacks} stacks are {num_of_stacks * calculation_to_units} {name_of_unit}"

user_input = input("Convert Stacks to items:\n")
user_input_number = int(user_input)
calculated_value = stacks_to_units(user_input_number)
print(calculated_value)


