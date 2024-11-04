# TODO Напишите функцию find_common_participants

def find_common_participants(participants_first_group, participants_second_group, razdel=','):
    participants_first_group_r = participants_first_group.split(razdel)
    participants_second_group_r = participants_second_group.split(razdel)
    common = []
    for person in participants_first_group_r:
        if (person in participants_second_group_r):
            common.append(person)
    common.sort()
    return common


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group, '|'))
# TODO Провеьте работу функции с разделителем отличным от запятой
