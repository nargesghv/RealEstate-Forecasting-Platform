import pyodbc
import pandas as pd

server = 'your_azure_sql_server.database.windows.net'
database = 'your_database_name'
username = 'your_username'
password = 'your_password'
driver= '{ODBC Driver 17 for SQL Server}'

conn = pyodbc.connect(
    f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
)

cursor = conn.cursor()

df = pd.read_csv("../data/processed_toronto_hpi.csv")

table_name = "TorontoRealEstate"

create_table_query = f"""
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='{table_name}' and xtype='U')
CREATE TABLE {table_name} (
    Date DATE,
    HPI FLOAT,
    Year INT,
    Month INT
)
"""

cursor.execute(create_table_query)
conn.commit()

for _, row in df.iterrows():
    cursor.execute(
        f"INSERT INTO {table_name} (Date, HPI, Year, Month) VALUES (?, ?, ?, ?)",
        row.Date, row.HPI, row.Year, row.Month
    )

conn.commit()
cursor.close()
conn.close()
