# Django

### MVC
```
Model-View-Controller       (MVC)
  |     |         |
  |     +-----+   |
  |           |   |
  |    +------|---+
  |    |      |
Model-View-Template         (MVT - Django)
```

### Создание и запуск проекта Django
- создание
```shell
django-admin start project name   # создание проекта Django с именем name
django-admin start project name . # создание проекта Django с именем name в текущей папке
```
- запуск
```shell
python manage.py runserver        # запуск сервера отладки (по умолчанию на порту 8000)
python manage.py runserver 9000   # запуск сервера отладки на порту 9000
```
