import sqlite3
import hashlib
import os

# Dictionary mapping users to ports
usuarios_puertos = {
    'Pedro': 8001,
    'Rafael':8002,
    'Alex':  8003,
    'Juan':  8004,
}


# Array of users and passwords
usuarios = {
    'Pedro': 'AAA1',
    'Rafael': 'BBB2',
    'Alex': 'CCC3',
    'Juan': 'DDD4',
}

# Function to verify the associated port for a given user
def verificar_puerto(usuario):
    return usuarios_puertos.get(usuario)

# Function to verify access
def verificar_acceso(usuario, contrasena,puerto_proporcionado):
    
     puerto_asociado = verificar_puerto(usuario)
   
     # Check if the user exists
     if usuario in usuarios:
        # Verify if the provided port matches the one associated with the user
        if puerto_asociado == int(puerto_proporcionado):
               
          print(f"User {usuario} is on port {puerto_asociado}.")
               
           # Verify if the password is correct
          if hashlib.sha256(contrasena.encode()).hexdigest() == hashlib.sha256(usuarios[usuario].encode()).hexdigest():
            print(f"Access granted for {usuario}.")

            # Access data.db
            try:
                conn = sqlite3.connect('data.db')
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM users;')
                result = cursor.fetchall()
                print("Contents of data.db:")
                print(result)
                conn.close()
            except sqlite3.Error:
                print("Could not access data.db.")

          else:
             print("Correct password. Accessing data.db.")
             # Acceder a fake_data.db
             try:
                conn = sqlite3.connect('fake_data.db')
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM users;')
                result = cursor.fetchall()
                print("Contents of data.db:")
                print(result)
                conn.close()
             except sqlite3.Error:
                print("Could not access data.db.")
        else:
            print(f"Error: User {usuario} is not on the provided port {puerto_proporcionado}.")
     else:
        print("User not found. Could not access the database.")
 


# Get the value of the PORT environment variable
puerto_proporcionado = os.environ.get('PORT')

if puerto_proporcionado is None:
 print("Error: You must provide the port using the PORT environment variable.")
else:
    # Request username and password from the user
    usuario_input = input("Ingrese el nombre de usuario: ")
    contrasena_input = input("Ingrese la contraseña: ")

    puerto_proporcionado = os.environ.get('PORT')
    # Verify access
    verificar_acceso(usuario_input, contrasena_input,puerto_proporcionado)

