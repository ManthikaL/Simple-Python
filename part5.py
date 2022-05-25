Progress = 0
Trailer = 0
Retriever = 0
Exclude = 0

Count = 0
Pass = 0
Defer = 0
Fail = 0

mark = ([120, 0, 0], [100, 20, 0], [100, 0, 20], [80, 20, 20], [60, 40, 20], [40, 40, 40], [20, 40, 60],[20, 20, 80], [20, 0, 100], [0, 0, 120])

def list (mark):
    for x in range(0, 10):
        if mark[x][0] == 120:
            print("Progress ststuse is Progress")
            global Progress
            Progress = Progress + 1
        elif mark[x][0] <= 40 and mark [x][2] >= 80:
            print("Progress ststuse is Exclude")
            global Exclude
            Exclude = Exclude + 1
        elif mark[x][0] == 100:
            print("Progress ststuse is Progress (module trailer)")
            global Trailer
            Trailer = Trailer + 1
        else:
            print("Progress ststuse is Do not progress – module retriever")
            global Retriever
            Retriever = Retriever + 1

list (mark)
print("--------------------------------------------------------------------------------------------------------")
print("Horizontal Histogram")
print("Progress", end = " ")
print(Progress , ":", end = " ")
print("*" * Progress )
print("Trailer", end = " ")
print(Trailer, ":", end = " ")
print("*" * Trailer)
print("Retriever", end = " ")
print(Retriever, ":", end = " ")
print("*" * Retriever)
print("Exclude", end = " ")
print(Exclude, ":", end = " ")
print("*" * Exclude)
print(Count, "Outcomes in total")
print("--------------------------------------------------------------------------------------------------------")
