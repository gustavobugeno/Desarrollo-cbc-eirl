from django.db import migrations

def create_admin_user(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='Admin123!'
        )

def delete_admin_user(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    User.objects.filter(username='admin').delete()

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_solicitudinformacion_comentarios_cambios'),
        ('auth', 'latest'),
    ]

    operations = [
        migrations.RunPython(create_admin_user, delete_admin_user),
    ]