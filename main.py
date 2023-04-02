import random

# print("Guess The Number... or else!")
# print(
#     "Only natural nubers! P.s. If you won at first attempt, you will have only just to fill them with this number. Will be fixed soon.")
# number = random.randint(1, 20)
#
# answer1 = ""
# answer1 = int(input("First Attempt: "))
# if answer1 == number:
#     print("You won. Only cuz you're lucky.")
# else:
#     print("No, It isn't. ")
# if answer1 > number:
#     print("that number is too big.")
# elif answer1 < number:
#     print("it's too small.")
#
# answer2 = ""
# answer2 = int(input("Second chance. "))
# if answer2 == number:
#     print("Yes, it is.")
# else:
#     print("hehe. You're funny.")
# if answer2 > number:
#     print("that number is too big.")
# elif answer2 < number:
#     print("it is too small.")
#
# answer3 = ""
# answer3 = int(input("Last try."))
# if answer3 == number:
#     print("You won. Don't know: are you lucky for answering right at 3rd attempt or you're unlucky")
# else:
#     print("Luck left the chat, {}".format(number))
#     print("anyway, that was good game. ")
#     # IF YOU SAW THAT, YOU SAW A... wait, I made a number random.
# print("do you want again?")

# print("Zero is not included, the rules are same.")
# number = random.randint(1, 20)
# answer1 = ""
# answer1 = int(input("First Attempt: "))
# if answer1 == number:
#     print("You won. Seems that is not fair play.")
# else:
#     print("No, It isn't. ")
# if answer1 > number:
#     print("that number is too big.")
# elif answer1 < number:
#     print("it's too small.")
#
# answer2 = ""
# answer2 = int(input("Again. "))
# if answer2 == number:
#     print("Yes, it is. Good")
# else:
#     print("Last attempt. Get serious.")
# if answer2 > number:
#     print("that number is too big.")
# elif answer2 < number:
#     print("it is too small.")
#
# answer3 = ""
# answer3 = int(input("And your finally number is... "))
# if answer3 == number:
#     print("You won.")
# else:
#     print(f'GG, number was {number}')


def game(rule, attempts):
    number = random.randint(1, 20)
    print(rule)
    while attempts > 0:
        answer = int(input(f'{attempts} attempt left: '))
        if answer > number:
            print("that number is too big.")
        elif answer < number:
            print("it's too small.")
        elif answer == number:
            print("You won. Seems that is not fair play.")
            break
        attempts = attempts - 1
    print("do you want again?")


game("Only natural nubers! P.s. If you won at first attempt, you will have only just to fill them with this number. Will be fixed soon.", 3)