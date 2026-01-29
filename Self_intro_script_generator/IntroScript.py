import datetime
print("Personalized Self Intro Script Generator....")

name = input("What is your name? ").strip().title()
age = int(input("How old are you? ").strip())
city = input("Which city do you live in? ").strip().title()
profession = input("What is your profession or field of study? ").strip().title()
hobby = input("What is one hobby you really enjoy? ").strip().capitalize()

def generate_intro(name, age, city, profession, hobby):
    current_time = datetime.datetime.now().strftime("%d %B %Y, %I:%M %p")
    
    print(f"\nHi! My name is {name}, and I’m {age} years old.")
    print(f"I live in {city}, a place I really enjoy calling home.")
    
    if profession == "Student":
        print("I’m currently a student, and I enjoy learning new things and exploring my interests.")
    else:
        print(f"I’m currently a {profession}, and I like what I do because it keeps me curious.")

    print(f"In my free time, I love {hobby}, which helps me relax and express myself.I’m always excited to learn, grow, and connect with people who share similar interests.It’s really nice to be here!")

    print(f"\nLogged on: {current_time}")
    
generate_intro(name, age, city, profession, hobby)

