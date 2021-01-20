min = int(input())
max = int(input())
i=int(input())
while i!= -999:    
    if min <= i <= max:
        print("Nothing to report")
        i=int(input())
    else:
        print("Alert!")
        break
        