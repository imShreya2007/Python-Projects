import textwrap
print("Bio Generator For Your Social Accounts....")

name= input("Enter Your Name: ").strip().title()   
profession= input("Enter Your Profession: ").title().strip()
passion= input("Enter one-liner Passion: ").title().strip()
emoji = input("What's Your Favourite Emoji: ").strip()
website = input("Enter Your Website or Handle: ").strip()

print("Choose Your style: \n\t1.Simple Line\n\t2.Emoji Sandwhich\n\t3.Vertial Flair: ")
try:
    style = int(input("Enter 1, 2, or 3 to mention your style-type:"))
except ValueError:
    print("Invalid input! Defaulting to Style 1.")
    style = 1

def generate_bio(style):
    if style == 1:
        return f"{emoji} {name} | 💼 {profession} \n💡 {passion} \n🔗 {website}"
    
    elif style == 2:
        return f"{emoji*3}\n{name} | {profession}\n{passion}\n{website}\n{emoji*3}"

    
    elif style == 3:
        return f"{emoji} {name}\n{profession}💼\n{passion}\n{website}🔥"
    
    else:
        print("Invalid style selected. Defaulting to style 1.")
        return generate_bio(1)

bio = generate_bio(style)
print("\n Your Style Bio:\n")
print(textwrap.dedent(bio))

save = input("\nDo You Want To Save This File To Txt file, (Yes/No): ").capitalize()
if save == "Yes":

    filename = f"{name.lower().replace(' ', '_')}_bio.txt"
    with open (filename, "w", encoding = "utf-8") as file:
        file.write(bio)
    print("File Saved...")

