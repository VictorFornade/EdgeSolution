import os
import pyodbc
from dotenv import load_dotenv

load_dotenv()

def get_credentials():
    '''Get the credentials to connect to the database'''
    try:
        driver = os.getenv('driver')  
        server = os.getenv('server')
        database = os.getenv('database')
        username = os.getenv('usrname')
        password = os.getenv('password')  

    except Exception as err:
        print(f"Exception: {err}") 

    return driver, server, database, username, password

def connect(driver: str, server: str, database: str, username: str, password: str):
    '''Connect to the database'''
    try:
        conn =  pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
        print("Connection successful!")
        return conn
   
    except Exception as err:
        print(f"Exception: {err}") 
    return None

'''
if __name__ == '__main__':
    driver, server, database, username, password = get_credentials()
    print('driver is: ',driver)
    print('server is: ',server)
    print('database is: ',database)
    print('username is: ',username)
    print('password is: ',password)
    conn = connect(driver,server,database,username,password)
    cursor = conn.cursor()
    cursor.execute("SELECT TOP 1 CO2 FROM [dbo].[Metrics]")
    row = cursor.fetchone()
    print(row)    
'''