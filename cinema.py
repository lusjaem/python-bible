films = {
    "Finding Dory" : [3,5],
    "Bourne" : [18,5],
    "Tarzan" : [15,5],
    "Ghost Busters" : [12,5]
}

while True:
    choice = input("What film you like to watch?:").strip().title()

    if choice in films:
        #pass
        age = int(input("How old are you?: ").strip())
        if age >= films[choice][0]:
            print("Enjoy the film!")
        else:
            print("You are too young to see this film.")
    else:
        print("Sorry, we don't have that film in our library.")