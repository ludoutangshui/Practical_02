def main():
    score = 0

    print("(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit")
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "G":
            score = int(input("Enter your score(muse be [0, 100]): "))
        if choice == "P":
            result = get_result(score)
            print(result)
        if choice == "S":
            print("⭐" * score)
        else:
            print("Invalid input")
        print("(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit")
        choice = input(">>>").upper()

    print("Farewell")


def get_result(score):
    if score < 0:
        result = "Invalid score"
    else:
        if score < 50:
            result = "Bad"
        elif score > 90:
            result = "Excellent"
        elif score > 50:
            result = "Passable"
        else:
            result = "Invalid score"
    return result


main()
