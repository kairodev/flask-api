import sqlite3
import pandas as pd
import os
import json

# Criação do banco de dados ficticio.
def createData():

    try:

        if os.path.exists("data") == True:

            return True

        else:

            connection = sqlite3.connect('data') 

            cursor = connection.cursor()

            cursor.execute('''CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, user_name text NOT NULL, user_password text NOT NULL)''')
            
            cursor.execute('''INSERT INTO users (user_name, user_password) VALUES ('Kairo','1234'), ('John','1234'), ('João','1234'), ('Carlos','1234')''')
            
            connection.commit()

            return True

    except:

        return False

    

# Visualização dos dados 
def viewData():

    try:

        connection = sqlite3.connect('data') 

        cursor = connection.cursor()  
        
        cursor.execute('''SELECT id,user_name,user_password FROM users''')
        
        dados = cursor.fetchall()

        return json.dumps({"message": "OK", "users": dados})

    except:

        return json.dumps({"message": "Error"})

# Visualização dos dados de um usuário especifico
def viewDataSpecific(id):
    
    try:

        connection = sqlite3.connect('data') 

        cursor = connection.cursor()  
        
        cursor.execute(f'''SELECT id,user_name,user_password FROM users WHERE id = {id}''')
        
        dados = cursor.fetchone()

        return json.dumps({"message": "OK", "details": dados})

    except:

        return json.dumps({"message": "Error"})

# Resetar banco de dados
def resetDatabase():

    try:

        if os.path.exists("data") == True:
            os.remove('data')
            if createData():
                return json.dumps({"message": "Success"})
        else:
            if createData():
                return json.dumps({"message": "Success"})


    except:

        return json.dumps({"message": "Error"})

# Deletar usuário
def deleteUser(id):

    try:

        connection = sqlite3.connect('data') 

        cursor = connection.cursor()  
        
        cursor.execute(f'''DELETE FROM users WHERE id = {id}''')
        
        connection.commit()

        return json.dumps({"message": "OK"})

    except:

        return json.dumps({"message": "Error"})

# Alterar usuário
def changeUser(id, username, password):

    try:

        connection = sqlite3.connect('data') 

        cursor = connection.cursor()  
        
        cursor.execute(f'''UPDATE users SET user_name = '{username}', user_password = '{password}' WHERE id = {id}''')
        
        connection.commit()

        return json.dumps({"message": "OK"})

    except Exception as e:
        print(e)

        return json.dumps({"message": "Error"})

