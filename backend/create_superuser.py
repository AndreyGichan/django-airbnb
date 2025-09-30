#!/usr/bin/env python
import os
import django

# Указываем настройки Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_airbnb.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Создаём суперюзера, если его ещё нет
name = "Andrew"
email = "andreygichan@gmail.com"
password = "Andrey17042004333"

if not User.objects.filter(email=email).exists():
    User.objects.create_superuser(name=name, email=email, password=password) # type: ignore
    print(f"Superuser '{email}' created!")
else:
    print(f"Superuser '{email}' already exists")
