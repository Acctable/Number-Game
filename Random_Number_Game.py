import random


def numer_gen():
    return random.randint(1, 100)


def get_hint(guess, target):
    distance = abs(guess - target)
    if distance == 0:
        return "🔥 Correct!"
    elif distance <= 5:
        return "🔥 Scorching hot!"
    elif distance <= 10:
        return "🔥 Hot!"
    elif distance <= 20:
        return "🌤 Warm"
    elif distance <= 40:
        return "❄️ Cold"
    else:
        return "🧊 Freezing!"


def player_choice(num, chances, score):
    while chances > 0:
        try:
            guess = int(input(f"\nWhat number am I guessing? (1 to 100) "))

            if guess <= 0 or guess >= 101:
                chances -= 1
                print("Must be between 1 and 100")
                print(f"You have {chances} chances left")
                continue

            hint = get_hint(guess, num)
            print(hint)

            if guess == num:
                score += 1000
                chances += 3
                print("Awesome! Correct Choice! ")
                print(f"Score increased by 1000!!!! (Total: {score})")
                print(f"You gained 3 extra chances! (Total: {chances})")
                return True, score, chances  # Signal to generate new number

            chances -= 1
            direction = "less" if guess > num else "more"
            print(f"The number is {direction} than {guess}")
            print(f"You have {chances} chances left")

        except ValueError:
            chances -= 1
            print("Invalid input. Please enter a number between 1-100")
            print(f"You have {chances} chances left")

    print(f"\nGame over! The number was {num}")
    return False, score, chances


def difficulty():
    while True:
        print("\n--Select difficulty--")
        print("1. Easy: 10 Chances")
        print("2. Medium: 5 Chances")
        print("3. Hard: 3 Chances")

        choice = input("Enter Your Number Choice: ")

        if choice == "1":
            print("Game is Set to Easy")
            return 10
        elif choice == "2":
            print("Game is Set to Medium")
            return 5
        elif choice == "3":
            print("Game is Set to Hard")
            return 3
        else:
            print("Invalid Choice. Please select 1, 2, or 3")


def view_score(high_scores):
    if not high_scores:
        print("\nNo high scores yet!")
    else:
        print("\n--- HIGH SCORES ---")
        for i, (name, score) in enumerate(high_scores, 1):
            print(f"{i}. {name}: {score}")


def main():
    high_scores = []
    while True:
        print("\n--- MAIN MENU ---")
        print("1. Start Game")
        print("2. Check High Scores")
        print("3. Change Difficulty")
        print("4. Exit Game")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            chances = difficulty()
            score = 0
            num = numer_gen()

            while True:
                game_won, score, chances = player_choice(num, chances, score)
                if not game_won:
                    break
                num = numer_gen()  # Generate new number after correct guess

            if score > 0:
                name = input("Enter your name for the high score board: ")
                high_scores.append((name, score))
                high_scores.sort(key=lambda x: x[1], reverse=True)
                high_scores = high_scores[:10]  # Keep top 10

        elif choice == "2":
            view_score(high_scores)
        elif choice == "3":
            pass  # Difficulty is set at game start
        elif choice == "4":
            print("Thanks for playing!")
            break
        else:
            print("Invalid selection. Please try again!")


if __name__ == '__main__':
    main()