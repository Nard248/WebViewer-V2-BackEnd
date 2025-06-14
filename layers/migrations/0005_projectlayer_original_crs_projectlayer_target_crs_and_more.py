# Generated by Django 5.1.7 on 2025-03-26 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layers', '0004_projectlayer_is_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectlayer',
            name='original_crs',
            field=models.CharField(blank=True, help_text='Original CRS of the uploaded data', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='projectlayer',
            name='target_crs',
            field=models.CharField(default='EPSG:4326', help_text='Target CRS for storing geometries', max_length=100),
        ),
        migrations.AddField(
            model_name='projectlayer',
            name='upload_error',
            field=models.TextField(blank=True, help_text='Error details if upload failed', null=True),
        ),
        migrations.AddField(
            model_name='projectlayer',
            name='upload_file_name',
            field=models.CharField(blank=True, help_text='Original file name of uploaded data', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='projectlayer',
            name='upload_file_type',
            field=models.CharField(blank=True, help_text='Original file type of uploaded data', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='projectlayer',
            name='upload_status',
            field=models.CharField(choices=[('pending', 'Pending'), ('processing', 'Processing'), ('crs_needed', 'CRS Needed'), ('importing', 'Importing'), ('complete', 'Complete'), ('failed', 'Failed')], default='pending', help_text='Current status of file upload/import process', max_length=50),
        ),
    ]
