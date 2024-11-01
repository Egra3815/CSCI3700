   from flask import Flask, render_template
import util
import psycog2
import Error

# create an application instance
# all requests it receives from clients to this object for handling
# we are instantiating a Flask object by passing __name__ argument to the Flask constructor.
# The Flask constructor has one required argument which is the name of the application package.
# Most of the time __name__ is the correct value. The name of the application package is used
# by Flask to find static assets, templates and so on.
app = Flask(Homework2)

# evil global variables
# can be placed in a config file
# here is a possible tutorial how you can do this
username='raywu1990'
password='test'
host='127.0.0.1'
port='5432'
database='dvdrental'


@app.route('/api/Question1')
def Question1():
#Question 1
#Inserts a new row
	try:
     	cursor, connection = util.connect_to_db(username,password,host,port,database)
    	# execute SQL commands
   	cursor.execute("Insert INTO basket_a (id,fruit_name) VALUES (%s, %s)", (5,'Cherry'))
    	connection.commit
    	util.disconnect_from_db(connection,cursor)
    	return "Success!"
except Exception as e
	Return f"Error!"
	util.disconnect_from_db(connection,cursor)


def Question2():
	try:
     	cursor, connection = util.connect_to_db(username,password,host,port,database)
    	# execute SQL commands
   	cursor.execute("SELECT DISTINCT item FROM basket_a;")
    	item_a = cursor.fetchall()


    	#Basket b
    	cursor.execute("Select DISTINCT item From basket_b;")
    	item_b = cursor.fetchall()


	return render_template('index.html', sql_table = log, table_title=col_names)


if __name__ == '__main__':
	# set debug mode
	app.debug = True
	# your local machine ip
	ip = '127.0.0.1'
	app.run(host=ip)
