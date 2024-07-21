# Взлом школьного дневника

Скрипты корректировки установленных конкретно для базы данных, которые являются неотъемлемой частью работ формирования (изменения) учительского журнала. 
Учителя формируют его, ставят оценки и т.д., а мы его корректируем по нашему угодию.

### Как установить

Python 3.11.4 должен быть уже установлен.

Файл со всеми скриптами установить в папке с кодом `manage.py` или запускать через `shell` путем "копипасты".

### Скрипты и их запуск 

Сам запуск будем производить путем копирования одних из скриптов в зависимости от цели. 
Необходимы будут только корректировки в наименовании ученика.


Все функции запускать в командной строке `shell`  командой `python manage.py shell`
***
1. Данный скрипт производит исправление в базе данных оценок ученика с 2 и 3 на 5.
``` Python
from datacenter.models import Schoolkid, Mark, Chastisement, Lesson
def fix_marks(schoolkid):
    schoolkid_ivan = Schoolkid.objects.filter(full_name__contains=schoolkid)
    child = schoolkid_ivan[0]
    mark_child = Mark.objects.filter(schoolkid=child, points__in=[2, 3])
    for mark in mark_child:
        mark.points = 5
        mark.save()
```
    Запускается посредством копирования в командную строку `shell` и запускается: 
```
fix_marks("ФИО школьника")
```
***
2. Полное удаление замечаний на ученика.
```Python
from datacenter.models import Schoolkid, Mark, Chastisement, Lesson
def remove_chastisements(schoolkid):
    schoolkid_feofan = Schoolkid.objects.filter(full_name__contains=schoolkid)
    child = schoolkid_feofan[0]
    chastisement_feofan = Chastisement.objects.filter(schoolkid=child)
    chastisement_feofan.delete()
```
    Запускается посредством копирования в командную строку `shell` и запускается: 
```
remove_chastisements("ФИО школьника")
```
***
3. Данный скрипт отмечает похвалу в базе данных ученика.
```Python
import random
from datacenter.models import Schoolkid, Mark, Chastisement, Lesson
def create_commendation(schoolkid, subject):
    schoolkid_ivan = Schoolkid.objects.filter(full_name__contains=schoolkid)
    child = schoolkid_ivan[0]
    lesson_6a = Lesson.objects.filter(year_of_study=6, group_letter="А", subject__title=subject)
    random_commendations = random.choice(COMMENDATIONS)
    Commendation.objects.create(text=random_commendations, created=lesson_6a[0].date,
                                schoolkid=child, subject=lesson_6a[0].subject,
                                teacher=lesson_6a[0].teacher)
```
    Запускается посредством копирования в командную строку `shell` и запускается: 
```
create_commendation("ФИО школьника", "Предмет")
```
***
4. Проверка на правильность написания ФИО ученика. В случае, если будет ошибка на других скриптах, то данный скрипт пояснит в чем она заключается.
```Python
def checks_pupil(schoolkid):
    try:
        schoolkid_check = Schoolkid.objects.get(full_name__contains=schoolkid)
        return schoolkid_check
    except MultipleObjectsReturned:
        print("Найдено несколько учеников с таким же именем")
    except ObjectDoesNotExist:
        print("Ученик с таким именем не найден")
```
    Запускается посредством копирования в командную строку `shell` и запускается: 
```
checks_pupil("ФИО школьника")
```
***
### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).