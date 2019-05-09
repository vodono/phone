import os
import sqlite3
import sys

from sqlite3 import Error


class Config:
    numbers_to_select = 10
    output_as_string = False


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
        sys.exit(0)

    return conn


def create_table(conn):
    table_phone_numbers = """ CREATE TABLE IF NOT EXISTS phone_numbers (
                                id integer PRIMARY KEY,
                                number text NOT NULL UNIQUE); """
    try:
        cursor = conn.cursor()
        cursor.execute(table_phone_numbers)
    except Error as e:
        print(e)
        sys.exit(0)

    return None


def select_numbers_first_digits(conn, digits):
    sql_select = "SELECT number FROM phone_numbers WHERE number LIKE ?"

    try:
        cursor = conn.cursor()
        cursor.execute(sql_select, (digits+'%', ))
    except Error as e:
        print(e)
        sys.exit(0)

    numbers_list = []

    for number in cursor.fetchmany(Config.numbers_to_select):
        numbers_list.append(number[0] if Config.output_as_string else int(number[0]))

    return numbers_list


def main():
    conn = create_connection(
        os.path.join(
            os.path.dirname(os.path.abspath( __file__ )),
            'phone_db'
        )
    )

    with conn:
        create_table(conn)

        while True:
            digits = str(input('Enter first digits or "exit": '))

            if digits == 'exit':
                print("Exited!")
                break

            print(select_numbers_first_digits(conn, digits))


if __name__ == '__main__':
    main()
