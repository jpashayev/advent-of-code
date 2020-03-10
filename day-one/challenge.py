def get_fuel_module_masses():
    num_list = []
    with open('input.txt') as f:
        for line in f:
            mass = int(line.strip())
            num_list.append(mass)
    return num_list


def get_module_fuel(fuel_module_mass):
    return fuel_module_mass // 3 - 2


def get_filler_fuel(fuel_module_mass):
    total_filler_fuel = 0
    while fuel_module_mass >= 9:
        fuel_module_mass = fuel_module_mass // 3 - 2
        total_filler_fuel += fuel_module_mass
    return total_filler_fuel


def get_total_fuel(fuel_module_masses):
    total_fuel = 0
    for fuel_module_mass in fuel_module_masses:
        total_fuel += get_module_fuel(fuel_module_mass)
    return total_fuel


def get_total_filler_fuel(fuel_module_masses):
    total_fuel = 0
    for fuel_module_mass in fuel_module_masses:
        total_fuel += get_filler_fuel(fuel_module_mass)
    return total_fuel


def part_one():
    fuel_module_masses = get_fuel_module_masses()
    total_fuel = get_total_fuel(fuel_module_masses)
    print(f'The total fuel requirements are {total_fuel}')


def part_two():
    fuel_filler_mass = get_fuel_module_masses()
    total_filler_fuel = get_total_filler_fuel(fuel_filler_mass)
    print(f'The total fuel requirements are {total_filler_fuel}')
    # pass


if __name__ == '__main__':
    part_one()
    part_two()
