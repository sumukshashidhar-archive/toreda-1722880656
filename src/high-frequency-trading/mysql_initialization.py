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
    """MySQL commands used directly as comments for now, can also be directly executed on mysql """
    """CREATE DATABASE IF NOT EXISTS `pythonlogin` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
    USE `pythonlogin`;

    CREATE TABLE IF NOT EXISTS `accounts` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
  	`username` varchar(50) NOT NULL,
  	`password` varchar(255) NOT NULL,
  	`email` varchar(100) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

INSERT INTO `accounts` (`id`, `username`, `password`, `email`) VALUES (1, 'test', 'test', 'test@test.com');
    """
#     pass


def make_logs_table():
    """
    Table where we store metrics and logs for our code
    """
    pass

if __name__ == "__main__":
    pass #just run everything
