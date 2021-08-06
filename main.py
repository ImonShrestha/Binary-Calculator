import inputRange
import decimalToBinary
import bitAdder

firstNumber=[] #To store converted first number
secondNumber=[] #To store converted second number
Sum =[] #To store sum of those two coverted numbers
Input=True
Range=False

while (Input==True):
    try:
        print("")
                     
        #To input the first number
        n1= int(input("Enter the first number: "))                   
        Range=inputRange.numberRange(n1) #Checking the range of the  first number.

        while (Range==True):
            print("")
            n1=int(input(" Can you please enter the first number in Range of 0-255: "))
            print("")
            Range=inputRange.numberRange(n1)
        firstNumber=decimalToBinary.convertDecimalToBinary(n1)
        displayFirstNumberInBinary=decimalToBinary.listString (firstNumber)
                

        #To input the second number
        n2= int(input("Enter the second number: "))
        print("")
        Range=inputRange.numberRange(n2) #Checking the range of second number

        while (Range==True):
            print("")
            n2=int(input(" Can you please enter the second number in Range of 0-255: "))
            print("")
            Range=inputRange.numberRange(n2)
        secondNumber=decimalToBinary.convertDecimalToBinary(n2)
        displaySecondNumberInBinary=decimalToBinary.listString (secondNumber)

        if n1 + n2>255:
            print ("Error ! This program only runs 8-bit Operations.")

        else:
            print("The binary conversion of ",n1,"is", displayFirstNumberInBinary)
            print("")
            print("The binary conversion of ",n2,"is", displaySecondNumberInBinary)
            print ("")
            print ("The sum of binary numbers is :")
            print ("")

            #adding first number and second number
            Sum=bitAdder.addBinaryNumber(firstNumber,secondNumber)
            bitAdder.display(firstNumber,secondNumber,Sum)
                        
                

           
    except:
        print ("Please enter the valid input.")

    print("")    
    print("Do You Want To Continue Again ? Yes/No?")
    print("")
    Continue=input("Answer: ")
    print("")
    if (Continue=='No' or Continue=='no' or Continue=='NO' or Continue=='nO' ):
        print ("****")
        print("Thank You For Using Python ! Have A Great Day ahead.")
        print("******")
        break

     
