import os
from supabase import create_client
from dotenv import load_dotenv
from gotrue.errors import AuthError

load_dotenv()
DB_URL = os.environ.get("DB_URL")
PUBLIC_KEY = os.environ.get("PUBLIC_KEY")
PRIVATE_KEY = os.environ.get("PRIVATE_KEY")


supabase = create_client(DB_URL, PUBLIC_KEY)


def insert_customer(customer):
    name = customer.get_name()
    age = customer.get_age()
    weight = customer.get_weight()
    data_to_insert = {"name": name, "age": age, "weight": weight}

    supabase.table("customers").insert(data_to_insert).execute()


# Select all
def select_all():
    response = supabase.table("customers").select("*").execute()
    data = response.data or []
    for row in data:
        print(row)
    return data


# select part of the table by setting the column to select to True
def select_part(
    selectId=False,
    selectCreatedAt=False,
    selectName=False,
    selectAge=False,
    selectWeight=False,
):
    # create list of columns to select
    selected_columns = []

    # check if column to be selected is true and if is add it to the list
    if selectId:
        selected_columns.append("id")
    if selectCreatedAt:
        selected_columns.append("created_at")
    if selectName:
        selected_columns.append("name")
    if selectAge:
        selected_columns.append("age")
    if selectWeight:
        selected_columns.append("weight")
    # convert list to string
    selected_columns = ",".join(selected_columns)
    # select
    response = supabase.table("customers").select(selected_columns).execute()
    # get data
    data = response.data or []
    # for each row print
    for row in data:
        print(row)
    return data


def select_customer(id):
    response = supabase.table("customers").select("*").eq("id", id).execute()
    customer = response.data[0]
    return customer


def select_where(id="", created_at="", name="", age="", weight=""):
    # create query
    query = supabase.table("customers").select("*")
    # Add conditions for the fields that are not empty
    if id:
        query = query.eq("id", id)
    if created_at:
        query = query.eq("created_at", created_at)
    if name:
        query = query.eq("name", name)
    if age:
        query = query.eq("age", age)
    if weight:
        query = query.eq("weight", weight)
    # Execute the query
    response = query.execute()

    # Retrieve the data
    data = response.data or []
    # print(data)
    return data


def update_customer(id, customer):
    name = customer.get_name()  # get passed values
    age = customer.get_age()
    weight = customer.get_weight()
    customer_to_update = select_customer(id)  # retrieve customer from data base
    # create empty dict
    customer_dict = {}
    # add values to update
    # if customer field is not empty add to dict
    if name != "":
        customer_dict["name"] = name
    if age != "":
        customer_dict["age"] = age
    if weight != "":
        customer_dict["weight"] = weight
    supabase.table("customers").update(customer_dict).eq("id", id).execute()


def delete_customer(id):
    supabase.table("customers").delete().eq("id", id).execute()


def sign_up(email, password):
    user = supabase.auth.sign_up({"email": email, "password": password})


def sign_in(email, password):
    try:
        data = supabase.auth.sign_in_with_password(
            {"email": email, "password": password}
        )

        session = supabase.auth.get_session()
        supabase.postgrest.auth(session.access_token)
    # print(session.access_token)

    except AuthError:
        print("Login failed!")


def sign_out():
    supabase.auth.sign_out()


# TODO
def upload_profile_pic():
    bucket_name = "profile_pic"
    new_profile_pic = "profile.png"
    supabase.storage.from_(bucket_name).upload("/user1/profile.png", new_profile_pic)


def get_profile_pic():
    url = supabase.storage.from_("profile_pic").get_public_url("profile.png")
    print(url)
