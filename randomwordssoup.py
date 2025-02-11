import requests
from bs4 import BeautifulSoup
from googletrans import Translator

translator = Translator()

def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        english_word = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        return {
            "english_word": english_word,
            "word_definition": word_definition
        }
    except Exception as e:
        print("Произошла ошибка:", e)
        return None

def word_game():
    print("Добро пожаловать в игру")
    while True:
        word_dict = get_english_words()
        if word_dict is None:
            continue

        word = word_dict.get("english_word")
        word_definition = word_dict.get("word_definition")
        translated_definition = translator.translate(word_definition, dest="ru").text
        print(f"Значение слова - {translated_definition}")

        user = input("Что это за слово? ")
        if user.lower() == word.lower():
            print("Все верно!")
        else:
            translated_word = translator.translate(word, dest="ru").text
            print(f"Ответ неверный, было загадано это слово - {translated_word} ({word})")
            translated_definition = translator.translate(word_definition, dest="ru").text
            print(f"Значение слова: {translated_definition}")

        play_again = input("Хотите сыграть еще раз? (y/n) ")
        if play_again.lower() != "y":
            print("Спасибо за игру!")
            break

word_game()