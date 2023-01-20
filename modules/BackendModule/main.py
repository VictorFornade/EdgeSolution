import os
import sqldatabase
import pyodbc

from dotenv import load_dotenv
from flask import Flask

load_dotenv()

app = Flask(__name__)

global conn
global cursor
global DEBUG

DEBUG=os.getenv('DEBUG')

@app.route('/')
def welcoming_page():
    '''Main page'''
    return 'Welcome!'
    
@app.route('/co2/<roomname>', methods=['GET'])
def get_co2(roomname):
    ''' Get CO2 readings from the database'''
    cursor = conn.cursor()
    row = None
    returnstring = ''

    try:
        cursor.execute(
                        f"SELECT TOP (1) [CO2] FROM [master].[dbo].[Metrics]\
                        INNER JOIN [master].[dbo].[Rooms]\
                        ON [master].[dbo].[Rooms].[ID] = [master].[dbo].[Metrics].[IDRoom]\
                        WHERE [master].[dbo].[Rooms].[Name] = '{roomname}'"
        )
        row = cursor.fetchone()
        if eval(DEBUG):
            print(row)
        returnstring = f'CO2 is {row[0]}'

    except Exception as err:
        print(f"Exception: {err}") 

    return returnstring

@app.route('/temperature/<roomname>', methods=['GET'])
def get_temperature(roomname):
    ''' Get temperature readings from the database'''
    cursor = conn.cursor()
    row = None
    returnstring = ''

    try:
        cursor.execute(
                        f"SELECT TOP (1) [Temperature] FROM [master].[dbo].[Metrics]\
                        INNER JOIN [master].[dbo].[Rooms]\
                        ON [master].[dbo].[Rooms].[ID] = [master].[dbo].[Metrics].[IDRoom]\
                        WHERE [master].[dbo].[Rooms].[Name] = '{roomname}'"
        )
        row = cursor.fetchone()
        if eval(DEBUG):
            print(row)
        returnstring = f'Temperature is {row[0]}'
    
    except Exception as err:
        print(f"Exception: {err}") 
    
    return returnstring

@app.route('/humidity/<roomname>', methods=['GET'])
def get_humidity(roomname):
    ''' Get temperature readings from the database'''
    cursor = conn.cursor()
    row = None
    returnstring = ''

    try:
        cursor.execute(
                        f"SELECT TOP (1) [Humidity] FROM [master].[dbo].[Metrics]\
                        INNER JOIN [master].[dbo].[Rooms]\
                        ON [master].[dbo].[Rooms].[ID] = [master].[dbo].[Metrics].[IDRoom]\
                        WHERE [master].[dbo].[Rooms].[Name] = '{roomname}'"
        )
        row = cursor.fetchone()
        if eval(DEBUG):
            print(row)
        returnstring = f'Humidity is {row[0]}'
    except Exception as err:
        print(f"Exception: {err}") 
    
    return returnstring

def main():
    '''Main function'''
    if eval(DEBUG):
        print("ip is: ",os.getenv('ip'))
        print("port is: ",os.getenv('port'))
    global conn
    global cursor
    driver, server, database, username, password = sqldatabase.get_credentials()
    conn = sqldatabase.connect(driver, server, database, username, password)
    cursor = conn.cursor()
    app.run(debug=True,host=os.getenv('ip'),port=int(os.getenv('port')))

if __name__ == '__main__':
    main()