# Generated by Django 3.1.7 on 2021-04-05 10:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("history", "0034_webhook_new_outgoing_transaction"),
    ]

    operations = [
        migrations.AddField(
            model_name="safemastercopy",
            name="deployer",
            field=models.CharField(default="Gnosis", max_length=50),
        ),
    ]
