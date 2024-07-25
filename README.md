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
1. Проверка на правильность написания ФИО ученика, а также на возможность повторения.
```Python
from datacenter.models import Schoolkid, Mark, Chastisement, Lesson, Commendation
def checks_pupil(schoolkid_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name, year_of_study=6, group_letter="А")
        return schoolkid
    except Schoolkid.MultipleObjectsReturned:
        print("Найдено несколько учеников с таким же именем")
    except Schoolkid.DoesNotExist:
        print("Ученик с таким именем не найден")
```
    Запускается посредством копирования в командную строку `shell` и запускается: 
```
checks_pupil("ФИО школьника")
```
***
2. Данный скрипт производит исправление в базе данных оценок ученика с 2 и 3 на 5.
``` Python
from datacenter.models import Schoolkid, Mark, Chastisement, Lesson, Commendation
def fix_marks(schoolkid_name):
    schoolkid = checks_pupil(schoolkid_name)
    if schoolkid:
        marks_child = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
        marks_child.update(points=5)
```
    Запускается посредством копирования в командную строку `shell` и запускается: 
```
fix_marks("ФИО школьника")
```
***
3. Полное удаление замечаний на ученика.
```Python
from datacenter.models import Schoolkid, Mark, Chastisement, Lesson, Commendation
def remove_chastisements(schoolkid_name):
    schoolkid = checks_pupil(schoolkid_name)
    if schoolkid:
        chastisement = Chastisement.objects.filter(schoolkid=schoolkid)
        chastisement.delete()
```
    Запускается посредством копирования в командную строку `shell` и запускается: 
```
remove_chastisements("ФИО школьника")
```
***
4. Данный скрипт отмечает похвалу в базе данных ученика.
```Python
import random
from datacenter.models import Schoolkid, Mark, Chastisement, Lesson
def create_commendation(schoolkid_name, subject):
    schoolkid = checks_pupil(schoolkid_name)
    if schoolkid:
        lesson = Lesson.objects.filter(subject__title=subject, year_of_study=schoolkid.year_of_study,
                                       group_letter=schoolkid.group_letter).order_by("subject").first()
        if lesson is None:
            print('Данного урока не найдено')
        else:
            random_commendations = random.choice(COMMENDATIONS)
            Commendation.objects.create(text=random_commendations, created=lesson.date, schoolkid=schoolkid,
                                        subject=lesson.subject, teacher=lesson.teacher)
```
    Запускается посредством копирования в командную строку `shell` и запускается: 
```
create_commendation("ФИО школьника", "Предмет")
```
***
### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).