"""
This file is for adding all the initializations for mysql

useful incase we need to remake the tables on a new machine

"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mysql123rootpswd",
  database="testdb"
)

mycursor = mydb.cursor()


def make_request_table():
    """
    Makes a requests table
    Must contain the stock it is requesting, the date it is requesting it on, accuracy of prediction it wants and number of days after that it wants the predicted price
    """
    mycursor.execute("CREATE TABLE requests (id INT AUTO_INCREMENT PRIMARY KEY, uuid varchar(36), lookupstep int, ticker VARCHAR(255), reqdate date, epochs int)")
    
    pass

def make_response_table():
    """
    Makes the response table that moves the requests once they are served
    """
    mycursor.execute("CREATE TABLE response (id INT AUTO_INCREMENT PRIMARY KEY, uuid varchar(36), lookupstep int, ticker VARCHAR(255), responsedate date, epochs int, filepath varchar(100), priceprediction int")
    pass


# def make_users_table():
#     """
#     Table where we store user data
#     """
#     pass


def make_logs_table():
    """
    Table where we store metrics and logs for our code
    """
    pass

if __name__ == "__main__":
    pass #just run everything
