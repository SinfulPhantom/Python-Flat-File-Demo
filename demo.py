import csv
import shutil
from tempfile import NamedTemporaryFile


def add_sales_data(data, filename):
    with open(filename, "a") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                data["order_date"],
                data["category"],
                data["product_name"],
                data["unit_price"],
                data["quantity"],
                data["discount"],
            ]
        )


def get_total_prices(filename):
    with open(filename, "r") as file:
        reader = csv.reader(file)
        header = next(reader)  # skip header row
        for row in reader:
            order_date = row[0]
            category = row[1]
            product_name = row[2]
            unit_price = float(row[3])
            quantity = int(row[4])
            discount = float(row[5])
            total_price = unit_price * quantity * (1 - discount)
            print(f"{order_date}: {category} - {product_name} - ${total_price}")


def update_item(item, filename, fields):
    tempfile = NamedTemporaryFile(mode="w", delete=False)

    with open(filename, "r") as file, tempfile:
        reader = csv.DictReader(file, fieldnames=fields)
        writer = csv.DictWriter(tempfile, fieldnames=fields, lineterminator="\n")

        for row in reader:
            if row["Product Name"] == item["product_name"]:
                row[item["column_to_change"]] = item["new_data"]
            writer.writerow(row)
    shutil.move(tempfile.name, filename)


def delete_row(item_to_delete, filename, fields):
    tempfile = NamedTemporaryFile(mode="w", delete=False)

    with open(filename, "r") as file, tempfile:
        reader = csv.DictReader(file, fieldnames=fields)
        writer = csv.DictWriter(tempfile, fieldnames=fields, lineterminator="\n")

        for row in reader:
            if row["Product Name"] != item_to_delete:
                writer.writerow(row)
    shutil.move(tempfile.name, filename)
