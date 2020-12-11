from utils import get_input, print_answers


def get_seat_id(seat):
    def _get_binary(letter):
        return "0" if letter == "F" or letter == "L" else "1"

    return int("".join([_get_binary(letter) for letter in seat]), 2)


seats = get_input(__file__)
seats = {get_seat_id(seat) for seat in seats}

print_answers(max(seats), ({i for i in range(min(seats), max(seats) + 1)} - seats).pop())
