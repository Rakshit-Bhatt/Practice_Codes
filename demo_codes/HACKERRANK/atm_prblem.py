#required to take two inputs from the user and print the balance after successful transaction thereby deducting the amount of 0.50$.
#faciliating the transaction only when the amount is divisible by 5
#faciliating the transaction only when the amount is > stored amount(+ deduction included)

def cashier(amount_withdrawn, amount_stored):
    BANK_CHARGES=0.50

    if amount_withdrawn < (amount_stored + BANK_CHARGES):
        if amount_withdrawn %5==0:
            print("Transaction allowed: ")
            print("LEFT BALANCE IS :", (amount_stored -( amount_withdrawn + BANK_CHARGES)))

        elif amount_withdrawn %5!=0:
            print("Cannot faciliate the transaction. Plese enter the amount in multiples of 5 only: ")
        else:
            pass

#ADD A DECORATOR SO THAT THE FUNCTION CAN ASK AGAIN IN CASE ELIF() CONDITION COMES TRUE

amount_withdrawn, amount_stored=input("Enter the amount to witdraw and the balance: ").split()
amount_withdrawn=int(amount_withdrawn)
amount_stored=float(amount_stored)

cashier(amount_withdrawn,amount_stored)   

