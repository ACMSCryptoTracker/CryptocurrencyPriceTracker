import psycopg2

hostname = 'baasu.db.elephantsql.com'
username = 'dbuzkqmi'
password = 'vi24qSFc5TG77k5GPa4aQr3XlnLOBIRf'
database = 'dbuzkqmi'
port='5432'
conn = psycopg2.connect(host=hostname, user=username, password=password, dbname=database,port=port)
curr=conn.cursor()
password ='12345'
email='goyalakshita@gmail.com'
name='Akshita'
curr.execute("insert into public.user (password,email,name) values('{}','{}','{}')".format(password,email,name))
conn.commit()
conn.close()
