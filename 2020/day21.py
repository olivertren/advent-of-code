from collections import Counter, defaultdict
from functools import lru_cache

from utils import get_input, print_answers


@lru_cache(None)
def get_foods_and_allergens(line):
    foods, allergens = line.split(" (contains ")
    allergens = allergens[:-1].split(", ")
    foods = foods.split(" ")
    return foods, allergens


def get_ingredients(i_):
    ingredients = defaultdict(Counter)
    for line in i_:
        foods, allergens = get_foods_and_allergens(line)

        for a in allergens:
            for f in foods:
                ingredients[f][a] += 1

    return ingredients


def get_ingredients_counter(i_):
    ingredients_counter = Counter()
    for line in i_:
        foods, allergens = get_foods_and_allergens(line)

        for f in foods:
            ingredients_counter[f] += 1

    return ingredients_counter


def get_allergen_counter(i_):
    allergen_counter = Counter()
    for line in i_:
        foods, allergens = get_foods_and_allergens(line)

        for a in allergens:
            allergen_counter[a] += 1

    return allergen_counter


def part_one(i_):
    ingredients = get_ingredients(i_)
    ingredients_counter = get_ingredients_counter(i_)
    allergen_counter = get_allergen_counter(i_)

    num_appear = 0

    for f in ingredients:
        allergens = ingredients[f]
        possible = False
        for a in allergens:
            if allergens[a] >= allergen_counter[a]:
                possible = True
                break
        if not possible:
            num_appear += ingredients_counter[f]

    return num_appear


def part_two(i_):
    ingredients = get_ingredients(i_)
    allergen_counter = get_allergen_counter(i_)

    possible_allergens = defaultdict(set)

    for f in ingredients:
        as_ = ingredients[f]
        for a in as_:
            if as_[a] >= allergen_counter[a]:
                possible_allergens[f].add(a)

    ingredient_to_allergen_map = {}
    while len(ingredient_to_allergen_map) < len(possible_allergens):
        matched_allergens = set()
        for ingredient, allergens in possible_allergens.items():
            if len(allergens) == 1:
                allergen = allergens.pop()
                ingredient_to_allergen_map[ingredient] = allergen
                matched_allergens.add(allergen)

        for ingredient in possible_allergens:
            possible_allergens[ingredient] -= matched_allergens

    sorted_ingredients = sorted(ingredient_to_allergen_map, key=lambda i: ingredient_to_allergen_map[i])
    return ",".join(sorted_ingredients)


def print_answers_for_input(input_):
    p1 = part_one(input_)
    p2 = part_two(input_)

    print_answers(p1, p2)


input_ = get_input(f"2020/day21test")
print("Tests")
print_answers_for_input(input_)

input_ = get_input(__file__)
print("Actual")
print_answers_for_input(input_)
