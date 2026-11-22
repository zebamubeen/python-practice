firstname = "Zeba"
lastname = "Mubeen"
age = 21
programme = "B.TECH"
dept = "CSE"
university = "SBR"
hobby = "cooking,coding,reading,travelling,exploring"
print(firstname)
print(lastname)
print(age)
print(programme)
print(dept)
print(university)
print(hobby)
# ---new code here---
for i in range(20,30):
    print(i)
# ---new code here---
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
# ---new code here---
def say_assalamualaikum():
    print("assalamualaikum Zeba!")
say_assalamualaikum()
say_assalamualaikum()
# ---new code here---
hobbies = ["cooking", "coding", "reading", "travelling", "exploring"]
print(hobbies)    
for hobby in hobbies:
    print("I like ",hobby)