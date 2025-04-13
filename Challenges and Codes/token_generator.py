# # import random
# # import time
# #
# # def get_random(length):
# #     alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# #     random.seed(int(time.time() * 1000))  # seeding with current time
# #     s = ""
# #     for i in range(length):
# #         s += random.choice(alphabet)
# #     return s
# #
# # def flag():
# #     with open('/flag.txt', 'r') as picoCTF:
# #         content = picoCTF.read()
# #         print(content)
# #
# #
# # def main():
# #     print("Welcome to the token generation challenge!")
# #     print("Can you guess the token?")
# #     token_length = 20  # the token length
# #     token = get_random(token_length)
# #
# #     try:
# #         n=0
# #         while n < 50:
# #             user_guess = input("\nEnter your guess for the token (or exit):").strip()
# #             n+=1
# #             if user_guess == "exit":
# #                 print("Exiting the program...")
# #                 break
# #
# #             if user_guess == token:
# #                 print("Congratulations! You found the correct token.")
# #                 flag()
# #                 break
# #             else:
# #                 print("Sorry, your token does not match. Try again!")
# #             if n == 50:
# #                 print("\nYou exhausted your attempts, Bye!")
# #     except KeyboardInterrupt:
# #         print("\nKeyboard interrupt detected. Exiting the program...")
# #
# # if __name__ == "__main__":
# #     main()
# import random
# import time
# import sys
#
# alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
#
#
# def get_random(length, seed_value=None):
#     # If a seed is provided, use it; otherwise, seed with current time in milliseconds.
#     if seed_value is None:
#         seed_value = int(time.time() * 1000)
#     random.seed(seed_value)
#     s = ""
#     for i in range(length):
#         s += random.choice(alphabet)
#     return s
#
#
# def flag():
#     with open('/flag.txt', 'r') as picoCTF:
#         content = picoCTF.read()
#         print(content)
#
#
# def generate_tokens_for_range(target_seed, delta, token_length=20):
#     print(f"Generating tokens for seeds in range: {target_seed - delta} to {target_seed + delta}")
#     for seed in range(target_seed - delta, target_seed + delta + 1):
#         token = get_random(token_length, seed)
#         print(f"Seed: {seed} -> Token: {token}")
#
#
# def main():
#     # If the user provides the "--generate-range" argument, run the range generation mode.
#     if len(sys.argv) > 1 and sys.argv[1] == "--generate-range":
#         # Use the current time in milliseconds as the estimated target seed.
#         target_seed = int(time.time() * 1000)
#         delta = 50  # Change this value to adjust the range of seeds.
#         generate_tokens_for_range(target_seed, delta)
#         return
#
#     print("Welcome to the token generation challenge!")
#     print("Can you guess the token?")
#     token_length = 20  # the token length
#     token = get_random(token_length)
#
#     try:
#         n = 0
#         while n < 50:
#             user_guess = input("\nEnter your guess for the token (or exit): ").strip()
#             n += 1
#             if user_guess == "exit":
#                 print("Exiting the program...")
#                 break
#
#             if user_guess == token:
#                 print("Congratulations! You found the correct token.")
#                 flag()
#                 break
#             else:
#                 print("Sorry, your token does not match. Try again!")
#             if n == 50:
#                 print("\nYou exhausted your attempts, Bye!")
#     except KeyboardInterrupt:
#         print("\nKeyboard interrupt detected. Exiting the program...")
#
#
# if __name__ == "__main__":
#     main()
import random

alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
target_seed = 1741453531698
delta = 5000  # ±5 seconds in milliseconds

for seed in range(target_seed - delta, target_seed + delta + 1):
    random.seed(seed)
    token = "".join(random.choice(alphabet) for _ in range(20))
    print(f"Seed: {seed} -> Token: {token}")
