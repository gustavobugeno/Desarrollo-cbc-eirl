from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser(
        username="admin",
        email="admin@example.com",
        password="Admin123!"
    )
    print(">>> Superusuario creado automáticamente")
else:
    print(">>> Superusuario ya existe")
