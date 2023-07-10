import auth
import products
print("product dashboard")
action=input("Enter 1 for register\nEnter 2 for login\nEnter ur choic: ")
match action:
    case "1":
        print("creat new user")
        user_name=input("user_name : ")
        email=input("Email : ")
        password=input("password : ")
        # do register
        auth.register(user_name,email,password)
    case "2":
        print("crheck user exist or not")
        # do login
        email=input("Email : ")
        password=input("password : ")
        if auth.login(email,password):
            print("hello user")
            products.dashboard()
        else:
            print("wrong password or email")
    case _:
        print("invalid choic")