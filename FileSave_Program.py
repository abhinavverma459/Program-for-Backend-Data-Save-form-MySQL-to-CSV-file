import pymysql
import csv

# Function to fetch data from MySQL database and update CSV file
def update_csv(filename, table, host, user, password, database):
    # Connect to MySQL database
    try:
        conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        cursor = conn.cursor()

        # Fetch data from MySQL table
        cursor.execute(f"SELECT * FROM {table}")
        rows = cursor.fetchall()

        # Check if CSV file exists, if not create one
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)

            # Write header if the file is empty
            if file.tell() == 0:
                writer.writerow([i[0] for i in cursor.description])

            # Write data to CSV file
            for row in rows:
                writer.writerow(row)

        print("CSV file updated successfully.")

    except pymysql.Error as error:
        print("Failed to update CSV file:", error)

    finally:
        if conn.open:
            cursor.close()
            conn.close()

# Example usage
filename = "data.csv"
table = "students"
host = "localhost"
user = "root"
password = "root"
database = "scss"

update_csv(filename, table, host, user, password, database)
