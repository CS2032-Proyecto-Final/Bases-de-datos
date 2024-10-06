import os
import psycopg2
import csv

# Database connection details
DB_HOST = "34.202.67.244"
DB_PORT = "8000"
DB_NAME = "clientes_db"
DB_USER = "postgres"
DB_PASSWORD = "utec"

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host=DB_HOST,
    port=DB_PORT,
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)
cur = conn.cursor()

# Function to export a table to CSV
def export_table_to_csv(table_name):
    # Create the directory for the table if it doesn't exist
    if not os.path.exists("clientes_db/" + table_name):
        os.makedirs("clientes_db/" + table_name)

    # Query to get the contents of the table
    query = f"SELECT * FROM {table_name};"
    cur.execute(query)

    # Write the table content to CSV without headers
    csv_file_path = f"clientes_db/{table_name}/{table_name}.csv"
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(cur.fetchall())
    print(f"Exported table {table_name} to {csv_file_path}")

# Get the list of all tables in the database
cur.execute("""
    SELECT table_name 
    FROM information_schema.tables 
    WHERE table_schema = 'public' 
    AND table_type = 'BASE TABLE';
""")
tables = cur.fetchall()

# Export each table to a CSV file
for table in tables:
    table_name = table[0]
    export_table_to_csv(table_name)

# Close the cursor and connection
cur.close()
conn.close()
