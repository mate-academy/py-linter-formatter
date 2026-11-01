# languages = ["python", "java", "c++", "javascript", "ruby", "go"]
# languages = [lang for lang in languages if len(lang) >= 4]
# print(languages)
#
from unittest import result


# matrix = [
#     [10, 20],
#     [30, 40],
#     [50, 60]
# ]
# flat_list = [num + 1 for  row in matrix for num in row]
# print(flat_list)

# words = ["apple", "banana", "kiwi", "pear"]
# word_lengths = {word: len(word) for word in words}
# print(word_lengths)

# words = ["apple", "banana", "kiwi", "pear"]
# long_words = {word: len(word) for word in words if len(word) >= 5}
# print(long_words)

# def get_users_data(users: list) -> dict:
#     return {
#         user_id: {"username": username, "email": email, "password": password}
#         for user_id, username, email, password in users
#     }

def powerful_cars(brand_cars: list, minimal_hp: int) -> list:
    return [[car for car in cars if car["hp"] >= minimal_hp] for cars in brand_cars]

