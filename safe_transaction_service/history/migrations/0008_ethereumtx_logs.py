# Generated by Django 3.0.2 on 2020-01-27 10:17

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("history", "0007_auto_20200122_1305"),
    ]

    operations = [
        migrations.AddField(
            model_name="ethereumtx",
            name="logs",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=django.contrib.postgres.fields.jsonb.JSONField(),
                default=None,
                null=True,
                size=None,
            ),
        ),
    ]
