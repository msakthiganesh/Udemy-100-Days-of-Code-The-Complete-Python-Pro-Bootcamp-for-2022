import random
from art import logo, vs
from game_data import data


def pick_a_b() -> tuple:
    item_a = random.choice(data)
    item_b = random.choice(data)
    if item_a == item_b:
        item_b = random.choice(data)
    return item_a, item_b


def who_wins(item_a, item_b) -> str:
    if item_a["follower_count"] > item_b["follower_count"]:
        return "a"
    else:
        return "b"


def main():
    user_lost = False
    score = 0
    while not user_lost:
        print(logo)
        a_b = pick_a_b()
        item_a = a_b[0]
        item_b = a_b[1]

        print(
            f"Compare A: {item_a['name']}, a {item_a['description']}, from {item_a['country']}."
        )
        print(vs)
        print(
            f"Compare B: {item_b['name']}, a {item_b['description']}, from {item_b['country']}."
        )
        user_choice = input("Who has more followers? Type 'A' or 'B': ")

        if user_choice.lower() != who_wins(item_a, item_b):
            user_lost = True
            print(f"You lost. Your score is {score}")
        else:
            score += 1
            print(f"You're right! Your score is {score}")


if __name__ == "__main__":
    main()
