import psycopg2
import random
import os

# Internal Database URL from your Render PostgreSQL instance
DATABASE_URL = os.getenv("DATABASE_URL")

names = [
    "John", "Emma", "Liam", "Olivia", "Sophia",
    "Noah", "James", "Ava", "William", "Mia"
]

cities = [
    "Bangalore",
    "Mumbai",
    "Delhi",
    "Chennai",
    "Hyderabad",
    "Pune",
    "Kolkata"
]

name = random.choice(names)

phone = "9" + "".join(str(random.randint(0, 9)) for _ in range(9))

email = f"{name.lower()}{random.randint(100,999)}@gmail.com"

city = random.choice(cities)

conn = psycopg2.connect(DATABASE_URL)

cursor = conn.cursor()

cursor.execute("""
INSERT INTO Customers
(CustomerName, Phone, Email, City)
VALUES (%s,%s,%s,%s)
""", (name, phone, email, city))

conn.commit()

cursor.close()
conn.close()

print("New customer inserted successfully.")