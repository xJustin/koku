# Generated by Django 2.2.14 on 2020-07-27 23:02
import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [("reporting", "0122_auto_20200803_2307")]

    operations = [
        migrations.DeleteModel(name="OCPStorageVolumeClaimLabelSummary"),
        migrations.AddIndex(
            model_name="awscostentrylineitemdaily", index=models.Index(fields=["resource_id"], name="resource_id_idx")
        ),
    ]