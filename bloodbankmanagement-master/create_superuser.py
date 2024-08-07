import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bloodbankmanagement.settings')
django.setup()

from django.contrib.auth.models import User

def create_superuser():
    username = 'admin'
    email = 'admin@example.com'
    password = 'yourpassword'
   

    if User.objects.filter(username=username).exists():
        print('Superuser already exists')
    else:
        User.objects.create_superuser(username, email, password)
        print('Superuser created successfully')

if __name__ == "__main__":
    create_superuser()

