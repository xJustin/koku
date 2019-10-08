# Generated by Django 2.2.4 on 2019-09-26 18:16

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0070_auto_20191002_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='ocpawscostlineitemprojectdailysummary',
            name='data_source',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='ocpusagelineitemdailysummary',
            name='data_source',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='ocpusagelineitemdailysummary',
            name='infra_cost',
            field=models.DecimalField(decimal_places=6, max_digits=24, null=True),
        ),
        migrations.AddField(
            model_name='ocpusagelineitemdailysummary',
            name='markup_cost',
            field=models.DecimalField(decimal_places=6, max_digits=24, null=True),
        ),
        migrations.AddField(
            model_name='ocpusagelineitemdailysummary',
            name='persistentvolume',
            field=models.CharField(max_length=253, null=True),
        ),
        migrations.AddField(
            model_name='ocpusagelineitemdailysummary',
            name='persistentvolumeclaim',
            field=models.CharField(max_length=253, null=True),
        ),
        migrations.AddField(
            model_name='ocpusagelineitemdailysummary',
            name='persistentvolumeclaim_capacity_gigabyte',
            field=models.DecimalField(decimal_places=6, max_digits=24, null=True),
        ),
        migrations.AddField(
            model_name='ocpusagelineitemdailysummary',
            name='persistentvolumeclaim_capacity_gigabyte_months',
            field=models.DecimalField(decimal_places=6, max_digits=24, null=True),
        ),
        migrations.AddField(
            model_name='ocpusagelineitemdailysummary',
            name='persistentvolumeclaim_charge_gb_month',
            field=models.DecimalField(decimal_places=6, max_digits=24, null=True),
        ),
        migrations.AddField(
            model_name='ocpusagelineitemdailysummary',
            name='persistentvolumeclaim_usage_gigabyte_months',
            field=models.DecimalField(decimal_places=6, max_digits=24, null=True),
        ),
        migrations.AddField(
            model_name='ocpusagelineitemdailysummary',
            name='project_infra_cost',
            field=models.DecimalField(decimal_places=6, max_digits=24, null=True),
        ),
        migrations.AddField(
            model_name='ocpusagelineitemdailysummary',
            name='project_markup_cost',
            field=models.DecimalField(decimal_places=6, max_digits=24, null=True),
        ),
        migrations.AddField(
            model_name='ocpusagelineitemdailysummary',
            name='storageclass',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='ocpusagelineitemdailysummary',
            name='volume_labels',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='ocpusagelineitemdailysummary',
            name='volume_request_storage_gigabyte_months',
            field=models.DecimalField(decimal_places=6, max_digits=24, null=True),
        ),
        migrations.AddIndex(
            model_name='ocpusagelineitemdailysummary',
            index=models.Index(fields=['data_source'], name='summary_data_source_idx'),
        ),
        migrations.RunSQL(
            """
            UPDATE reporting_ocpusagelineitem_daily_summary
                SET data_source='Pod'
            ;
            """
        ),
        migrations.RunSQL(
            """
            INSERT INTO reporting_ocpusagelineitem_daily_summary
                (data_source,
                 persistentvolumeclaim,
                 persistentvolume,
                 storageclass,
                 volume_labels,
                 persistentvolumeclaim_capacity_gigabyte,
                 persistentvolumeclaim_capacity_gigabyte_months,
                 volume_request_storage_gigabyte_months,
                 persistentvolumeclaim_usage_gigabyte_months,
                 persistentvolumeclaim_charge_gb_month
                )
                SELECT 'Storage' as data_source,
                    persistentvolumeclaim,
                    persistentvolume,
                    storageclass,
                    volume_labels,
                    persistentvolumeclaim_capacity_gigabyte,
                    persistentvolumeclaim_capacity_gigabyte_months,
                    volume_request_storage_gigabyte_months,
                    persistentvolumeclaim_usage_gigabyte_months,
                    persistentvolumeclaim_charge_gb_month
                FROM reporting_ocpstoragelineitem_daily_summary
            ;
            """
        ),
        migrations.RunSQL(
            """
            UPDATE reporting_ocpusagelineitem_daily_summary ods
                SET infra_cost = ic.infra_cost,
                    project_infra_cost = ic.project_infra_cost,
                    markup_cost = ic.markup_cost,
                    project_markup_cost = ic.project_markup_cost
                FROM reporting_ocpcosts_summary AS ic
                WHERE ods.usage_start = ic.usage_start
                    AND ods.cluster_id = ic.cluster_id
                    AND ods.cluster_alias = ic.cluster_alias
                    AND ods.namespace = ic.namespace
                    AND ods.pod = ic.pod
                    AND ods.node = ic.node
                    AND ods.pod_labels = ic.pod_labels
            ;
            """
        ),
        migrations.RunSQL(
            """
            UPDATE reporting_ocpusagelineitem_daily_summary ods
                SET infra_cost = ic.infra_cost,
                    project_infra_cost = ic.project_infra_cost,
                    markup_cost = ic.markup_cost,
                    project_markup_cost = ic.project_markup_cost
                FROM reporting_ocpcosts_summary AS ic
                WHERE ods.usage_start = ic.usage_start
                    AND ods.cluster_id = ic.cluster_id
                    AND ods.cluster_alias = ic.cluster_alias
                    AND ods.namespace = ic.namespace
                    AND ods.pod = ic.pod
                    AND ods.node = ic.node
                    AND ods.volume_labels = ic.pod_labels
            ;
            """
        ),
        migrations.DeleteModel(
            name='OCPStorageLineItemDailySummary',
        ),
    ]
