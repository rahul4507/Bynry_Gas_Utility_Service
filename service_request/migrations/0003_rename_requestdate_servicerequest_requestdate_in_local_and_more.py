# Generated by Django 5.0.4 on 2024-05-05 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_request', '0002_servicerequest_requestdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicerequest',
            old_name='requestdate',
            new_name='requestdate_in_local',
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='requestdate_in_utc',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]