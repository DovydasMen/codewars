import sqlite3
import random
import matplotlib.pyplot as plt
import numpy as np

conn = sqlite3.connect("Employees.db")

c = conn.cursor()

with conn:
    c.execute("""CREATE TABLE IF NOT EXISTS employees (
              name text,
              surname text,
              salary integer
                )""")
    
NAMES = ["John", "Kyle", "Walker", "Anna", "Hanna"]
SURNAMES = ["One", "Two", "Three", "Four"]


# for item in range(0,200):
#     with conn:
#         c.execute(f"INSERT INTO employees VALUES ('{random.choice(NAMES)}', '{random.choice(SURNAMES)}', {random.randint(0, 2000)})")
      

with conn:
    c.execute("SELECT * FROM employees WHERE salary > 1000 AND surname = 'Two'")
    values = c.fetchall()

with conn:
    c.execute("INSERT INTO employees VALUES ('Dovydas', 'Menk', 2000)")

with conn:
    c.execute("SELECT name, salary FROM employees")
    print(c.fetchall())

with conn:
    c.execute("SELECT DISTINCT name FROM employees")
    print(c.fetchall())

with conn:
  #Note: The COUNT(DISTINCT column_name) is not supported in Microsoft Access databases.
  #(SELECT Count(*) AS Distinctnames FROM (SELECT DISTINCT name FROM employees ))
  c.execute("SELECT COUNT(DISTINCT name) FROM employees")
  print(c.fetchall())


#WHERE could have a lot of operators. = - equals, > - greater, < - lower, >= greater or equal, <= lower or equal, <> or != not equal, BETWEEN - range specific, LIKE search patern, IN to specify multiple possible values for a column
    

salaries = []
total_employees = []
counter = 1
for item in values:
    salaries.append(item[2])
    total_employees.append(counter)
    counter +=1


avarage = sum(salaries) / len(total_employees)


# plt.scatter(total_employees, salaries)
# plt.axhline(y = np.nanmean(avarage))
# plt.show()
#Just a games.