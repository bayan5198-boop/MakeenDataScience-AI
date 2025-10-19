#question1 booleane:
correct_username = "admin"
correct_password = "12345"
username = input( "Enter your username: ")
password = input("Enter your password: ")
if username == correct_username and correct_password :
   print("Access granted")
else:
    print("Access denied")
    
#question2:
   
n=float(input("Enter a number: "))
if n %3 ==0 or n %5 == 0:
    print("The number is divisible by 3 or 5")
else:
  print("The number is  not divisible by 3 or 5")
  
  
#question3:
  
number = input("enter digit:")
total= 0
counter = 0
while counter < len(number):
    
    total = total + int(number[counter])
    counter = counter + 1
    
print(total)
  
  
   
   










     
