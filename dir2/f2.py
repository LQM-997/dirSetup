def Total(n):
    alpha=0;
    digit=0;
    space=0;
    other=0
    for s in n:
        if(s.isalpha()):
            alpha+=1
        elif(s.isdigit()):
            digit+=1
        elif(s.isspace()):
            space+=1
        else:
            other+=1
    print("alpha:",alpha)
    print("digit:",digit)
    print("space:",space)
    print("other:",other)
Total("thdg4 76s gtdef")
