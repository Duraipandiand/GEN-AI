
'''
key =1234
user_input=int(input("Please enter a key:"))
print("Default key:",key)
print("User entered Key :",user_input)

i=0 
while i <3:
    if key == user_input:
        print("Grant permission to access")
        break
    elif key != user_input and i<3:
        print("Invalid access key,Please Try Agian")
        if i<2:
            user_input=int(input("Please enter key again:"))
     
    i+=1

 '''

atm_pin = 5678
for i in range(3):
    password = int(input("Enter a PIN Number:"))

    if atm_pin == password:
        print("Correct Password,Continue your process")
        break
    elif atm_pin != password and i <3:
        print("Invalid access key,Please try again")
    

