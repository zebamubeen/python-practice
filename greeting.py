name = input("What's your name? ")
health = input("How is your health these days? (good / okay / not well) ")
education = input("What is your education?")

print(f"Nice to meet you, {name}!")

if health.lower() == "good":
    print("Glad to hear you're in good health!")
elif health.lower() == "okay":
    print("Hope you feel even better soon!")
else:
    print("I'm sorry to hear that. Take care of yourself!")

print(f"{education} is a great achievement. Keep learning!")
