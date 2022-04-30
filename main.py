Txtcontnt1 = input("Enter 1st file txt contnt: ")
Txtcontnt2 = input("Enter 2st file txt contnt: ")

with open ("file1.txt","r+") as txt1:
    txt1.write(Txtcontnt1)
with open ("file2.txt","r+") as txt2:
    txt2.write(Txtcontnt2)
    
with open ("file1.txt","r") as contntA:
    contnt1 = contntA.read()
with open ("file2.txt","r") as contntB:
    contnt2 = contntB.read()

print ("")
print ("text content in file 1 is: ")
print (Txtcontnt1)
print ("")
print ("text content in file 2 is: ")
print (Txtcontnt2)
print ("")
    
input("Press ENTER to swap data in the files...")

with open ("file1.txt","w+") as contntA:
    contntA.write(contnt2)
with open ("file2.txt","w+") as contntB:
    contntB.write(contnt1)
    
print ("File contents swap completed")