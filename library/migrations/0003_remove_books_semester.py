# Generated by Django 2.1.5 on 2019-01-26 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_remove_books_due_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='semester',
        ),
    ]
