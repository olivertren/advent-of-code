from collections import Counter

from utils import get_input, print_answers


def is_valid_one(row):
    nums, letter, password = row.split(" ")
    low_num, high_num = nums.split("-")
    low_num = int(low_num)
    high_num = int(high_num)
    letter = letter[0]

    letter_counts = Counter(password)
    return low_num <= letter_counts.get(letter, 0) <= high_num


def is_valid_two(row):
    nums, letter, password = row.split(" ")
    low_num, high_num = nums.split("-")
    low_num = int(low_num)
    high_num = int(high_num)
    letter = letter[0]

    return (password[low_num - 1] == letter) ^ (password[high_num - 1] == letter)


print_answers(sum(get_input(__file__, is_valid_one)), sum(get_input(__file__, is_valid_two)))
