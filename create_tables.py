import psycopg2

# TODO change this to your own credentials.
conn = psycopg2.connect(database="huwebshop",
                        user="postgres",
                        password="password",
                        host="localhost",
                        port=5433)

cur = conn.cursor()

# Drops colums that already exist
cur.execute("DROP TABLE IF EXISTS brand CASCADE")
cur.execute("DROP TABLE IF EXISTS category CASCADE")
cur.execute("DROP TABLE IF EXISTS sub_category CASCADE")
cur.execute("DROP TABLE IF EXISTS sub_sub_category CASCADE")
cur.execute("DROP TABLE IF EXISTS gender CASCADE")

# create columns
cur.execute("""CREATE TABLE brand(_id INT PRIMARY KEY, brand VARCHAR);""")
cur.execute("""CREATE TABLE category(_id INT PRIMARY KEY, category VARCHAR);""")
cur.execute("""CREATE TABLE sub_category(_id INT PRIMARY KEY, sub_category VARCHAR);""")
cur.execute("""CREATE TABLE sub_sub_category(_id INT PRIMARY KEY, sub_sub_category VARCHAR);""")
cur.execute("""CREATE TABLE gender(_id INT PRIMARY KEY, gender VARCHAR);""")

# Drops tables if they already exist
cur.execute("DROP TABLE IF EXISTS profiles CASCADE")
cur.execute("DROP TABLE IF EXISTS sessions CASCADE")
cur.execute("DROP TABLE IF EXISTS products CASCADE")
cur.execute("DROP TABLE IF EXISTS viewed_products CASCADE")
cur.execute("DROP TABLE IF EXISTS bought_products CASCADE")

# Create profiles table
cur.execute("""CREATE TABLE profiles
                (_id VARCHAR PRIMARY KEY,
                 buids VARCHAR);""")

# Creates sessions table
cur.execute("""CREATE TABLE sessions
                (buids VARCHAR PRIMARY KEY,
                 profid VARCHAR,
                 sale BOOLEAN,
                 starttime TIMESTAMP,
                 FOREIGN KEY (profid) REFERENCES profiles (_id));""")

# Creates Products table
cur.execute("""CREATE TABLE products
                (_id VARCHAR PRIMARY KEY, 
                brand_id INT,
                category_id INT,
                sub_category_id INT,
                sub_sub_category_id INT,
                gender_id INT,
                FOREIGN KEY (brand_id) REFERENCES brand (_id),
                FOREIGN KEY (category_id) REFERENCES category (_id),
                FOREIGN KEY (sub_category_id) REFERENCES sub_category (_id),
                FOREIGN KEY (sub_sub_category_id) REFERENCES sub_sub_category (_id),
                FOREIGN KEY (gender_id) REFERENCES gender (_id));""")
# Creates viewed products table
cur.execute("""CREATE TABLE viewed_products
                (profid VARCHAR,
                 prodid VARCHAR,
                 FOREIGN KEY (profid) REFERENCES profiles (_id),
                 FOREIGN KEY (prodid) REFERENCES products (_id));""")

cur.execute("""CREATE TABLE bought_products
                (_id SERIAL PRIMARY KEY,
                profile_id VARCHAR,
                product_id VARCHAR,
                FOREIGN KEY (profile_id) REFERENCES profiles (_id),
                FOREIGN KEY (product_id) REFERENCES products (_id));""")


conn.commit()
conn.close()

