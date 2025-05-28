import time
import random


def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def print_ascii_babaka():
    print(r"""
   /^ ^\
  / 0 0 \ 
  V\ Y /V
   / - \   /
  |    \  /
  || (__V
Это бабака! Она виляет хвостом от счастья и одобряет твой выбор 🐶
""")


def print_ascii_moon():
    print(r"""
        ___---___                    
     .--         --.      
   ./   ()      .-. \.
  /   o    .   (   )  \
 / .            '-'    \ 
| ()    .  O         .  |     
\                       / 
 \    '._.'         )  /
  `--._____.-'-.___.-'
Это ПОДЛИННИК луны (ну и что, что чучут на попку смахивает)! 🌕
""")


def print_ascii_sphynx():
    print(r"""
       |\___/|
     ==) ^Y^ (==
       \  ^  /
        )=*=(
       /     \
      |       |
     /| |   | |\
     \| |._.| |/
      '"'   '"'
Почти как настоящий... Осталось только завести 😺
""")


def ask_question(question, correct_answers, ascii_fun=None):
    slow_print(f"\n🧠 {question}")
    answer = input("👉 Ответ: ").strip().lower()
    if answer in correct_answers:
        slow_print("✅ Верно! 🎉")
        if ascii_fun:
            ascii_fun()
        return True
    else:
        slow_print("❌ Не совсем... но ты всё равно самый лучший 💛")
        time.sleep(1)
        return False


def space_mini_game():
    slow_print("\n👨‍🚀 Космическое испытание! Отгадай код запуска ракеты 🚀")
    secret_number = random.randint(1, 5)
    tries = 3
    while tries > 0:
        try:
            guess = int(input(f"🔢 Введи число от 1 до 5 ({tries} попыток): "))
            if guess == secret_number:
                slow_print("🌟 УРА! Ракета запущена! Ты прошёл испытание бесконечно вечным!")
                return True
            else:
                slow_print("❌ Не то! Попробуй снова")
                tries -= 1
        except ValueError:
            slow_print("😅 Нужно ввести число!")
    slow_print("🚀 Ракета улетела без тебя… но ты всё равно мой герой!")
    return False


def final_letter(score, total):
    slow_print("\n📜 Личное послание от твоей девочки:\n")
    time.sleep(1)
    slow_print(f"Ты прошёл этот путь, набрав {score} из {total} правильных ответов")

    if score == total:
        slow_print("🌟 Ты идеален! Просто GENIUS")
    elif score >= total - 1:
        slow_print("💖 Почти всё угадал! Ты очень внимательный!")
    elif score >= total // 2:
        slow_print("😊 Половину прошёл! Это достойно звания Защитника Жабок и Улиток")
    else:
        slow_print("🥺 Даже если не всё угадал, я тебя всё равно обожаю!")

    time.sleep(1.5)
    slow_print("\n💌 Спасибо тебе за всё, что ты делаешь, за твою доброту, юмор, заботу")
    slow_print("Ты мой подлинник во всей этой вселенной!\n")
    slow_print("С днём рождения, любимый 💛")

    time.sleep(2)
    slow_print("\n🐱 А вот и он — наш будущий лысый друг...")
    print_ascii_sphynx()


def start_quiz():
    slow_print("🎉 Привет, именинник! Сегодня твой день, и тебя ждёт викторина, которую пройдёшь только ты!\n"
               "В поле с ответом ты должен ввести всего одно слово или слово с предлогом\n"
               "Я бесконечно верю в тебя, ты справишься!")
    time.sleep(1)

    questions = [
        {
            "question": "В подлинности какого космического объекта я усомнилась на нашем первом свидании?",
            "answers": ["Луна", "луна", "в луне", "В луне"],
            "ascii": print_ascii_moon
        },
        {
            "question": "Как ты называешь собак?",
            "answers": ["бабаки", "Бабаки", "Бабака", "бабака"],
            "ascii": print_ascii_babaka
        },
        {
            "question": "Дополни имя: Варя... (подсказка: поездка в Мытищи, электричка, дядя с плаката)",
            "answers": ["валя", "Валя"],
        },
        {
            "question": "С чем таким ультра вкусненьким и сладким мы ели пиццку и хачапури?",
            "answers": ["груша", "Груша", "с грушей", "С грушей"],
        },
        {
            "question": "На каком молоке ты однажды приготовил нам кашу? (Введи прилагательное, которое отвечает на вопрос 'Какое?')",
            "answers": ["миндальное", "Миндальное"],
        },
        {
            "question": "С чем ты однажды прыгнул, без чего однозначно нельзя было лететь с такой высоты?",
            "answers": ["прыгнул с парашютом", "прыжок с парашютом", "с парашютом", "С парашютом", "парашют", "Парашют"],
        },
        {
            "question": "С чего Ксюшка просто 'Обожает' падать прямо на ногу?",
            "answers": ["с дерева", "С дерева", "дерево", "Дерево"],
        },
    ]

    score = 0
    for q in questions:
        if ask_question(q["question"], q["answers"], q.get("ascii")):
            score += 1

    if space_mini_game():
        score += 1
    total_questions = len(questions) + 1

    final_letter(score, total_questions)


if __name__ == "__main__":
    start_quiz()
