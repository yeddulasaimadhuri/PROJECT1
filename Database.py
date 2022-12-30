import mysql.connector
class Mysql_Connector():
    def __init__(self,host,user,passwd,db):
        self.host=host
        self.user=user
        self.passwd=passwd
        self.db=db
        self.con=mysql.connector.connect(host=self.host,user=self.user,passwd=self.passwd,database=self.db)
    def check_User(self,user):
        self.cur=self.con.cursor()
        self.sql="select * from login where username=%s"
        val=(user,)
        self.cur.execute(self.sql,val)
        data=self.cur.fetchone()
        if data!=None:
            self.cur.close()
            return True
        else:
            self.cur.close()
            return False
    def insert_db(self,username,password):
        self.username=username
        self.password=password
        self.cur=self.con.cursor()
        self.sql="insert into login(username,password) values(%s,%s)"
        val=(self.username,self.password)
        self.cur.execute(self.sql,val)
        self.con.commit()
    def search(self,user1):
        self.cur=self.con.cursor()
        self.sql="select * from login where username=%s"
        val1=(user1,)
        self.cur.execute(self.sql,val1)
        t=self.cur.fetchone()
        if t!=None:
            print(t)
            return True
        else:
            return False