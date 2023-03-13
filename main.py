import questionnaire
from demo import add_sales_data, get_total_prices, update_item, delete_row

if __name__ == "__main__":
    filename = "sales_data.csv"
    fields = [
        "Order Date",
        "Product Category",
        "Product Name",
        "Unit Price",
        "Quantity",
        "Discount",
    ]

    action = questionnaire.get_action()
    if action == "add":
        row = questionnaire.add_row()
        add_sales_data(row, filename)
    elif action == "total":
        total = get_total_prices(filename)
    elif action == "update":
        item = questionnaire.update_row(filename)
        update_item(item, filename, fields)
    elif action == "delete":
        item_to_remove = questionnaire.delete_row(filename)
        delete_row(item_to_remove, filename, fields)
