# Generated by Django 5.0.4 on 2024-05-06 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_request', '0004_remove_servicerequest_requestdate_in_utc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='requestdate_in_local',
            field=models.DateField(blank=True, null=True),
        ),
    ]