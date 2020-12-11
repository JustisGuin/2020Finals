#iteration 1
total=0                         #accumulative variable 
sandwhichSelected=False         #flag variable
beverageSelected=False
friesSelected=False
kelpShakeSelected=False
print("Welcome to Good Burger")
            #Printing the Menu
print('''
                            Galley Grab
    Krabby Patty        1.25       Krabby Meal      3.50
        w/sea cheese    1.50       Double Krabby M  3.75 
    Double Krabby Patty 2.00       Triple Krabby M  4.00 
        w/sea cheese    2.25       Salty Sea Dog    1.25
    Triple Krabby Patty 3.00       FootLong         2.00
        w/sea cheese    3.25       Sailors Suprise  3.00
                                   Golden Loaf      2.00
                                        w/sauce     2.50

    Coral Bits                 Kelp Shake      2.00
    Small   1.00                        
    Medium  1.25               SeaFoam Soda 
    Large   1.50                  Small       1.00
                                  Medium      1.25
    Kelp Rings  1.50              Large       1.50
        salty sauce .50 





''')
                    #Asking the user what they want to eat using if then eilf statments
while True:
    sandwhich= input ("Please pick a sandwhich, Krabby Patty for 1.25(k), Double(d) for 2.00, or Triple(t) for 3.00 ")
    print(sandwhich)
    if sandwhich == "k":
        total+=1.25
        sandwhichSelected=True
    elif sandwhich=="d":
        total+= 2.00
        sandwhichSelected=True
    elif sandwhich=="t":
        total+=3.00
        #cheese asking the user if they want cheese 
    chesse=input("Would you like to add sea Cheese, y or n")
    if (chesse=="y"):
        total+= .25
        sandwhichSelected=True
    beverage=input ("Would u like a SeaFoam Soda, y or n ")
    if (beverage=="y"): 
        beverageSelected=True
        beverage=input("s fpr 1.oo, m for 1.25, 1 for 1.50, ")
    print("you said", beverage,"drink" ) #print (string,string,string,string)
        #asking the user if they want a s,m,l beverage 
    if beverage== "s":
        total+=1.00
    elif beverage=="m":
        total+=1.25
    elif beverage=="l":
        total+=1.50

    fries=input("Would you like some Coral Bits, y or n " )
    if (fries== "y"):
        friesSelected=True
        fries=input("Would u like a s for a $1 , m for $1.25, or l for $1.50")


    if (fries=="s"):
            total= total+ 1
    elif (fries=="m"):
        total=total+1.25
    elif (fries=="l"):
        total=total+1.50

    kelpShake=input("Would you like a Kelp Shake, y or n ")
    if (kelpShake== "y"):
        kelpShakeSelected=True
        fries=input("Would u like a Regular Skake(r) for 2")

    if (kelpShake=="r"):
        total=total+2   
    #iteration 4
    #if you dont convert input to int() it will be a sequcence or a string 
    ketchup=int(input("How many ketchup packets would you like? "))*.25
    total+=ketchup
    #but you could combine the top two lines into one 

    if(sandwhichSelected and beverageSelected and friesSelected):        #and looks for true statements 
    #if varibale == true and variable == true and varibale == true 
        total-=1

    #Letting the User Add or Remove 
    
    #Need Sub Total
                #Formatting sandwhich drink and fries and packets and tax and subtotal 
    tax=total*.7
    subTotal=total 
    total=tax+subTotal
    print('''           #The Order 
    Your order is: 
    {0} sandwich,
    {1} drink,
    {2} fries,
    {3} packets,
    {4} Tax,
    {5} Subtotal

    For a total of ${6}
    '''.format(sandwhich,beverage,fries,ketchup,tax,subTotal,total))
    print('${:,.2f}'.format(total)) #string formatting      #Final Amount 
    

    
    #print(total) 