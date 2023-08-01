import sqlite3
import pandas as pd

square = lambda n: n*n*n #ABREVIACIÓN DE CREACIÓN DE FUNCIÓN
print(square(10))

with sqlite3.connect("Northwind.db") as conn:
    conn.create_function("square",1,square)
    cursor = conn.cursor()
    cursor.execute('SELECT *, square(Price) as Precio_al_cubo FROM Products WHERE PRICE > 0')
    results = cursor.fetchall()
    results_df = pd.DataFrame(results)

print(results_df)