# Generated by Django 5.0.6 on 2024-06-11 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_created_at_user_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Landlord'), (2, 'Tenant')], null=True),
        ),
    ]