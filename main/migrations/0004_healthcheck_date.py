# Generated by Django 3.1.2 on 2020-12-10 17:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_healthcheck_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthcheck',
            name='date',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2020, 12, 10, 17, 17, 3, 477818, tzinfo=utc)),
        ),
    ]
