'Daily scheduling program'

from classes import Timetable


def main():
    '''
    main function of programme
    :return:
    '''
    Timetable.set_lst_cab('cabinets.txt')
    with open('groups.txt', 'r') as f:
        for i in f:
            group = Timetable(list(map(str, i.split())))
            group.set_group()

    print('Если хотите узнать расписание кабинета на сегодняшний день, введите 1')
    print('Если хотите узнать расписание группы на сегодняшний день, введите 2')
    answers = ['1', '2']
    answer = str(input())
    while answer not in answers:
        print('Введите верный ответ')
        answer = str(input())

    if answer == '1':
        print('Введите номер кабинета')
        print(Timetable.get_for_cabinet(str(input())))

    else:
        print('Введите номер группы')
        print(Timetable.get_for_groups(str(input())))

main()