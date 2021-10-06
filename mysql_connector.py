import mysql.connector
from mysql.connector import Error


        
def add_query(table_num,query):
    
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database="jarvis",
                                             user='root',
                                             password='root',
                                             port=3307)
        if connection.is_connected():
            cursor = connection.cursor(buffered=True)
            cursor.execute("select database();")

            
            try:
                cursor.execute("INSERT INTO session{vari} VALUES(\"{queryy}\");".format(vari=table_num, queryy=query))
            except Error as e:
                print("not added to database: ",e)
            
            cursor.close()
            connection.commit()
            connection.close()
    except Error as e:
        print("Error while connecting to MySQL", e)

    return " query added to database"
