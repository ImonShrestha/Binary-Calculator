def convertDecimalToBinary(num):
    bit=[]
    actualBinaryNumber=[]
    counter=0

    while (counter!=8):
        remainder=num%2
        bit.append(remainder)
        num=num//2 
        counter+=1

    for i in range (len(bit)-1,-1,-1):
        actualBinaryNumber.append(bit[i])
    return actualBinaryNumber

def listString(listNumber):
    convertedNumber = ""
    for i in range(len(listNumber)):
        convertedNumber = convertedNumber + str(listNumber[i])
    return convertedNumber
