# Generated by Django 4.2.13 on 2024-06-01 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_detailreview_label_tag_active_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='active',
            field=models.CharField(default=True),
        ),
    ]
