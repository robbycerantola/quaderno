# Generated by Django 5.1.6 on 2025-02-20 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quaderno', '0003_remove_attivita_operatore_attivita_responsabile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attivita',
            name='tipo',
            field=models.CharField(choices=[('potatura', 'Potatura'), ('concimazione', 'Concimazione'), ('irrigazione', 'Irrigazione'), ('raccolta', 'Raccolta'), ('aratura', 'Aratura'), ('diserbo', 'Diserbo')], max_length=50),
        ),
    ]
