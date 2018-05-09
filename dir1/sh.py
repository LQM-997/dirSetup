def Prime(n):
    i=0;
    while (i<n):
        i=i+1
        if(n==1):
            return "false"
        if(n==2):
            return "true"
        elif(n%i==0):
            if(i!=1):
                return "false"
        else:
            return "true"
result=Prime(8)
print(result)
