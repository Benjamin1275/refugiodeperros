from django.db import migrations, models

def remove_duplicates(apps, schema_editor):
    CustomUser = apps.get_model('core', 'CustomUser')
    for rut in CustomUser.objects.values_list('rut', flat=True).annotate(count=models.Count('rut')).filter(count__gt=1):
        users = CustomUser.objects.filter(rut=rut)
        users_to_delete = users[1:]
        for user in users_to_delete:
            user.delete()

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(remove_duplicates),
    ]