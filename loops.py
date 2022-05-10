# Counting 

total = 0
while total < 50:
    print(total)
    donation = int(input("how much are you donating? "))
    # total = total + donation
    total += donation
print("We reached the target!")

# password loop
password = "hello"

guess = input("password? ")
while guess != password:
    print("incorrect")
    guess = input("password? ")
print("you're in!")
