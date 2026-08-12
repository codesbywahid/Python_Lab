Question = [
    ["Who wrote the play Romeo and Juliet?",
     "A) Charles Dickens",
     "B) William Shakespeare",
     "C) Mark Twain",
     "D) Jane Austen",
     "B"],

    ["What is the chemical symbol for water?",
     "A) O2",
     "B) CO2",
     "C) H2O",
     "D) NaCl",
     "C"],

    ["How many players are there in a football (soccer) team on the field?",
     "A) 9",
     "B) 10",
     "C) 11",
     "D) 12",
     "C"],

    ["Which is the fastest land animal?",
     "A) Lion",
     "B) Cheetah",
     "C) Horse",
     "D) Leopard",
     "B"],

    ["What is the largest desert in the world?",
     "A) Sahara",
     "B) Gobi",
     "C) Antarctic Desert",
     "D) Kalahari",
     "C"]
]

Answers = ["A", "B", "C", "D"]

while True:
    score = 0
    ques = 0

    for question in Question:
        ques += 1
        print("\n====Question", ques, "====")
        print(question[0])
        print(question[1])
        print(question[2])
        print(question[3])
        print(question[4])
        print()

        answer = input("Enter your option : ").upper()

        while answer not in Answers:
            print("Please Enter A, B, C, D")
            print("Answer Again")
            answer = input("Enter your option : ").upper()

        if answer == question[5]:
            print("Correct Answer")
            score += 1
        else:
            print("Incorrect Answer")

    print("Your Score is : ", str(score) + "/5")
    print("Your Percentage is : ", score / 5 * 100, "%")

    choice = input("Do You want to play Again : yes/no ").upper()

    if choice == "YES":
        print("Game starting again")
    elif choice == "NO":
        print("Thank you for playing")
        break
    else:
        print("Invalid choice")
        continue