bankPass=[]
wifiPass=[]
schoolPass=[]
entertaiment=[]
gamingPass=[]
def passwordGenerator():
    import random

    def text_prompt(msg):
        try:
            return raw_input(msg)
        except NameError:
            return input(msg)


    capLetList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'V', 'X', 'Y', 'Z']
    symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', '<', ';', '=', '>', '?']
    lowerCase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'v', 'x', 'y', 'z']

    numLet = ''
    userInput = 2
    for count in range(int(userInput)):
        numberList = str(numLet) + str(random.randint(0, 9))
    capLet = ''
    userInput = 3
    for count2 in range(int(userInput)):
        capLet = str(capLet) + str(random.choice(capLetList))
    LowLet = ''
    userInput = 1
    for count3 in range(int(userInput)):
        LowLet = str(LowLet) + str(random.choice(lowerCase))
    symLet = ''
    userInput = 4
    for count4 in range(int(userInput)):
        symLet = str(symLet) + str(random.choice(symbols))
    return(''.join([str(x) for x in [numberList, capLet, LowLet, symLet]]))

ui=str(input("Would u like to Login In? (y/n) "))
if (ui=="y"):
    first=input("What is ur First name? ")
    last=input("What is ur Last name? ")
    User=input("What is ur Username? ")
    Pass=input("What is ur Password? ")
        
ui2=input("Would u like us to create a Password for you? (y/n)")
if (ui2=="y"):
    print("Your password is" +passwordGenerator())
   


    print(f'''
        Your First name is {first}
        Your Last name  is {last}
        Your UserName   is {User}
        Your Password   is {passwordGenerator()}
    ''')
elif (ui=="n"):
        print(f'''
            Your First name is {first}
            Your Last name  is {last}
            Your UserName   is {User}
            Your Password   is {Pass}
        ''')
ui=input("Is this Information Correct? (y/n) ")



while  ui !="y":
        if (ui=="n"):
            first=input("What is ur First name? ")
            last=input("What is ur Last name? ")
            User=input("What is ur Username? ")
            Pass=input("What is ur Password(1) or Would u like me to create one(2). 1 or 2? ")

        print(f'''
            Your First name is {first}
            Your Last name  is {last}
            Your UserName   is {User}
            Your Password   is {Pass}
        ''')
        ui=input("Is this Information Correct? (y/n) ")
if (ui=="y"):
        catergory=input("What kind of Password is this? Bank(B), Wifi(W), School(S), Entertaiment(E), Gaming(G)   ")
        if (catergory=="B"):
            bankPass.append(Pass or passwordGenerator())
            print(bankPass)
        elif (catergory=="W"):
            wifiPass.append(Pass or passwordGenerator())
            print(wifiPass)
        elif (catergory=="S"):
            schoolPass.append(Pass or passwordGenerator())
            print(schoolPass)
        elif (catergory=="E"):
            entertaiment.append(Pass or passwordGenerator())
            print(entertaiment)
        elif (catergory=="G"):
            gamingPass.append(Pass or passwordGenerator())
            print(gamingPass) 



