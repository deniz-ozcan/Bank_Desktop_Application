from mysql.connector import connect 
mydb = connect(
host = "127.0.0.1",
user = "root",
password = "casablanca0102.",
auth_plugin='mysql_native_password',
database = "bankdatabase"
)

