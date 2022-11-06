from random import randint
from graphic_arts.start_game_banner import run_screensaver


def attack(char_name: str, char_class: str) -> str:
    """Тут мы жестко бьем."""
    sample_string: str = ' нанёс урон противнику равный '
    damage: int
    if char_class == 'warrior':
        damage = 5 + randint(3, 5)
        return (f'{char_name} {sample_string} {damage}')
    if char_class == 'mage':
        damage = 5 + randint(5, 10)
        return (f'{char_name} {sample_string}  {damage}')
    if char_class == 'healer':
        damage = 5 + randint(-3, -1)
        return (f'{char_name} {sample_string}  {damage}')
    return (f'{char_name} не нанес урона')


def defence(char_name: str, char_class: str) -> str:
    """Тут мы обороняемся, не без этого."""
    block: int
    if char_class == 'warrior':
        block = 10 + randint(5, 10)
        return (f'{char_name} блокировал {block} урона')
    if char_class == 'mage':
        block = 10 + randint(-2, 2)
        return (f'{char_name} блокировал {block} урона')
    if char_class == 'healer':
        block = 10 + randint(2, 5)
        return (f'{char_name} блокировал {block} урона')
    return (f'{char_name} не блокировал')


def special(char_name: str, char_class: str) -> str:
    """Тут мы достаем свой мэджик из заднего кармана и фигачим."""
    sample_string: str = 'применил специальное умение'
    special: int
    if char_class == 'warrior':
        special = 80 + 25
        return (f'{char_name} {sample_string} «Выносливость {special}»')
    if char_class == 'mage':
        special = 5 + 40
        return (f'{char_name} {sample_string} «Атака {special}»')
    if char_class == 'healer':
        special = 10 + 30
        return (f'{char_name} {sample_string} «Защита {special}»')
    return (f'{char_name} не применил специальное умение')


def start_training(char_name: str, char_class: str) -> str:
    """Запускаем самую казуальную игру."""
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд:')
    print('attack — чтобы атаковать противника;')
    print('defence — чтобы блокировать атаку противника;')
    print('special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    """Выбор перса."""
    approve_choice: str = None
    char_class: str = None
    while approve_choice != 'y':
        print('Введи название персонажа, за которого хочешь играть:')
        char_class = input('Воитель — warrior, Маг — mage, Лекарь — healer: ')
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя.', end=' ')
            print('Сильный, выносливый и отважный.')
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя.', end=' ')
            print('Обладает высоким интеллектом.')
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель.', end=' ')
            print('Черпает силы из природы, веры и духов.')
        part_one = 'Нажми (Y), чтобы подтвердить выбор, или любую другую'
        part_two = ',  кнопкучтобы выбрать другого персонажа '
        approve_choice = input(part_one + part_two).lower()
    return char_class


if __name__ == '__main__':
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))
