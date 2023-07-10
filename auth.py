import file
def validate(name,email,password):
    # 3<name<=8
    # password>=8
    # valid email
    error=""
    if not 3<len(name)<=8:
        error="invalid name"
    if len(password)<8:
        error +="invalid password"
    if not"@" in email:
        error +="invalid email no @"
    elif not ".com" ==email[-4:]:
        error +="invalid domain"
    return error
        
        
def register(name,email,password):
    # validation
    error=validate(name,email,password)
    # store in text file
    if error=="":
        info=name+":"+email+":"+password+"\n"
        file.store(info,"users.text")
        print("rigester sucssufully")
    else:
        print(error)


def login(email,password):
    data=file.fetch("users.text")
    for user in data:
       user=user.replace("\n","")
       user=user.split(":")
       if email==user[1] and password==user[2]:
            return True
    return False
    
       
        