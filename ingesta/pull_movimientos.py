import os
import pymysql
import csv

# Database connection details
DB_HOST = "34.202.67.244"
DB_PORT = 8001
DB_NAME = "movimientos_db"
DB_USER = "root"
DB_PASSWORD = "utec"

# Connect to the MySQL database
conn = pymysql.connect(
    host=DB_HOST,
    port=DB_PORT,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)
cur = conn.cursor()

# Function to export a table to CSV
def export_table_to_csv(table_name):
    # Create the directory for the table if it doesn't exist
    directory = f"movimientos_db/{table_name}"
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Query to get the contents of the table
    query = f"SELECT * FROM {table_name};"
    cur.execute(query)

    # Write the table content to CSV without headers
    csv_file_path = f"{directory}/{table_name}.csv"
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(cur.fetchall())
    print(f"Exported table {table_name} to {csv_file_path}")

# Get the list of all tables in the database
cur.execute("SHOW TABLES;")
tables = cur.fetchall()

# Export each table to a CSV file
for table in tables:
    table_name = table[0]
    export_table_to_csv(table_name)

# Close the cursor and connection
cur.close()
conn.close()
