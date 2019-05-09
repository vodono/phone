import sys

sys.path.insert(0, '.')
from src.main import create_connection, create_table, select_numbers_first_digits, Config


def insert_dummy_numbers(conn):
    sql_insert_dummy_phone_numbers = "INSERT OR IGNORE INTO phone_numbers(number) VALUES (?)"
    dummy_numbers = [
        (380676586587,),
        (380676586589,),
        (380676534861,),
        (380676534862,),
        (380676534863,),
        (380676534864,),
        (380676534865,),
        (380676534866,),
        (380676534867,),
        (380676534868,),
        (380676534869,),
        (380509874561,),
        (380501354967,)
    ]

    cursor = conn.cursor()
    cursor.executemany(sql_insert_dummy_phone_numbers, dummy_numbers)
    return None


def test_returned_numbers():
    conn = create_connection(':memory:')

    Config.numbers_to_select = 10
    Config.output_as_string = False

    with conn:
        create_table(conn)
        insert_dummy_numbers(conn)

        # test if only one item meet input
        assert select_numbers_first_digits(conn, '380509') == [380509874561]

        # test if more than maximum number_to_select meet input
        assert select_numbers_first_digits(conn, '38') == [
            380676586587,
            380676586589,
            380676534861,
            380676534862,
            380676534863,
            380676534864,
            380676534865,
            380676534866,
            380676534867,
            380676534868,
        ]

        # test if there are no items that meet input
        assert select_numbers_first_digits(conn, '1') == []

        # test if quantity of digits entered are more than number size possible
        assert select_numbers_first_digits(conn, '3806765865871') == []
