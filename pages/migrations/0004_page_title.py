# Generated by Django 4.2 on 2024-03-21 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_remove_page_content_remove_page_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]