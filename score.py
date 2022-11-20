"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    result = get_result(score)
    print(result)

    random_result = random.randint(0, 100)
    print(f"{random_result}")


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
