"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    generated = 0
    seats_list = ["A", "B", "C", "D"]
    while generated < number:
        for letter in seats_list:
            if generated >= number:
                break
            yield letter
            generated += 1

def generate_seats(number):
    """Generate a series of identifiers for airline seats.
    
    row_count = 1

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    seats_list = ["A", "B", "C", "D"]
    row = 1
    generated = 0 

    while generated < number:
        if row == 13:
            row += 1
        for letter in seats_list:
            if generated >= number:
                break
            yield f"{row}{letter}"
            generated += 1
        row += 1

def assign_seats(passengers):
    """
    Assigns sequential seats to passengers, skipping row 13.
    
    Example: {"Adele": "1A", "Björk": "1B", ...}
    """
    seats_list = ["A", "B", "C", "D"]
    row = 1
    seat_index = 0
    passengers_dict = {}

    for passenger in passengers:
        if row == 13:
            row += 1

        seat_letter = seats_list[seat_index % 4]
        seat_number = f"{row}{seat_letter}"
        passengers_dict[passenger] = seat_number

        seat_index += 1
        if seat_index % 4 == 0:
            row += 1  # Move to next row every 4 seats

    return passengers_dict
        
        
        

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    for seat in seat_numbers:
        base = f"{seat}{flight_id}"
        zeros_needed = 12 - len(base)
        padded = base + "0" * zeros_needed
        yield padded

