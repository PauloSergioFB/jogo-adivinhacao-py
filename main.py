from random import randint

import text as t


def choose_difficulty():
    print(t.difficulty_options)

    while True:
        match input(t.choose_difficulty):
            case "1": attempts, secret_number_range, difficulty = 6, (0, 100), "Fácil"
            case "2": attempts, secret_number_range, difficulty = 10, (0, 1_000), "Médio"
            case "3": attempts, secret_number_range, difficulty = 12, (0, 10_000), "Difícil"
            case "4": attempts, secret_number_range, difficulty = 1, (0, 100), "EXTREMO"
            case _:
                print(t.invalid_input)
                continue

        break

    print(t.confirm_difficulty.format(difficulty))
    return attempts, secret_number_range


def request_player_guess(secret_number_range):
    while True:
        player_guess = input(t.request_guess)
        print()
        if not player_guess.isdigit():
            print(t.invalid_guess_not_number)
            continue

        player_guess = int(player_guess)
        if player_guess < secret_number_range[0] or player_guess > secret_number_range[1]:
            print(t.invalid_guess_out_of_range)
            continue

        return player_guess


def play_again(game_result):
    if game_result == "win": print(t.play_again_win)
    else: print(t.play_again_lose)

    while True:
        option = input(t.prompt_play_again).upper()
        print()
        
        match option:
            case "S":
                print(t.player_wants_to_play_again)
                return True
            case "N":
                print(t.player_does_not_want_to_play_again)
                return False
            case _:
                print(t.invalid_input)


def new_game():
    remaining_attempts, secret_number_range = choose_difficulty()

    random_number = randint(secret_number_range[0], secret_number_range[1])
    while True:
        if remaining_attempts <= 0:
            print(t.lose_message.format(random_number))
            break
        
        if remaining_attempts == 0: print(t.last_attempt_warning)
        else: print(t.remaining_attempts.format(remaining_attempts))

        player_guess = request_player_guess(secret_number_range)

        if player_guess > random_number:
            print(t.guess_too_high)
            remaining_attempts -= 1
            continue

        if player_guess < random_number:
            print(t.guess_too_low)
            remaining_attempts -= 1
            continue
        
        if remaining_attempts == 0: print(t.win_last_try)
        else: print(t.win_message)

        break
            

def start():
    print(t.game_title)
    print(t.welcome_message)

    while True:
        game_result = new_game()

        if play_again(game_result):
            continue

        break
        

if __name__ == "__main__":
    start()
