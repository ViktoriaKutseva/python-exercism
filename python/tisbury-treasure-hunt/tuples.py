"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """

    return record[1]


def convert_coordinate(coordinate: str):
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """
    coordinate = tuple(coordinate)
    return coordinate

    


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """
    record_1 = tuple(azara_record[1])
    record_2 = rui_record[1]
    
    if record_1 == record_2:
        return True
    return False
    

def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """
    record_1 = tuple(azara_record[1])
    record_2 = rui_record[1]    
    
    if record_1 == record_2:
        new_records = azara_record + rui_record
        return new_records
    return 'not a match'



def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.

    The return statement should be a multi-lined string with items separated by newlines.

    (see HINTS.md for an example).
    """
    new_records = []
    # for index, records in enumerate(combined_record_group):          
    #     for index, item in enumerate(records):
    #         if index == 1:
    #             continue
    #         elif index == 3:
    #             coordinate = tuple(records[3])
    #             new_record.append(coordinate)
    #         elif index == 4:
    #             new_record.append(records[4])                    
    #         else:
    #             new_record.append(str(item))
    # return new_record
    for record in combined_record_group:
        new_records.append(str((record[0], record[2], record[3], record[4])))
    return '\n'.join(new_records) + '\n'
    
