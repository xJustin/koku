# Generated by Django 2.2.15 on 2020-09-09 14:00
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [("reporting", "0135_auto_20200902_1808")]

    operations = [
        migrations.AlterField(
            model_name="ocpawscostlineitemdailysummary", name="node", field=models.CharField(max_length=253, null=True)
        ),
        migrations.AlterField(
            model_name="ocpawscostlineitemprojectdailysummary",
            name="node",
            field=models.CharField(max_length=253, null=True),
        ),
        migrations.AlterField(
            model_name="ocpazurecostlineitemdailysummary",
            name="node",
            field=models.CharField(max_length=253, null=True),
        ),
        migrations.AlterField(
            model_name="ocpazurecostlineitemprojectdailysummary",
            name="node",
            field=models.CharField(max_length=253, null=True),
        ),
    ]
