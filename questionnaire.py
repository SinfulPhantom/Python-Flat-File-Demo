import csv
from questionary import form, select, text, Choice, confirm


def get_action():
    return select(
        "What would you like to do?",
        choices=[
            Choice("Add row", "add"),
            Choice("Get total prices", "total"),
            Choice("Update row", "update"),
            Choice("Delete row", "delete"),
        ],
    ).ask()


def add_row():
    return form(
        order_date=text("What is the order date? (YYYY-MM-DD)"),
        category=select(
            "Select product's category",
            choices=["Electronics", "Home & Garden", "Clothing"],
        ),
        product_name=text("Name of the product?"),
        unit_price=text("Price of the product?"),
        quantity=text("How many units have been sold?"),
        discount=text("Discount percentage as a decimal"),
    ).ask()


def update_row(filename):
    items = get_item_choices(filename)

    return form(
        product_name=select("Select item", choices=[item for item in items]),
        column_to_change=select(
            "What would you like to change?",
            choices=["Product Name", "Unit Price", "Quantity", "Discount"],
        ),
        new_data=text("Please enter the new value"),
    ).ask()


def delete_row(filename):
    items = get_item_choices(filename)

    product_name = select("Select item", choices=[item for item in items]).ask()
    validate = confirm(f"Are you sure you want to delete {product_name}?").ask()

    if validate:
        return product_name


def get_item_choices(filename):
    items = []
    with open(filename, "r", newline="") as file:
        reader = csv.reader(file)
        header = next(reader)
        [items.append(row[2]) for row in reader]

    return items
