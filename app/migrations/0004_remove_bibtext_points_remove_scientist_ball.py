# Generated by Django 4.2.6 on 2024-05-20 09:28

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0003_bibtext_points_alter_bibtext_index"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="bibtext",
            name="points",
        ),
        migrations.RemoveField(
            model_name="scientist",
            name="ball",
        ),
    ]