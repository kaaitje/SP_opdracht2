import psycopg2
import pymongo
import csv

# TODO change this to your own credentials.
conn = psycopg2.connect(database="huwebshop",
                        user="postgres",
                        password="password",
                        host="localhost",
                        port=5433)

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["huwebshop"]


def profiles_csv():
    """
    creates a csv file called profiles with profile information such as
    buid and profile_id
    :return: A message that says it has completed the task and how much info it retrieved
    """
    count = 0
    with open('profiles.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["buid", "_id"])
        for entry in db["profiles"].find():
            if "buids" in entry and len(entry["buids"]) > 0:
                if str(entry["buids"][0]) not in 'profiles.csv':
                    writer.writerow((str(entry["buids"][0]),
                                     str(entry["_id"])))
                count += 1
        return 'completed' + str(count) + " buids retrieved"


def products_csv():
    """
    Creates a csv file called products with product information
    product_id, brand, category, sub_category, sub_sub_category and gender

    :return: A message that says it has completed the task and how much info it retrieved.
    """
    count = 0
    with open('product.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["_id", "brand", "category", "sub_category", "sub_sub_category", "gender"])
        for entry in db["products"].find():
            try:
                writer.writerow((str(entry["_id"]),
                                 str(entry["brand"]),
                                 str(entry["category"]),
                                 str(entry["sub_category"]),
                                 str(entry["sub_sub_category"]),
                                 str(entry["gender"])))
                count += 1

            except:
                continue

        return 'completed' + str(count) + " products retrieved"


def sessions_csv():
    """
    Creates a csv file called session with session information like
    buid, session_id, session_start and has_sale

    :return: A message that says it has completed the task and how much info it retrieved.
    """
    count = 0
    with open('sessions.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["buid", "session_id", "session_start", "has_sale"])
        for entry in db["sessions"].find():
            try:
                writer.writerow((str(entry["buid"][0]),
                                 str(entry["_id"]),
                                 str(entry["session_start"]),
                                 str(entry["has_sale"])))
                count += 1
            except:
                continue
    return "completed " + str(count) + " sessions retrieved"


def bought_product_csv():
    count = 0
    with open('bought_products.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["_id", "bought_products"])

        for entry in db["sessions"].find():
            line = []
            products = []
            try:
                if entry["has_sale"] and len(entry["order"]["products"]) >= 1:
                    line.append(entry["_id"])
                    for i in entry["order"]["products"]:
                        products.append(entry["order"]["products"][-1]["id"])
                    line.append(products)
                    writer.writerow(line)
                    count += 1

            except:
                continue

    return "completed " + str(count) + " sessions with bought products retrieved"


def viewed_product_csv():
    """
    Creates a csv file called viewed_products with profile_id and the products that profile viewed.
    :return: A message that says it has completed the task and how much info it retrieved.
    """
    count = 0
    with open('viewed_products.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["_id", "viewed_before"])
        for entry in db["profiles"].find():
            try:
                if len(entry["recommendations"]["viewed_before"]) > 0:
                    writer.writerow((entry["_id"], entry["recommendations"]["viewed_before"]))
                count += 1

            except:
                continue

    return "completed " + str(count) + " profiles with viewed products retrieved"




