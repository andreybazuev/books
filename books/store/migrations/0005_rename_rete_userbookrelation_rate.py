# Generated by Django 4.0.1 on 2022-02-04 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_book_name_userbookrelation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userbookrelation',
            old_name='rete',
            new_name='rate',
        ),
    ]
