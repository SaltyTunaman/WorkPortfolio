import pandas as pd
import pyodbc

# Connection details
server = 'SPYWARE-EXE55\SQLEXPRESS'
database = 'AdventureWorks2022'
# username = 'SPYWARE-EXE55\salty'
# passwork = '********'


# Connection String
conn_str = (
    f'DRIVER=SQL Server;'
    f'SERVER={server};'
    f'DATABASE={database};'
    #f'UID={username};'
    #f'PWD'={password};
)

try:
    # Database connection
    conn = pyodbc.connect(conn_str)
    # Create cursor
    cursor = conn.cursor()

    # Create dataframe from query results
    cursor.execute('SELECT TOP (10) Title FROM DimEmployee')
    results = cursor.fetchall()
    df = pd.DataFrame(results, columns=['Title'])

    # Clean the data from selected column of the dataframe
    df['Title'] = df['Title'].apply(lambda x: str(x).replace("(", "").replace(")", "").replace(",", "").replace("'", ""))

    # create pathway for the output file
    output_file = r'C:\Users\Salty\OneDrive\Documents\Project outputs\DatCleanProj.csv'

    # Save and export data file
    df.to_csv(output_file, index=False)

    print(f'Data exported to {output_file} successfully.')

    # Close the cursor and connection
    cursor.close()
    conn.close()

except pyodbc.Error as e:
    print(f'Error connecting to SQL Server: {e}')