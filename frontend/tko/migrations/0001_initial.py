# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autotest.frontend.afe.model_logic


class Migration(migrations.Migration):

    dependencies = [
        ('afe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestView',
            fields=[
                ('test_idx', models.IntegerField(serialize=False, verbose_name=b'test index', primary_key=True)),
                ('job_idx', models.IntegerField(null=True, verbose_name=b'job index', blank=True)),
                ('test_name', models.CharField(max_length=90, blank=True)),
                ('subdir', models.CharField(max_length=180, verbose_name=b'subdirectory', blank=True)),
                ('kernel_idx', models.IntegerField(verbose_name=b'kernel index')),
                ('status_idx', models.IntegerField(verbose_name=b'status index')),
                ('reason', models.CharField(max_length=3072, blank=True)),
                ('machine_idx', models.IntegerField(verbose_name=b'host index')),
                ('test_started_time', models.DateTimeField(null=True, blank=True)),
                ('test_finished_time', models.DateTimeField(null=True, blank=True)),
                ('job_tag', models.CharField(max_length=300, blank=True)),
                ('job_name', models.CharField(max_length=300, blank=True)),
                ('job_owner', models.CharField(max_length=240, verbose_name=b'owner', blank=True)),
                ('job_queued_time', models.DateTimeField(null=True, blank=True)),
                ('job_started_time', models.DateTimeField(null=True, blank=True)),
                ('job_finished_time', models.DateTimeField(null=True, blank=True)),
                ('afe_job_id', models.IntegerField(null=True)),
                ('hostname', models.CharField(max_length=300, blank=True)),
                ('platform', models.CharField(max_length=240, blank=True)),
                ('machine_owner', models.CharField(max_length=240, blank=True)),
                ('kernel_hash', models.CharField(max_length=105, blank=True)),
                ('kernel_base', models.CharField(max_length=90, blank=True)),
                ('kernel', models.CharField(max_length=300, blank=True)),
                ('status', models.CharField(max_length=30, blank=True)),
            ],
            options={
                'db_table': 'tko_test_view_2',
                'managed': False,
            },
            bases=(models.Model, autotest.frontend.afe.model_logic.ModelExtensions),
        ),
        migrations.CreateModel(
            name='EmbeddedGraphingQuery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url_token', models.TextField()),
                ('graph_type', models.CharField(max_length=16)),
                ('params', models.TextField()),
                ('last_updated', models.DateTimeField(editable=False)),
                ('refresh_time', models.DateTimeField(editable=False)),
                ('cached_png', models.TextField(editable=False)),
            ],
            options={
                'db_table': 'tko_embedded_graphing_queries',
            },
            bases=(models.Model, autotest.frontend.afe.model_logic.ModelExtensions),
        ),
        migrations.CreateModel(
            name='IterationAttribute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('iteration', models.IntegerField()),
                ('attribute', models.CharField(max_length=90)),
                ('value', models.CharField(max_length=300, blank=True)),
            ],
            options={
                'db_table': 'tko_iteration_attributes',
            },
            bases=(models.Model, autotest.frontend.afe.model_logic.ModelExtensions),
        ),
        migrations.CreateModel(
            name='IterationResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('iteration', models.IntegerField()),
                ('attribute', models.CharField(max_length=90)),
                ('value', models.FloatField(null=True, blank=True)),
            ],
            options={
                'db_table': 'tko_iteration_result',
            },
            bases=(models.Model, autotest.frontend.afe.model_logic.ModelExtensions),
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('job_idx', models.AutoField(serialize=False, primary_key=True)),
                ('tag', models.CharField(unique=True, max_length=100)),
                ('label', models.CharField(max_length=300)),
                ('username', models.CharField(max_length=240)),
                ('queued_time', models.DateTimeField(null=True, blank=True)),
                ('started_time', models.DateTimeField(null=True, blank=True)),
                ('finished_time', models.DateTimeField(null=True, blank=True)),
                ('afe_job_id', models.IntegerField(default=None, null=True)),
            ],
            options={
                'db_table': 'tko_jobs',
            },
            bases=(models.Model, autotest.frontend.afe.model_logic.ModelExtensions),
        ),
        migrations.CreateModel(
            name='JobKeyval',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=90)),
                ('value', models.CharField(max_length=300, blank=True)),
                ('job', models.ForeignKey(to='tko.Job')),
            ],
            options={
                'db_table': 'tko_job_keyvals',
            },
        ),
        migrations.CreateModel(
            name='Kernel',
            fields=[
                ('kernel_idx', models.AutoField(serialize=False, primary_key=True)),
                ('kernel_hash', models.CharField(max_length=105, editable=False)),
                ('base', models.CharField(max_length=90)),
                ('printable', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'tko_kernels',
            },
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('machine_idx', models.AutoField(serialize=False, primary_key=True)),
                ('hostname', models.CharField(unique=True, max_length=255)),
                ('machine_group', models.CharField(max_length=240, blank=True)),
                ('owner', models.CharField(max_length=240, blank=True)),
            ],
            options={
                'db_table': 'tko_machines',
            },
        ),
        migrations.CreateModel(
            name='Patch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=240, blank=True)),
                ('url', models.CharField(max_length=900, blank=True)),
                ('the_hash', models.CharField(max_length=105, db_column=b'hash', blank=True)),
                ('kernel', models.ForeignKey(to='tko.Kernel', db_column=b'kernel_idx')),
            ],
            options={
                'db_table': 'tko_patches',
            },
        ),
        migrations.CreateModel(
            name='SavedQuery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('owner', models.CharField(max_length=80)),
                ('name', models.CharField(max_length=100)),
                ('url_token', models.TextField()),
            ],
            options={
                'db_table': 'tko_saved_queries',
            },
            bases=(models.Model, autotest.frontend.afe.model_logic.ModelExtensions),
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('status_idx', models.AutoField(serialize=False, primary_key=True)),
                ('word', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'tko_status',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('test_idx', models.AutoField(serialize=False, primary_key=True)),
                ('test', models.CharField(max_length=300)),
                ('subdir', models.CharField(max_length=300, blank=True)),
                ('reason', models.CharField(max_length=3072, blank=True)),
                ('finished_time', models.DateTimeField(null=True, blank=True)),
                ('started_time', models.DateTimeField(null=True, blank=True)),
                ('job', models.ForeignKey(to='tko.Job', db_column=b'job_idx')),
                ('kernel', models.ForeignKey(to='tko.Kernel', db_column=b'kernel_idx')),
                ('machine', models.ForeignKey(to='tko.Machine', db_column=b'machine_idx')),
                ('status', models.ForeignKey(to='tko.Status', db_column=b'status')),
                ('test_environment', models.ForeignKey(to='afe.TestEnvironment', null=True)),
            ],
            options={
                'db_table': 'tko_tests',
            },
            bases=(models.Model, autotest.frontend.afe.model_logic.ModelExtensions, autotest.frontend.afe.model_logic.ModelWithAttributes),
        ),
        migrations.CreateModel(
            name='TestAttribute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attribute', models.CharField(max_length=90)),
                ('value', models.CharField(max_length=1024, blank=True)),
                ('user_created', models.BooleanField(default=False)),
                ('test', models.ForeignKey(to='tko.Test', db_column=b'test_idx')),
            ],
            options={
                'db_table': 'tko_test_attributes',
            },
            bases=(models.Model, autotest.frontend.afe.model_logic.ModelExtensions),
        ),
        migrations.CreateModel(
            name='TestLabel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=80)),
                ('description', models.TextField(blank=True)),
                ('tests', models.ManyToManyField(to='tko.Test', db_table=b'tko_test_labels_tests', blank=True)),
            ],
            options={
                'db_table': 'tko_test_labels',
            },
            bases=(models.Model, autotest.frontend.afe.model_logic.ModelExtensions),
        ),
        migrations.AddField(
            model_name='job',
            name='machine',
            field=models.ForeignKey(to='tko.Machine', db_column=b'machine_idx'),
        ),
        migrations.AddField(
            model_name='iterationresult',
            name='test',
            field=models.OneToOneField(db_column=b'test_idx', to='tko.Test'),
        ),
        migrations.AddField(
            model_name='iterationattribute',
            name='test',
            field=models.OneToOneField(db_column=b'test_idx', to='tko.Test'),
        ),
    ]
