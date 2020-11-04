#models/userdb.py
import os, psycopg2

class Userdb():
  def __init__(self):
    self.createTable()

  def setConection(self):
    if 'DYNO' in os.environ:
      DATABASE_URL = os.environ['DATABASE_URL']
      self.conn = psycopg2.connect(DATABASE_URL, sslmode='require')
      self.cursor = self.conn.cursor()
    else: 
      self.conn = psycopg2.connect(
        database="postgres", 
        user="postgres", 
        password="sokhavuth", 
        host="localhost", 
        port="5432"
      )

      self.cursor = self.conn.cursor()
  
  def createTable(self):
    self.setConection()
    
    SQL = '''CREATE TABLE IF NOT EXISTS TYPERS(
      ID SERIAL PRIMARY KEY,
      USERNAME TEXT,
      PASSWORD VARCHAR(320),
      EMAIL VARCHAR(320),
      GRADE INT,
      GRADUATED BOOLEAN NOT NULL
    )'''

    self.cursor.execute(SQL)
  
    self.conn.close()

  def insert(self, *user):
    self.setConection()

    self.cursor.execute("INSERT INTO TYPERS (USERNAME, PASSWORD, EMAIL, GRADE, GRADUATED) VALUES %s ", (user,))
  
    self.conn.commit()
    self.conn.close()

  def checkUser(self, *user):
    self.setConection()

    SQL = "SELECT USERNAME, PASSWORD, GRADE FROM TYPERS WHERE USERNAME = %s AND PASSWORD = %s AND EMAIL = %s LIMIT 1"
    self.cursor.execute(SQL, user)
    result = self.cursor.fetchone()
    
    self.conn.close()

    return result

  def checkUsername(self, username):
    self.setConection()

    SQL = "SELECT USERNAME, PASSWORD, GRADE FROM TYPERS WHERE USERNAME = %s LIMIT 1"
    self.cursor.execute(SQL, (username,))
    result = self.cursor.fetchone()
    
    self.conn.close()

    return result
