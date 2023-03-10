import time
print("please insert your card")

time.sleep(5)

password=1234

pin=int(input("enter your atm pin :"))


balance=0
if pin==password:
    while True:
        print("""
            1 == balalnce

            2 == withdraw

            3 == deposit balance
            
            4 == exit
            """
            )
        try:
            option=int(input("please enter your choise : "))
        except:
            print("please enter velid option")
        
        if option==1:
            print(f"your current balance is {balance}")

        if option==2:

            withdraw_amount=int(input("please enter withdraw_amount "))

            balance=balance-withdraw_amount

            print(f"{withdraw_amount} is debited from your account")

            print(f"your updated balance is {balance}")

        if option==3:
            
            deposit_amount=int(input("please enter deposit_amount "))

            balance=balance+deposit_amount

            print(f"{deposit_amount} is credited from your account")

            print(f"your updated balance is {balance}")

        if option==4:
            break

else:
     print("worng pin try again")