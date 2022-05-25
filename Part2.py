def list(x,y,z):
    if(x not in [0,20,40,60,80,100,120]): #range
        print("Out of range")
    if(y not in [0,20,40,60,80,100,120]):
        print("Out of range")
    if(z not in [0,20,40,60,80,100,120]):
        print("Out of range")

def total(x,y,z):           #total
    if(x+y+z !=120):
        print("Total incorrect")

while True:
    try:
        x = int(input("Please enter your credits at pass :"))
        y = int(input("Please enter your credits at defer :"))
        z = int(input("Please enter your credits at fail :"))

        list(x,y,z)       #range
    except ValueError:
        print("Integer required")       #Interger
    def check (x,y,z):
        if (x+y+z != 120):              #total
            print("Totle incorrect")
    check(x,y,z)
    
    if x == 120 and y == 00 and z == 00:
        print("Progress")
    elif x == 100 and y == 20 and z == 00:
        print("Progress (module trailer)")
    elif x == 100 and y == 00 and z == 20:
        print("Progress (module trailer)")
    elif x == 80 and y==40 and z == 00:
        print("Do not Progress – module retriever")
    elif x == 80 and y == 20 and z == 20:
        print("Do not Progress – module retriever")
    elif x == 80 and y == 00 and z == 40:
        print("Do not Progress – module retriever")
    elif x == 60 and y == 60 and z == 00:
        print("Do not Progress – module retriever")
    elif x == 60 and y == 40 and z == 20:
        print("Do not Progress – module retriever")
    elif x == 60 and y == 20 and z == 40:
        print("Do not Progress – module retriever")
    elif x == 60 and y == 00 and z == 60:
        print("Do not Progress – module retriever")
    elif x == 40 and y == 80 and z == 00:
        print("Do not Progress – module retriever")
    elif x == 40 and y == 60 and z == 20:
        print("Do not Progress – module retriever")
    elif x == 40 and y == 40 and z == 40:
        print("Do not Progress – module retriever")
    elif x == 40 and y == 20 and z == 60:
        print("Do not Progress – module retriever")
    elif x == 40 and y == 00 and z == 80:
        print("Exclude")
    elif x == 20 and y == 100 and z == 00:
        print("Do not progress – module retriever")
    elif x == 20 and y == 80 and z == 20:
        print("Do not progress – module retriever")
    elif x == 20 and y == 60 and z == 40:
        print("Do not progress – module retriever")
    elif x == 20 and y == 40 and z == 60:
        print("Do not progress – module retriever")
    elif x == 20 and y == 20 and z == 80:
        print("Exclude")
    elif x == 20 and y == 00 and z == 100:
        print("Exclude")
    elif x == 00 and y == 120 and z == 00:
        print("Do not progress – module retriever")
    elif x == 00 and y == 100 and z == 20:
        print("Do not progress – module retriever")
    elif x == 00 and y == 80 and z == 40:
        print("Do not progress – module retriever")
    elif x == 00 and y == 60 and z == 60:
        print("Do not progress – module retriever")
    elif x == 00 and y == 40 and z == 80:
        print("Exclude")
    elif x == 00 and y == 20 and z == 100:
        print("Exclude")
    elif x == 00 and y == 00 and z == 120:
        print("Exclude")
    else:
        print("Invalid number")
