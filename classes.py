import random as r


class Timetable:
    '''
    class describing the schedule for cabinets
    '''
    cabinets = {}

    def __init__(self, group):
        self.lesson = group[0]
        self.group = group[2]
        self.time = group[1]
        if len(group) == 4:
            self.cabinet = group[3]
        else:
            self.cabinet = None

    def __str__(self):
        return self.lesson

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def set_lst_cab(txt_file):
        with open(txt_file, 'r') as f:
            for i in f:
                Timetable.cabinets[i.replace('\n', '')] = {'1': [], '2': [], '3': [], '4': [],
                                                           '5': [], '6': [], '7': [], '8': []}

    @staticmethod
    def check(str_cab, time, lesson, group):
        if str_cab[len(str_cab) - 1] == 'M':
            if len(Timetable.cabinets[str_cab][str(time)]) == 0:
                Timetable.cabinets[str_cab][str(time)] = [lesson, group]
                return 1

            else:
                return 0

        else:
            if len(Timetable.cabinets[str_cab][str(time)]) == 0:
                Timetable.cabinets[str_cab][str(time)] = [lesson, group]
                return 1

            elif Timetable.cabinets[str_cab][str(time)][0] == lesson:
                Timetable.cabinets[str_cab][str(time)] = Timetable.cabinets[str_cab][str(time)].append(group)

                return 1

            else:
                return 0

    def set_group(self):
        if self.cabinet == None:
            for i in range(len(self.cabinets)):
                cab_new = r.choice(list(self.cabinets.keys()))
                cab_new = str(cab_new)
                if Timetable.check(cab_new, self.time, self.lesson, self.group) == 1:
                    break

        else:
            self.cabinets[str(self.cabinet)][self.time] = [self.lesson, self.group]

    @staticmethod
    def get_for_groups(group):
        group_lessons = {}
        group = group
        try:
            for i in Timetable.cabinets:
                for j in Timetable.cabinets[i]:
                    for g in Timetable.cabinets[i][j]:
                        if g == group:
                            group_lessons[j] = [Timetable.cabinets[i][j][0], i]
            return group_lessons

        except KeyError:
            print('Такой группы нет')

    @staticmethod
    def get_for_cabinet(cabinet):
        try:
            return Timetable.cabinets[cabinet]
        except KeyError:
            print('Такого кабинета нет')