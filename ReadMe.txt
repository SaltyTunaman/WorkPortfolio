"""========================================================================================
    This python script will pull data from a database (SQL Server Management Studio) using
pyodbc & pandas libraries. Then it will clean & export the data file into a designated
folder in .csv format. This is accomplished by using the following These steps:

    1. Install the librarires by typing 'pip install pyodbc' and 'pip install pandas' in
        the command line. *when typing the commands be sure to EXCLUDE the single quotes*
    2. import the libraries with the statement 'import pandas' and 'import pyodbc'.
        *EXCLUDE the single quotes when using the import function*
    3. A connection needs to be estblished with SSMS. In order to accomplish this
       the connection details need to be established. For this connection the variables
       will consist of (Server, Database) for a secure server then establish variables for
       (Username, Password).
    4. With the connection details assigned a CONNECTION STRING will now need to be
       created. The primary components for the connection string are (Driver, Server,
       Database). Include (Username, Password) for connections to secure servers.
    5. Use a 'try' statement as an exception could occure in the code block.
    6. Create the connection to the database using the connection string.
    7. Create a cursor that will execute and fetch the SQL queries.
    8. Store the data from the fetchall as a variable i.e. 'results'.
    9. Create a dataframe using the fetchall results that will eventually be used for
       the output file.
   10. Clean dataframe, this will make it easier to read in the output file.
   11. Designate the pathway, ending with the filename for the output file. Index=False
       will remove the dataframe indexing.
   12. Best practice is to always print a message that tells you if the job was successful
       or if an error had occured.
   13. Save and export cleaned datafile.
   14. The expected exception of this 'try' statement is an error. Create error message for
       exceptions as best practice.
   15. When connecting to a source or creating a cursor its best practice to ensure you
       close those pathways to prevent resource leaks.
   16. Print message for success or failure of job.
========================================================================================"""
import pandas as pd #pandas has been importaed as the alias pd
import pyodbc

# Connection details
server = '*Server Name*'
database = '*Database Name*'
# username = '*srvr UserName*'
# passwork = '*srvr Password*'


# Connection String
conn_str = (
    f'DRIVER=*ODBC driver*;' # You can find the driver info under 'ODBC data source' *Windows
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

    # Execute sample query
    cursor.execute('SELECT TOP (10) *column* FROM *table name*')

    # Fetch the results and store them in the 'results' variable
    results = cursor.fetchall()

    # Create a DataFrame from the results
    df = pd.DataFrame(results, columns=['*column*'])

    # Clean the data in the *column*
    df['*column*'] = df['*column*'].apply(lambda x: str(x).replace("(", "").replace(")", "").replace(",", "").replace("'", ""))

    # Variable contains pathway and filename where the output will be saved
    output_file = r'C:\*File Pathway\DatCleanProj.csv'

    # Saves file to the specified filepath with
    df.to_csv(output_file, index=False)

    # If no errors occure the system will print this message
    print(f'Data exported to {output_file} successfully.')

    # Close the cursor and connection
    cursor.close()
    conn.close()

# This will print a message in the event of an error.
except pyodbc.Error as e:
    print(f'Error connecting to SQL Server: {e}')