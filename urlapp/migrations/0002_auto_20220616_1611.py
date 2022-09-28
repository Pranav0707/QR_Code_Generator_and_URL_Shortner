# Generated by Django 3.1.7 on 2022-06-16 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlshortner',
            name='short_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='urlshortner',
            name='uid_field',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
