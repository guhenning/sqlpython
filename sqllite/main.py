import sqlite3
from pathlib import Path
from dotenv import load_dotenv
import os

import customer

ROOT_DIR = Path(__file__).parent
DB_NAME = "db.sqlite3"
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = "customers"


def db_session(query, params=""):
    con = sqlite3.connect(DB_FILE)  # open connection
    cursor = con.cursor()  # pass the connection commands terminal to cursor
    cursor.execute(query, params)  # execute this comand
    data = cursor.fetchall()
    con.commit()  # send comand
    cursor.close()  # close terminal
    con.close()  # close connection
    return data


# Create Table if dont exists
def create_table_if_dont_exists():
    query = (
        f"CREATE TABLE IF NOT EXISTS {TABLE_NAME}"
        "("
        "id INTEGER PRIMARY KEY AUTOINCREMENT,"
        "name TEXT,"
        "age INTEGER,"
        "weight REAL"
        ")"
    )
    # execute this comand
    db_session(query=query)


# Insert in Table #
def insert_customer(customer):
    name = customer.get_name()
    age = customer.get_age()
    weight = customer.get_weight()
    params = (name, age, weight)
    query = (
        f"INSERT INTO {TABLE_NAME} (id, name, age, weight)" f"VALUES (NULL, ?, ?, ?)"
    )
    db_session(query=query, params=params)


# TODO
# def insert_multiplcustomer(name, age, weight):
#     con = sqlite3.connect(DB_FILE)
#     cursor = con.cursor()
#     params = (name, age, weight)
#     cursor.execute(
#         f"INSERT INTO {TABLE_NAME} (id, name, age, weight)" f"VALUES (NULL, ?, ?, ?)",
#         params,
#     )
#     con.commit()
#     cursor.close()
#     con.close()


def select_customer(id):
    query = f"SELECT * FROM {TABLE_NAME} WHERE id={id}"
    data = db_session(query=query)
    customer = data[0]  # take index 0 from list of customers
    return customer


def update_customer(id, customer):
    name = customer.get_name()
    age = customer.get_age()
    weight = customer.get_weight()
    customer_to_update = select_customer(id)  # retrieve customer from data base
    name = (
        customer_to_update[1] if name == "" else name
    )  # if passing new name set new name else use the old name from retrieved customer
    age = customer_to_update[2] if age == "" else int(age)
    weight = customer_to_update[3] if weight == "" else float(weight)
    params = (name, age, weight, id)
    query = f"UPDATE {TABLE_NAME} SET name = ?, age = ?, weight = ? WHERE id = ?"
    db_session(query, params)


# Delete from table by id
def delete_customer(id):
    query = f"DELETE FROM {TABLE_NAME} WHERE id = {id}"
    db_session(query=query)


def select_all():
    query = f"SELECT * FROM {TABLE_NAME}"
    data = db_session(query=query)

    for row in data:
        _id, name, age, weight = row
        print(f"ID: {_id} Name: {name} Age: {age} Weight: {weight}")


# Just print test if executing this file directly not from imports
if __name__ == "__main__":
    print("Test")
