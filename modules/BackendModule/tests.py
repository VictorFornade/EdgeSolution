import sqldatabase
import pyodbc
import unittest

def test_connection():
    """Ensure error raised if insert fails due to truncation"""
    driver, server, database, username, password = sqldatabase.get_credentials()
    print('driver is: ',driver)
    print('server is: ',server)
    print('database is: ',database)
    print('username is: ',username)
    print('password is: ',password)
    conn = sqldatabase.connect(driver,server,database,username,password)
    cursor = conn.cursor()
    def mytest():
        cursor.execute("INSERT INTO [dbo].[Metrics] (ID,IDRoom,Temperature,Humidity,CO2) VALUES (NEWID(),'df700779-f17e-40ff-94b2-9a5fdc864f5b',a,65,200)")
    unittest.TestCase.assertRaises(mytest, pyodbc.DataError)

if __name__ == '__main__':
    test_connection() 