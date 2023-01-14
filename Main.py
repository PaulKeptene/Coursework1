from prettytable import PrettyTable as pt
from translate import Translator as tr
from random import randint
import pyjokes as pj

table = pt()
data_source = {
    'Films': ['Бойцовский клуб', 'Начало', 'Криминальное чтиво', 'Престиж', 'Форрест Гамп', 'Семь', 'Молчание ягнят'
        , 'Побег из Шоушенка', 'Остров проклятых', 'Зеленая миля'],
    'Music': ['Rap', 'Rock', 'Pop', 'Jazz', 'Classic', 'EDM', 'Hard Rock', 'RnB', 'Retro', 'Folk'],
    'Games':{'Shooter': ['Call of Duty', 'Battlefield', 'Half-Life', 'Counter-Strike', 'Serious Sam'],
             'RPG': ['The Elder Scrolls', 'Fallout', 'Mass Effect', 'Divinity', 'DARK SOULS'],
             'Sport': ['Fifa 2023', 'NBA 2023', 'NHL 2023', 'Forza Horizon', 'F1'],
             'Survival': ['Subnautica', 'Rust', 'Raft', 'The Forest', 'Dont Starve'],
             'MMORPG':['WoW', 'Black Desert', 'The Elder Scrolls Online', 'Lineage 2', 'Guild Wars 2']}
}


def selector_menu():
    table.add_column('Я - Чат-Бот. Что вы хотите?', ['1 - Посоветуй фильм', '2 - Посоветуй музыку', '3 - Посоветуй игру',
                                             '4 - Расскажи шутку', '5 - Хочу сыграть в игру', '0 - Выход'])
    print(table)
    table.clear()
    selector = input('|   Ваш выбор: ')

    return selector


def film_rec(films):
    if len(films) != 0:
        film = films.pop(randint(0, len(films))-1)
        table.add_column('Рекомендую тебе посмотреть...', [film])
        print(f'{table}')
        table.clear()
    else:
        table.add_column('Что хочу сказать....', ['Прости, но больше мне тебе порекомендовать нечего'])
        print(f'{table}')
        table.clear()


def music_rec(music):
    if len(music) != 0:
        track = music.pop(randint(0, len(music)) - 1)
        table.add_column('Рекомендую тебе послушать...', [track])
        print(f'{table}')
        table.clear()
    else:
        table.add_column('Что хочу сказать....', ['Прости, но больше мне тебе порекомендовать нечего'])
        print(f'{table}')
        table.clear()


def game_rec(games):
    table.add_column('Какой жанр игры вам интересен?',
                     ['1 - Shooter', '2 - RPG', '3 - Sport','4 - Survival', '5 - MMORPG'])
    print(table)
    table.clear()

    select = input('|  Ваш выбор: ')

    match select:
        case '1':
            selected_game = games['Shooter']
        case '2':
            selected_game = games['RPG']
        case '3':
            selected_game = games['Sport']
        case '4':
            selected_game = games['Survival']
        case '5':
            selected_game = games['MMORPG']
        case '_':
            print('Такого значения нет!')

    if len(games) != 0:
        game = selected_game.pop(randint(0, len(selected_game)) - 1)
        table.add_column('Рекомендую тебе поиграть в...', [game])
        print(f'{table}')
        table.clear()
    else:
        table.add_column('Что хочу сказать....', ['Прости, но больше мне тебе порекомендовать нечего'])
        print(f'{table}')
        table.clear()


def getJokes():
    translator = tr(to_lang="ru")
    joke = pj.get_joke()
    translation = translator.translate(joke)
    table.add_column('Вот ваша шутка...', [joke, translation])

    print(f'{table}')
    table.clear()


def gameGuessNum():
    table.add_column('Мы играем в игру....', ['Угадай число!\nЯ загадал от 1 до 10, а твоя задача угадать, что '
                                              'именно я загадал)'])
    print(table)
    table.clear()
    user_num = input('| Выберите число от 1 до 10: ')
    my_num = randint(1, 10)

    if user_num.isdigit():
        if 10 >= int(user_num) >= 1:
            if int(user_num) == my_num:
                print("| Вы угадали! Попробуете еще?")
                select = input('| Да/Нет: ')
            else:
                print("| Не угадали... Попробуете еще?")
                select = input('| Да/Нет: ')
        else:
            select = '_'
    else:
        select = '_'

    match select:
        case 'Да'|'да':
            gameGuessNum()
        case 'Нет'|'нет':
            print('| Выходим из игры...')
        case _:
            print('| Введено не верное значение! Завершаем работу...')


def main():
    while True:
        sel = selector_menu()
        print()

        match sel:
            case '1':
                film_rec(data_source['Films'])
            case '2':
                music_rec(data_source['Music'])
            case '3':
                game_rec(data_source['Games'])
            case '4':
                getJokes()
            case '5':
                gameGuessNum()
            case '0':
                table.add_column('Спасибо, что использовал меня)', ['Выходим из приложения...'])
                print(table)
                table.clear()
                break
            case _:
                table.add_column('Упс, что-то пошло не так...', ['введено неверное значение!'])
                print(table)
                table.clear()


if __name__ == '__main__':
    main()