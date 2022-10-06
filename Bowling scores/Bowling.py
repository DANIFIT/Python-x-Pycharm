#####################################################################################
# Student:    Daniel Elombi.
# Due:        2021-11-14
# Date:       November 6th, 2021
# Purpose:    Bowler's score
# Course:     Intro to Programming
#####################################################################################

# for this program, we'll make a simple program to input six scores for a bowler,
# then display High, low and average bowling score of the user


continue_processing = False
user_check = False


while not continue_processing:

    print('\n')
    game_1_upperbound = 6

    game_input_array = list()

    game_average = 0

    for index in range(game_1_upperbound):
        success = False

        while not success:

            try:
                user_input = float(input("Please enter the Score for Game " + str(index + 1) + ": "))

                if user_input <= 300:

                   game_input_array.append(user_input)

                   success = True

                else:
                     print("Ensure score entered is between 0 and 300, please try again")

            except ValueError:
                print("Unexpected input, the score entered must be numeric, only whole numbers, please try again")

    game_average = sum(game_input_array) / len(game_input_array)

    max_game = max(game_input_array)
    min_game = min(game_input_array)
    print("\n")

    print("=" * 50)
    print(game_input_array)
    print("=" * 50)
    print()
    print("bowling high score is : ", max_game)
    print("bowling lowest score is : ", min_game)
    print("Your average bowling score is : " + "{:.2f}".format(round(game_average, 2)))
    print("=" * 50)

    while not user_check:
        user_input = input("Would you like to enter another data? Y for Yes or N for No: ")
        #Exit interface; Yes or no question given to user
        try:
            user_input = int(user_input)
        except ValueError:

# Giving the user proceed option with Y or y, N or n to end program
            if user_input == "Y" or user_input == "y":
                user_continue = True
                user_check = True
                #If input is Y or y run the program again for new data entry
            elif user_input == "N" or user_input == "n":
                user_continue = False
                user_check = False
                print("\nThanks for using my program ")
                exit()
