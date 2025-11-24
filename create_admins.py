import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fusion_system.settings')
django.setup()

from django.contrib.auth.models import User

admins = [
    {'username': 'marjon_vera', 'email': 'marjon@fusion.com', 'first_name': 'Marjon', 'last_name': 'Vera'},
    {'username': 'eliza_rosaryo', 'email': 'eliza@fusion.com', 'first_name': 'Eliza', 'last_name': 'Rosaryo'},
    {'username': 'christine_oliverio', 'email': 'christine@fusion.com', 'first_name': 'Christine', 'last_name': 'Oliverio'},
    {'username': 'carl_marco', 'email': 'carl@fusion.com', 'first_name': 'Carl', 'last_name': 'Marco'},
]

for admin_data in admins:
    if not User.objects.filter(username=admin_data['username']).exists():
        user = User.objects.create_user(
            username=admin_data['username'],
            email=admin_data['email'],
            password='admin123',
            first_name=admin_data['first_name'],
            last_name=admin_data['last_name']
        )
        user.is_staff = True
        user.save()
        print(f"Created admin: {admin_data['username']}")
    else:
        print(f"Admin {admin_data['username']} already exists")