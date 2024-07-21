import random
from datacenter.models import Schoolkid, Mark, Chastisement, Lesson


COMMENDATIONS = [
    'Молодец',
    'Отлично',
    'Хорошо',
    'Гораздо лучше, чем я ожидал',
    'Ты меня приятно удивил',
    'Великолепно',
    'Прекрасно',
    'Ты меня очень обрадовал',
    'Именно этого я давно ждал от тебя',
    'Сказано здорово – просто и ясно',
    'Ты, как всегда, точен',
    'Очень хороший ответ',
    'Талантливо',
    'Ты сегодня прыгнул выше головы',
    'Я поражен',
    'Уже существенно лучше',
    'Потрясающе',
    'Замечательно',
    'Прекрасное начало',
    'Так держать',
    'Ты на верном пути',
    'Здорово',
    'Это как раз то, что нужно',
    'Я тобой горжусь',
    'С каждым разом у тебя получается всё лучше',
    'Мы с тобой не зря поработали',
    'Я вижу, как ты стараешься',
    'Ты растешь над собой',
    'Ты многое сделал, я это вижу',
    'Теперь у тебя точно все получится'
]


def fix_marks(schoolkid):
    schoolkid_ivan = Schoolkid.objects.filter(full_name__contains=schoolkid)
    child = schoolkid_ivan[0]
    mark_child = Mark.objects.filter(schoolkid=child, points__in=[2, 3])
    for mark in mark_child:
        mark.points = 5
        mark.save()


def remove_chastisements(schoolkid):
    schoolkid_feofan = Schoolkid.objects.filter(full_name__contains=schoolkid)
    child = schoolkid_feofan[0]
    chastisement_feofan = Chastisement.objects.filter(schoolkid=child)
    chastisement_feofan.delete()


def create_commendation(schoolkid, subject):
    schoolkid_ivan = Schoolkid.objects.filter(full_name__contains=schoolkid)
    child = schoolkid_ivan[0]
    lesson_6a = Lesson.objects.filter(year_of_study=6, group_letter="А", subject__title=subject)
    random_commendations = random.choice(COMMENDATIONS)
    Commendation.objects.create(text=random_commendations, created=lesson_6a[0].date,
                                schoolkid=child, subject=lesson_6a[0].subject,
                                teacher=lesson_6a[0].teacher)


def checks_pupil(schoolkid):
    try:
        schoolkid_check = Schoolkid.objects.get(full_name__contains=schoolkid)
        return schoolkid_check
    except MultipleObjectsReturned:
        print("Найдено несколько учеников с таким же именем")
    except ObjectDoesNotExist:
        print("Ученик с таким именем не найден")