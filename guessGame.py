import random
def NumberGuessingGame():
    """Setting up the number guessing game"""
    
    # generating random number between 1 - 100
    number_to_guess = random.randint(1, 100)

    # Reseting the attempts to zero every time the loop starts after a break.
    attempts = 0

    # Welcoming message to the user.
    print("I think of a number. \nCan you guess it?")
    
    # This loop continues running for as long as the user fails to guess right.
    while True:
        try:          
            # Here the user is prompt to enter a number.
            guess = int(input("\nEnter the number to guess: "))

            # As the users continues to try until the right guess, this counts the times.
            attempts += 1

            """
            Here the number to be entered by the user is evaluated, when greater, less or equal
            to the secret number them a corresponding message will be displayed to the user.
            """
            if guess > number_to_guess:
                print("Too high! try again.")
            elif guess < number_to_guess:
                print("Too low! try again.")
            else:
                print(f"Correct! You guessed it right in {attempts} attempts.")
                break

        # Error of entering letters will not stop the program
        except ValueError:
            print("Error! please enter a number.")

        # Incase of any other error that comes up, the information about the error will be displayed 
        # As the program continues running.
        except Exception as e:
            print(f"Error occurred: {e}")

NumberGuessingGame()