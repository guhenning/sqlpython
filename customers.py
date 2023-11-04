from main import (
    create_table_if_dont_exists,
    insert_customer,
    select_customer,
    update_customer,
    select_all,
    delete_customer,
)


create_table_if_dont_exists()

# insert_customer("Rafael", 33, 75)
# update_customer(1, name="Wiliam", age=55, weight=60)
# delete_customer(9)
# select_customer(1)
select_all()
