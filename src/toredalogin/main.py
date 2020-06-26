from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re


app = Flask(__name__)

# Secret key for extra protection
app.secret_key = 'SecKey'

# Enter your database connection details below
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mysql123rootpswd'
app.config['MYSQL_DB'] = 'toredalogin'

# Intialize MySQL
mysql = MySQL(app)
