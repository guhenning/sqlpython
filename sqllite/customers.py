from main import (
    create_table_if_dont_exists,
    insert_customer,
    select_customer,
    update_customer,
    select_all,
    delete_customer,
)

import customer

customer1 = customer.customer(age=26)

create_table_if_dont_exists()

# insert_customer(customer1)
update_customer(10, customer1)
# delete_customer(9)
# select_customer(1)
# select_all()
