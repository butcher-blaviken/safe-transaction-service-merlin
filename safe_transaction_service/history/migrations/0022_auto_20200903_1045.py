# Generated by Django 3.0.9 on 2020-09-03 10:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("history", "0021_moduletransaction_failed"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="multisigconfirmation",
            options={"ordering": ["created"]},
        ),
    ]
