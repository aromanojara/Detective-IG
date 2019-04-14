import instaloader
import simplejson
import os
import sys
import getpass

# Variables
username = input("Ingrese su nombre de usuario: ")
password = getpass.getpass("Ingrese su contraseña: ")
user2check = input("Ingrese el usuario que quiere checkear: ")

followers_path = 'C:\\Users\Angelo\Desktop\\followers.txt'
faggots_path = 'C:\\Users\Angelo\Desktop\\faggots.txt'
lovers_path = 'C:\\Users\Angelo\Desktop\\lovers.txt'

new_followers_list = []
faggots = []
lovers = []

# Opening followers list
followers_instance = open(followers_path, mode='r+')
old_followers_list = simplejson.load(followers_instance)
followers_instance.close()

# Get instance
L = instaloader.Instaloader()

print("Iniciando sesión como", username)

# Login or load session
L.login(username, password)        # (login)
#L.interactive_login("angeromanojara")      # (ask password on terminal)
#L.load_session_from_file("angeromanojara") # (load session created w/
                               #  `instaloader -l USERNAME`)

# Obtain profile metadata
profile = instaloader.Profile.from_username(L.context,user2check)

# Getting new followers list
for followers in profile.get_followers():
    new_followers_list.append(followers.username)

if not (os.path.isfile(followers_path)):
    create_followers_list = open(followers_path, mode = "w+").close()
    print('El archivo followers.txt no existía, ahora ha sido creado')

if os.stat(followers_path).st_size == 0:
    followers_instance = open(followers_path, mode = 'r+')
    simplejson.dump(new_followers_list, followers_instance)
    followers_instance.close()
    print('El archivo followers.txt estaba vacio, se llenó con los followers actuales')
    print("Se ha cerrado sesión")
    sys.exit(0)

# Finding out who the faggots are
for i in range(len(old_followers_list)):
    check = old_followers_list[i]
    if check not in new_followers_list:
        faggots.append(check)

if len(faggots) > 0:
    print('Los faggots son:')
    print("\n".join(faggots))
else:
    print('No se han encontrado faggots')


# Finding out who the lovers are
for i in range(len(new_followers_list)):
    check = new_followers_list[i]
    if check not in old_followers_list:
        lovers.append(check)

if len(lovers) > 0:
    print('Los lovers son:')
    print("\n".join(lovers))
else:
    print('No se han encontrado faggots')


# Updating new followers list
print('Escribiendo en followers.txt')
followers_instance = open(followers_path, mode='w').close()
followers_instance = open(followers_path, mode='r+')
simplejson.dump(new_followers_list, followers_instance)
followers_instance.close()

# Dumping faggots list
print('Escribiendo en faggots.txt')
faggots_file_instance = open(faggots_path, mode='w').close()
faggots_file_instance = open(faggots_path, mode='r+')
simplejson.dump(faggots, faggots_file_instance)
faggots_file_instance.close()

# Dumping lovers list
print('Escribiendo en lovers.txt')
lovers_file_instance = open(lovers_path, mode='w').close()
lovers_file_instance = open(lovers_path, mode='r+')
simplejson.dump(lovers, lovers_file_instance)
lovers_file_instance.close()

# Clearing lists
print('Limpiando listas')
new_followers_list = []
faggots = []
lovers = []

# Closing session
L.close()
print('Se ha cerrado sesión')