# Generated by Django 2.2.11 on 2020-03-11 20:49
import django.contrib.postgres.fields.jsonb
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [("api", "0014_reload_azure_map")]

    operations = [
        migrations.AddField(
            model_name="sources",
            name="status",
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict, null=True),
        )
    ]