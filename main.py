import random

def get_numbers_ticket(min_num, max_num, quantity):

    if min_num < 1 or max_num > 1000 or quantity < 1 or quantity > (max_num - min_num + 1):
        return []


    numbers_set = set()
    while len(numbers_set) < quantity:
        numbers_set.add(random.randint(min_num, max_num))


    return sorted(list(numbers_set))


lot_numbers = get_numbers_ticket(1, 49, 6)
print("Your lottery numbers:", lot_numbers)