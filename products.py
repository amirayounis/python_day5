def dashboard():
    action=input("Enter 1 for add product\nEnter 2 for show all product\nEnter ur choic: ")
    match action:
        case "1":
            # stor new prodct-->(name,price)
            pass
        case "2":
            # list all products
            pass
        case _:
            print("wrong choic")