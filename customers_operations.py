from supabase_connection import (
    insert_customer,
    select_part,
    select_all,
    select_customer,
    select_where,
    update_customer,
    upload_profile_pic,
    get_profile_pic,
    delete_customer,
    sign_up,
    sign_in,
    sign_out,
)
import customer

customer1 = customer.customer(name="Rafael", age=32, weight=71)

# sign_up(email="gustavo-guidi@hotmail.com", password="123456")
# sign_in(email="gustavo-guidi@hotmail.com", password="1234567") # wrong login
sign_in(email="gustavo-guidi@hotmail.com", password="123456")
# insert_customer(customer1)
# select_all()
# select_customer(4)
# select_part(selectName=True, selectAge=True, selectId=True)
# select_where(age=32)
# update_customer(6, customer1)
upload_profile_pic(1, profile_pic_path="profile_renata.png")
# get_profile_pic(1)
# delete_customer(8)

sign_out()
