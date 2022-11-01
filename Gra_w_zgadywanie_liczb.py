import random


def enter_the_number():
    """The function gets a number from the user and checks if the given value is a number
    :rtype int
    :return entered number
    """
    correct = False
    while correct == False:
        try:
            entered_num = input("Guess the number: ")
            entered_num = int(entered_num)
            correct = True
        except ValueError:
            print("It's not a number!")
            correct = False
    return entered_num


def game():
    """Main function with game"""
    rand_num = random.randint(1, 100)
    while True:
        entered_num = enter_the_number()
        if entered_num < rand_num:
            print("Too small!")
        elif entered_num > rand_num:
            print("Too big!")
        else:
            print("You win!")
            break


if __name__ == '__main__':
    game()
