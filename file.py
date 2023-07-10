# write function take string & appendit in file
def store(text,file):
    with open(file,"a") as f:
        f.write(text) 
def fetch(file):
    with open(file,"r") as f:
        return f.readlines()