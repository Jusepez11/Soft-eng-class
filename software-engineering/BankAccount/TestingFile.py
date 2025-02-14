import Bank , Savings, Checking

b1 = Savings.SavingAccount("Truist", "Juan", 10, 1, 321654, 789321, 5)
b2 = Checking.CheckingAccount("Chase", "Pedro", 100, 10, 654321, 321789, 10)


print("\n"*3 + "*" * 10 + "Savings" + "*" * 10 + "\n"*3)

print(b1.deposit("j"))
print(b1.deposit(50000))
print(b1.deposit("j"))
print(b1.deposit(50))
print(b1.deposit("j"))
print(b1.withdraw(50))

print("\n"*3 + "*" * 10 + "Checking" + "*" * 10 + "\n"*3)

print(b2.deposit("j"))
print(b2.withdraw("-9050000"))
print(b2.withdraw("j"))
print(b2.withdraw(50))
print(b2.withdraw(-50000))


print("\n"*3 + "*" * 10 + "Savings obj" + "*" * 10 + "\n"*3)

print(b1)


print("\n"*3 + "*" * 10 + "Checking obj" + "*" * 10 + "\n"*3)

print(b2)