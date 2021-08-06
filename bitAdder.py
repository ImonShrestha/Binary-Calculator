def addBinaryNumber (a,b):
    add=[]
    reverse=[]
    c=[0,0,0,0,0,0,0,0]
    for i in range (7,-1,-1):
        sum =(~((a[i]^b[i]) & c[i]) & ((a[i] ^b[i]) | c[i]))
        c[i-1]= ~(~((c[i] & (a[i] ^ b[i])) | (a[i] & b[i])))
        add.append(sum)
    for i in range (len(add)-1,-1,-1):
        reverse.append(add[i])
    return reverse

def display (a,b,d):
    
    for value in a:
        print (value,end="")

    print("")
    for value in b:
        print (value,end="")
    print("")
    print("+")
    print("---------")
    
    
    for value in d:
        print (value,end="")

    print("")
