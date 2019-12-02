from mysql.connector import MySQLConnection

con = MySQLConnection(host='localhost',database='mysql_study',user='root',password='rootroot')

print(con)