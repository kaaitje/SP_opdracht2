import psycopg2
# TODO change this to your own credentials.
c = psycopg2.connect(database="huwebshop",
                              user="postgres",
                              password="password",
                              host="localhost",
                              port=5433)
cur = c.cursor()

filenames = ['profiles', 'sessions', 'products', 'viewed_products', 'bought_products']

for filename in filenames:
    with open(filename+'.csv') as csvfile:
        print("Copying {}...".format(filename))
        cur.copy_expert("COPY "+filename+" FROM STDIN DELIMITER ',' CSV HEADER", csvfile)
        c.commit()

c.commit()
cur.close()
c.close()
