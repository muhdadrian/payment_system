product = 27.50
balance = 0

print("\nGood Day!\n")

name = input("Your name please: ")

print(f"\nHello, {name.title()}!\n")
print(f"You have RM{balance} in your balance.\n")
print(f"The price of the product is RM{product}.\n")

answer = input(f"Do you wish to proceed? Y/N: "
)
if answer == 'y' or answer == 'Y':
    print(f"\nYou need to top up your e-wallet amounted to RM{product:.2f}.\n")
elif answer == 'n' or answer == 'N':
    print(f"\nThank You {name.title()}!\n")
    exit()

answer = input("Do you wish to proceed? Y/N: ")
if answer == 'y' or answer == 'Y':
    topup = input(f"\nPlease top up RM{product:.2f}: ")
    # print(f"Please top up RM{product:.2f}.")
elif answer == 'n' or answer == 'N':
    print(f"\nThank You {name.title()}!")
    exit()

print(f"\nYour balance is RM{topup}!\n")

answer = input(f"Do you wish to buy the product worth RM{product}? Y/N ")
if answer == 'y' or answer == 'Y':
    print("\nIt's paid. The product is yours. Thank you.\n")
    # exit()
elif answer == 'n' or answer == 'N':
    print(f"\nThank you {name.title()}.\n")
    exit()

print(f"Your balance is RM{balance:.2f}.\n")
