import sqlite3

# Connect to the database (this will create the file if it doesn't exist)
conn = sqlite3.connect('signup.db')

# Create a cursor object
cursor = conn.cursor()

# SQL command to create the 'info' table
# Using "IF NOT EXISTS" prevents an error if you run the script multiple times.
create_table_query = """
CREATE TABLE IF NOT EXISTS info (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    password TEXT NOT NULL
);
"""

# Execute the command
print("Creating 'info' table...")
cursor.execute(create_table_query)
print("Table 'info' created successfully.")

# Commit the changes to the database
conn.commit()

# Close the connection
conn.close()