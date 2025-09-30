#!/usr/bin/env python
import os
import django

# Указываем настройки Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_airbnb.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Создаём суперюзера, если его ещё нет
username = "Andrew"
email = "andreygichan@gmail.com"
password = "Andrey17042004333"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"Superuser '{username}' created!")
else:
    print(f"Superuser '{username}' already exists")
