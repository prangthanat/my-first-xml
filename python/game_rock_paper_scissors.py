import random

Rock = "a"
Scissors = "s"
Paper = "d"
actions = ["a","s","d"]

def rock_paper_scissors():
    while True:
        user_action = input("Please select: Rock[a]| Scissors[s]| Paper[d]| Quit[q]: ")
        computer_action = random.choice(actions)
        print(f"User choose : {user_action}\nComputer choose : {computer_action}")
        if user_action == computer_action:
            print("--- tie ---")
        elif user_action == "a":
            if computer_action == "s":
                print("--- you win! :D ---")
            else:
                print("--- you lose :( ---")
        elif user_action == "s":
            if computer_action == "d":
                print("--- you win! :D ---")
            else:
                print("--- you lose :( ---")
        elif user_action == "d":
            if computer_action == "a":
                print("--- you win! :D ---")
            else:
                print("--- you lose :( ---")
        elif user_action == "q":
            print("Thank you for playing, Good bye :D")
            break
