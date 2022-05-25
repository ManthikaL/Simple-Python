x=0
y=0
z=0

Progress=0
trailer=0
retriever=0
excluded=0
total=0

def list(x,y,z):
    if(x not in [0,20,40,60,80,100,120]):        #range
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

        list(x,y,z)    #range
        
    except ValueError:
        print("Integer required")       #Interger
        
    def check (x,y,z):
        if (x+y+z != 120):              #total
            print("Totle incorrect")
            
    check(x,y,z)

    if x == 120 and y == 00 and z == 00:                                #marks
        print("Progress")
        Progress = Progress + 1
    elif x == 100 and y == 20 and z == 00:
        print("Progress (module trailer)")
        trailer = trailer + 1
    elif x == 100 and y == 00 and z == 20:
        print("Progress (module trailer)")
        trailer = trailer + 1
    elif x == 80 and y==40 and z == 00:
        print("Do not Progress – module retriever")
        retriever = retriever + 1
    elif x == 80 and y == 20 and z == 20:
        print("Do not Progress – module retriever")
        retriever = retriever + 1
    elif x == 80 and y == 00 and z == 40:
        print("Do not Progress – module retriever")
        retriever = retriever + 1
    elif x == 60 and y == 60 and z == 00:
        print("Do not Progress – module retriever")
        retriever = retriever + 1
    elif x == 60 and y == 40 and z == 20:
        print("Do not Progress – module retriever")
        retriever = retriever + 1
    elif x == 60 and y == 20 and z == 40:
        print("Do not Progress – module retriever")
        retriever = retriever + 1
    elif x == 60 and y == 00 and z == 60:
        print("Do not Progress – module retriever")
        retriever = retriever + 1
    elif x == 40 and y == 80 and z == 00:
        print("Do not Progress – module retriever")
        retriever = retriever + 1
    elif x == 40 and y == 60 and z == 20:
        print("Do not Progress – module retriever")
        retriever = retriever + 1
    elif x == 40 and y == 40 and z == 40:
        print("Do not Progress – module retriever")
        retriever = retriever + 1
    elif x == 40 and y == 20 and z == 60:
        print("Do not Progress – module retriever")
        retriever = retriever + 1
    elif x == 40 and y == 00 and z == 80:
        print("Exclude")
        excluded = excluded + 1
    elif x == 20 and y == 100 and z == 00:
        print("Do not progress – module retriever")
        retriever = retriever + 1
    elif x == 20 and y == 80 and z == 20:
        print("Do not progress – module retriever")
        retriever = retriever + 1
    elif x == 20 and y == 60 and z == 40:
        print("Do not progress – module retriever")
        retriever = retriever + 1
    elif x == 20 and y == 40 and z == 60:
        print("Do not progress – module retriever")
        retriever = retriever + 1
    elif x == 20 and y == 20 and z == 80:
        print("Exclude")
        excluded = excluded + 1
    elif x == 20 and y == 00 and z == 100:
        print("Exclude")
        excluded = excluded + 1
    elif x == 00 and y == 120 and z == 00:
        print("Do not progress – module retriever")
        retriever = retriever + 1
    elif x == 00 and y == 100 and z == 20:
        print("Do not progress – module retriever")
        retriever = retriever + 1
    elif x == 00 and y == 80 and z == 40:
        print("Do not progress – module retriever")
        retriever = retriever + 1
    elif x == 00 and y == 60 and z == 60:
        print("Do not progress – module retriever")
        retriever = retriever + 1
    elif x == 00 and y == 40 and z == 80:
        print("Exclude")
        excluded = excluded + 1
    elif x == 00 and y == 20 and z == 100:
        print("Exclude")
        excluded = excluded + 1
    elif x == 00 and y == 00 and z == 120:
        print("Exclude")
        excluded = excluded + 1
    else:
        print("Invalid number")

    option=input("Would you like to enter another set of data?Enter 'y' for yes or 'q' to quit and view results:")    #option
    if option=='y':
        continue
    if option=='q':
        break
   
print("--------------------------------------------------------------------------------------------------------")
print("Horizontal Histogram")
print("Progress", end = " ")
print(Progress , ":", end = " ")
print("*" * Progress )
print("trailer", end = " ")
print(trailer, ":", end = " ")
print("*" * trailer)
print("retriever", end = " ")
print(retriever, ":", end = " ")
print("*" * retriever)
print("excluded", end = " ")
print(excluded, ":", end = " ")
print("*" * excluded)
print(total, "Outcomes in total")
print("--------------------------------------------------------------------------------------------------------")
