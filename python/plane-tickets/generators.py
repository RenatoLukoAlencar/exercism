def generate_seat_letters(number):
    letters = ["A", "B", "C", "D"]
    id = 0
    for i in range(number):
        yield letters[id]
        id += 1 if id != 3 else -3


def generate_seats(number):
    letters = generate_seat_letters(number)
    n_row = 1
    for letter in letters:
        yield f"{n_row}{letter}"
        n_row += 1 if letter == "D" else 0
        n_row += 1 if n_row == 13 else 0


def assign_seats(passengers):
    assigned_seats = {}
    seat = generate_seats(len(passengers))
    for passenger in passengers:
        assigned_seats[passenger] = next(seat)
    return assigned_seats


def generate_codes(seat_numbers, flight_id):
    for seat in seat_numbers:
        prefix = f"{seat}{flight_id}"
        zeros = "0" * (12 - len(prefix))
        yield f"{prefix}{zeros}"
