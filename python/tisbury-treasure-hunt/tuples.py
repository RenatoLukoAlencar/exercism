"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    return record[1]


def convert_coordinate(coordinate):
    return (coordinate[0], coordinate[1])


def compare_records(azara_record, rui_record):
    return convert_coordinate(azara_record[1]) in rui_record


def create_record(azara_record, rui_record):
    return (
        azara_record + rui_record
        if compare_records(azara_record, rui_record)
        else "not a match"
    )


def clean_up(combined_record_group):
    report = ""

    for item in combined_record_group:
        report = report + str((item[0], item[2], item[3], item[4])) + "\n"

    return report
