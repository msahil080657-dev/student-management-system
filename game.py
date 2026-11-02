import random

secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("1 se 100 ke darmiyan number guess karo: "))
    attempts += 1

    if guess < secret_number:
        print("Too Low! Dobara try karo.")

    elif guess > secret_number:
        print("Too High! Dobara try karo.")
    else:
        print("🎉 You Win!")
        print(f"Aap ne {attempts} attempts mein number guess kar liya.")
        break