product = 27.50
balance = 0

users = {
    'John Foo': 50,
    'Jack Neil': 70,
    'Francis Xavier': 37,
}

# print(users)
print('\n')
print('Before payment:')
for name, cash in users.items():
    print(f"{name.title()} has RM{cash} in his e-wallet.")

print(f"\nEach of them buy the product worth RM{product:.2f} for a quantity:")

for name, cash in users.items():
        balance = cash - product
        print(f"{name} has RM{balance:.2f} balance updated in his e-wallet.")
print('\n')



