import psycopg2
from config import config

#conn -> estabelecer a conexao
def conn():
    connection = None
    
    try:
        params = config()
        
        #connecting to database
        connection = psycopg2.connect(**params)
        
        #create a cursor
        cursor = connection.cursor()
        
        return connection, cursor
        
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    
#create -> criar as tabelas
def create():
    connection = None
    
    try:
        connection,cursor = conn()
        
        table1 = """
        CREATE TABLE IF NOT EXISTS study (
        students VARCHAR(255) NOT NULL PRIMARY KEY,
        hours INTEGER NOT NULL,
        grades REAL NOT NULL
        )
        """
         
        cursor.execute(table1)
        
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.commit()
            connection.close()

def insert(student,hours,grades):

    try:
        sql_command = f""" INSERT INTO study(students,hours,grades)
        VALUES('{student}','{hours}','{grades}'); 
        """
        
        connection,cursor = conn()
        
        cursor.execute(sql_command)
    
    
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.commit()
            connection.close()

def remove(student):
    try:
        sql_command = f""" DELETE FROM study WHERE
        students = '{student}';
        """
        
        connection,cursor = conn()
        
        cursor.execute(sql_command)
    
    
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.commit()
            connection.close()

def select(student):
    try:
        sql_command = f""" SELECT * FROM study WHERE
        students = '{student}';
        """
        
        connection,cursor = conn()
        
        cursor.execute(sql_command)
        
        records = cursor.fetchall()
        
        return [row for row in records]
    
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.commit()
            connection.close()

def select_all():
    try:
        sql_command = f""" SELECT * FROM study;
        """
        
        connection,cursor = conn()
        
        cursor.execute(sql_command)
        
        records = cursor.fetchall()
        
        return [row for row in records]
    
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.commit()
            connection.close()
            
def select_stats():
    try:
        sql_command = f""" SELECT hours,grades FROM study;
        """
        
        connection,cursor = conn()
        
        cursor.execute(sql_command)
        
        records = cursor.fetchall()
        
        return [row for row in records]
    
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.commit()
            connection.close()

def update(student,hours,grades):

    try:
        sql_command = f""" UPDATE study
        SET hours = {hours},
        grades = {grades}
        WHERE students = '{student}'
        """
        connection,cursor = conn()
        
        cursor.execute(sql_command)
    
    
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.commit()
            connection.close()

