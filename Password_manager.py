from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()                       with open("key.key", "wb") as key_file:               key_file.write(key)
                                                  
master_pwd =input("What is the master password?: ")
key = load_key() + master_pwd.encode()            fer = Fernet(key)

def load_key():                                                       
  file = open("key.key", "rb")                                        
  key = files.read()
    file.close()                                         
  return key

def view_password():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            user, passw = data.split("|")                     print("User:", user,"| Password:", (fer.decrypt (passw.encode()).decode() + "\n"))


def add_password():
    name = input("Account name: ")
    pwd = input("Password: ")
    with open('password.txt', 'a') as f:
        f.write(name + "" +(fer.encrypt (pwd.encod
e()).decode() +"\n"))


while True:
    mode = input("Do you want to add a new password or view an existing one or quit? (add/view/q): ")
    if mode == "q":
       break
    elif mode == "view":
        view()                                        elif mode == "add":
        add()
    else:
        print("Invalid input")