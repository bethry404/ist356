PASSWORD = "secret"



for attempt in range(5):
    entered_password = input("Enter Password: ")

    if entered_password == PASSWORD:
        print("Access Granted!")
        break
        
    else: 
        print("Invalid Password.")

    print(f"You have {4 - attempt} attempts left.")
    attempt += 1

    if attempt == 5:
        print("You are locked out.")
       




        