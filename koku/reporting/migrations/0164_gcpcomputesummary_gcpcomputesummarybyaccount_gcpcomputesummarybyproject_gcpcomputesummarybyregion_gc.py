# Generated by Django 3.1.3 on 2021-01-22 18:39
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [("reporting", "0163_gcp_compute_summary")]

    operations = [
        migrations.CreateModel(
            name="GCPComputeSummary",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("usage_start", models.DateField()),
                ("usage_end", models.DateField()),
                ("instance_type", models.CharField(max_length=50, null=True)),
                ("usage_amount", models.DecimalField(decimal_places=9, max_digits=24, null=True)),
                ("unit", models.CharField(max_length=63, null=True)),
                ("unblended_cost", models.DecimalField(decimal_places=9, max_digits=24, null=True)),
                ("markup_cost", models.DecimalField(decimal_places=9, max_digits=24, null=True)),
                ("currency", models.CharField(max_length=10)),
                ("source_uuid", models.UUIDField(null=True)),
            ],
            options={"db_table": "reporting_gcp_compute_summary", "managed": False},
        ),
        migrations.CreateModel(
            name="GCPComputeSummaryByAccount",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("usage_start", models.DateField()),
                ("usage_end", models.DateField()),
                ("instance_type", models.CharField(max_length=50, null=True)),
                ("usage_amount", models.DecimalField(decimal_places=9, max_digits=24, null=True)),
                ("unit", models.CharField(max_length=63, null=True)),
                ("unblended_cost", models.DecimalField(decimal_places=9, max_digits=24, null=True)),
                ("markup_cost", models.DecimalField(decimal_places=9, max_digits=24, null=True)),
                ("currency", models.CharField(max_length=10)),
                ("source_uuid", models.UUIDField(null=True)),
                ("account_id", models.CharField(max_length=50)),
            ],
            options={"db_table": "reporting_gcp_compute_summary_by_account", "managed": False},
        ),
        migrations.CreateModel(
            name="GCPComputeSummaryByProject",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("usage_start", models.DateField()),
                ("usage_end", models.DateField()),
                ("instance_type", models.CharField(max_length=50, null=True)),
                ("usage_amount", models.DecimalField(decimal_places=9, max_digits=24, null=True)),
                ("unit", models.CharField(max_length=63, null=True)),
                ("unblended_cost", models.DecimalField(decimal_places=9, max_digits=24, null=True)),
                ("markup_cost", models.DecimalField(decimal_places=9, max_digits=24, null=True)),
                ("currency", models.CharField(max_length=10)),
                ("source_uuid", models.UUIDField(null=True)),
                ("project_id", models.CharField(max_length=256, unique=True)),
                ("project_name", models.CharField(max_length=256)),
                ("account_id", models.CharField(max_length=50)),
            ],
            options={"db_table": "reporting_gcp_compute_summary_by_project", "managed": False},
        ),
        migrations.CreateModel(
            name="GCPComputeSummaryByRegion",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("usage_start", models.DateField()),
                ("usage_end", models.DateField()),
                ("instance_type", models.CharField(max_length=50, null=True)),
                ("usage_amount", models.DecimalField(decimal_places=9, max_digits=24, null=True)),
                ("unit", models.CharField(max_length=63, null=True)),
                ("unblended_cost", models.DecimalField(decimal_places=9, max_digits=24, null=True)),
                ("markup_cost", models.DecimalField(decimal_places=9, max_digits=24, null=True)),
                ("currency", models.CharField(max_length=10)),
                ("source_uuid", models.UUIDField(null=True)),
                ("account_id", models.CharField(max_length=50)),
                ("region", models.CharField(max_length=50, null=True)),
            ],
            options={"db_table": "reporting_gcp_compute_summary_by_region", "managed": False},
        ),
        migrations.CreateModel(
            name="GCPComputeSummaryByService",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("usage_start", models.DateField()),
                ("usage_end", models.DateField()),
                ("instance_type", models.CharField(max_length=50, null=True)),
                ("usage_amount", models.DecimalField(decimal_places=9, max_digits=24, null=True)),
                ("unit", models.CharField(max_length=63, null=True)),
                ("unblended_cost", models.DecimalField(decimal_places=9, max_digits=24, null=True)),
                ("markup_cost", models.DecimalField(decimal_places=9, max_digits=24, null=True)),
                ("currency", models.CharField(max_length=10)),
                ("source_uuid", models.UUIDField(null=True)),
                ("service_id", models.CharField(max_length=256, null=True)),
                ("service_alias", models.CharField(blank=True, max_length=256, null=True)),
                ("account_id", models.CharField(max_length=50)),
            ],
            options={"db_table": "reporting_gcp_compute_summary_by_service", "managed": False},
        ),
    ]
