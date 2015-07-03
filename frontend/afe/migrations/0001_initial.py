# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autotest.frontend.afe.model_logic
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AclGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('description', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'db_table': 'afe_acl_groups',
            },
            bases=(models.Model, autotest.frontend.afe.model_logic.ModelExtensions),
        ),
        migrations.CreateModel(
            name='AtomicGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('description', models.TextField(blank=True)),
                ('max_number_of_machines', models.IntegerField(default=333333333)),
                ('invalid', models.BooleanField(default=False, editable=False)),
            ],
            options={
                'db_table': 'afe_atomic_groups',
            },
            bases=(autotest.frontend.afe.model_logic.ModelWithInvalid, models.Model),
        ),
        migrations.CreateModel(
            name='Drone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostname', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'db_table': 'afe_drones',
            },
            bases=(models.Model, autotest.frontend.afe.model_logic.ModelExtensions),
        ),
        migrations.CreateModel(
            name='DroneSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('drones', models.ManyToManyField(to='afe.Drone', db_table=b'afe_drone_sets_drones')),
            ],
            options={
                'db_table': 'afe_drone_sets',
            },
            bases=(models.Model, autotest.frontend.afe.model_logic.ModelExtensions),
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostname', models.CharField(unique=True, max_length=255)),
                ('locked', models.BooleanField(default=False)),
                ('synch_id', models.IntegerField(null=True, editable=False, blank=True)),
                ('status', models.CharField(default=b'Ready', max_length=255, editable=False, choices=[(b'Verifying', b'Verifying'), (b'Running', b'Running'), (b'Ready', b'Ready'), (b'Repairing', b'Repairing'), (b'Repair Failed', b'Repair Failed'), (b'Cleaning', b'Cleaning'), (b'Pending', b'Pending')])),
                ('invalid', models.BooleanField(default=False, editable=False)),
                ('protection', models.SmallIntegerField(default=0, blank=True, choices=[(0, b'No protection'), (1, b'Repair software only'), (2, b'Repair filesystem only'), (3, b'Do not repair'), (4, b'Do not verify')])),
                ('lock_time', models.DateTimeField(null=True, editable=False, blank=True)),
                ('dirty', models.BooleanField(default=True, editable=False)),
            ],
            options={
                'db_table': 'afe_hosts',
            },
            bases=(autotest.frontend.afe.model_logic.ModelWithInvalid, models.Model, autotest.frontend.afe.model_logic.ModelWithAttributes),
        ),
        migrations.CreateModel(
            name='HostAttribute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attribute', models.CharField(max_length=90)),
                ('value', models.CharField(max_length=300)),
                ('host', models.ForeignKey(to='afe.Host')),
            ],
            options={
                'db_table': 'afe_host_attributes',
            },
        ),
        migrations.CreateModel(
            name='HostQueueEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('profile', models.CharField(default=b'', max_length=255, blank=True)),
                ('status', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=False)),
                ('complete', models.BooleanField(default=False)),
                ('deleted', models.BooleanField(default=False)),
                ('execution_subdir', models.CharField(default=b'', max_length=255, blank=True)),
                ('aborted', models.BooleanField(default=False)),
                ('started_on', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'afe_host_queue_entries',
            },
            bases=(models.Model, autotest.frontend.afe.model_logic.ModelExtensions),
        ),
        migrations.CreateModel(
            name='IneligibleHostQueue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('host', models.ForeignKey(to='afe.Host')),
            ],
            options={
                'db_table': 'afe_ineligible_host_queues',
            },
            bases=(models.Model, autotest.frontend.afe.model_logic.ModelExtensions),
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('owner', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('priority', models.SmallIntegerField(default=1, blank=True, choices=[(0, b'Low'), (1, b'Medium'), (2, b'High'), (3, b'Urgent')])),
                ('control_file', models.TextField(null=True, blank=True)),
                ('control_type', models.SmallIntegerField(default=2, blank=True, choices=[(1, b'Server'), (2, b'Client')])),
                ('created_on', models.DateTimeField()),
                ('synch_count', models.IntegerField(default=1, null=True)),
                ('timeout', models.IntegerField(default=b'72')),
                ('run_verify', models.BooleanField(default=True)),
                ('email_list', models.CharField(max_length=250, blank=True)),
                ('reboot_before', models.SmallIntegerField(default=1, blank=True, choices=[(0, b'Never'), (1, b'If dirty'), (2, b'Always')])),
                ('reboot_after', models.SmallIntegerField(default=2, blank=True, choices=[(0, b'Never'), (1, b'If all tests passed'), (2, b'Always')])),
                ('parse_failed_repair', models.BooleanField(default=True)),
                ('max_runtime_hrs', models.IntegerField(default=b'72')),
                ('reserve_hosts', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'afe_jobs',
            },
            bases=(models.Model, autotest.frontend.afe.model_logic.ModelExtensions),
        ),
        migrations.CreateModel(
            name='JobKeyval',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=90)),
                ('value', models.CharField(max_length=300)),
                ('job', models.ForeignKey(to='afe.Job')),
            ],
            options={
                'db_table': 'afe_job_keyvals',
            },
            bases=(models.Model, autotest.frontend.afe.model_logic.ModelExtensions),
        ),
        migrations.CreateModel(
            name='Kernel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.CharField(max_length=255)),
                ('cmdline', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'db_table': 'afe_kernels',
            },
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('kernel_config', models.CharField(max_length=255, blank=True)),
                ('platform', models.BooleanField(default=False)),
                ('invalid', models.BooleanField(default=False, editable=False)),
                ('only_if_needed', models.BooleanField(default=False)),
                ('atomic_group', models.ForeignKey(blank=True, to='afe.AtomicGroup', null=True)),
            ],
            options={
                'db_table': 'afe_labels',
            },
            bases=(autotest.frontend.afe.model_logic.ModelWithInvalid, models.Model),
        ),
        migrations.CreateModel(
            name='LinuxDistro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('version', models.CharField(max_length=40)),
                ('release', models.CharField(default=b'', max_length=40)),
                ('arch', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'linux_distro',
            },
            bases=(models.Model, autotest.frontend.afe.model_logic.ModelExtensions),
        ),
        migrations.CreateModel(
            name='MigrateInfo',
            fields=[
                ('version', models.IntegerField(default=None, serialize=False, primary_key=True, blank=True)),
            ],
            options={
                'db_table': 'migrate_info',
            },
            bases=(models.Model, autotest.frontend.afe.model_logic.ModelExtensions),
        ),
        migrations.CreateModel(
            name='ParameterizedJob',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('use_container', models.BooleanField(default=False)),
                ('profile_only', models.BooleanField(default=False)),
                ('upload_kernel_config', models.BooleanField(default=False)),
                ('kernels', models.ManyToManyField(to='afe.Kernel', db_table=b'afe_parameterized_job_kernels')),
                ('label', models.ForeignKey(to='afe.Label', null=True)),
            ],
            options={
                'db_table': 'afe_parameterized_jobs',
            },
        ),
        migrations.CreateModel(
            name='ParameterizedJobParameter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('parameter_value', models.TextField()),
                ('parameter_type', models.CharField(max_length=8, choices=[(b'int', b'int'), (b'float', b'float'), (b'string', b'string')])),
                ('parameterized_job', models.ForeignKey(to='afe.ParameterizedJob')),
            ],
            options={
                'db_table': 'afe_parameterized_job_parameters',
            },
        ),
        migrations.CreateModel(
            name='ParameterizedJobProfiler',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('parameterized_job', models.ForeignKey(to='afe.ParameterizedJob')),
            ],
            options={
                'db_table': 'afe_parameterized_jobs_profilers',
            },
        ),
        migrations.CreateModel(
            name='ParameterizedJobProfilerParameter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('parameter_name', models.CharField(max_length=255)),
                ('parameter_value', models.TextField()),
                ('parameter_type', models.CharField(max_length=8, choices=[(b'int', b'int'), (b'float', b'float'), (b'string', b'string')])),
                ('parameterized_job_profiler', models.ForeignKey(to='afe.ParameterizedJobProfiler')),
            ],
            options={
                'db_table': 'afe_parameterized_job_profiler_parameters',
            },
        ),
        migrations.CreateModel(
            name='Profiler',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'afe_profilers',
            },
            bases=(models.Model, autotest.frontend.afe.model_logic.ModelExtensions),
        ),
        migrations.CreateModel(
            name='RecurringRun',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateTimeField()),
                ('loop_period', models.IntegerField(blank=True)),
                ('loop_count', models.IntegerField(blank=True)),
                ('job', models.ForeignKey(to='afe.Job')),
            ],
            options={
                'db_table': 'afe_recurring_run',
            },
            bases=(models.Model, autotest.frontend.afe.model_logic.ModelExtensions),
        ),
        migrations.CreateModel(
            name='SoftwareComponent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('version', models.CharField(max_length=120)),
                ('release', models.CharField(max_length=120)),
                ('checksum', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'software_component',
            },
            bases=(models.Model, autotest.frontend.afe.model_logic.ModelExtensions),
        ),
        migrations.CreateModel(
            name='SoftwareComponentArch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=20)),
            ],
            options={
                'db_table': 'software_component_arch',
            },
            bases=(models.Model, autotest.frontend.afe.model_logic.ModelExtensions),
        ),
        migrations.CreateModel(
            name='SoftwareComponentKind',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=20)),
            ],
            options={
                'db_table': 'software_component_kind',
            },
            bases=(models.Model, autotest.frontend.afe.model_logic.ModelExtensions),
        ),
        migrations.CreateModel(
            name='SpecialTask',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('task', models.CharField(max_length=64, choices=[(b'Verify', b'Verify'), (b'Cleanup', b'Cleanup'), (b'Repair', b'Repair')])),
                ('time_requested', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=False)),
                ('is_complete', models.BooleanField(default=False)),
                ('time_started', models.DateTimeField(null=True, blank=True)),
                ('success', models.BooleanField(default=False)),
                ('host', models.ForeignKey(to='afe.Host')),
            ],
            options={
                'db_table': 'afe_special_tasks',
            },
            bases=(models.Model, autotest.frontend.afe.model_logic.ModelExtensions),
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('test_class', models.CharField(max_length=255)),
                ('test_category', models.CharField(max_length=255)),
                ('dependencies', models.CharField(max_length=255, blank=True)),
                ('description', models.TextField(blank=True)),
                ('experimental', models.BooleanField(default=True)),
                ('run_verify', models.BooleanField(default=True)),
                ('test_time', models.SmallIntegerField(default=2, choices=[(1, b'SHORT'), (2, b'MEDIUM'), (3, b'LONG')])),
                ('test_type', models.SmallIntegerField(default=1, choices=[(1, b'Client'), (2, b'Server')])),
                ('sync_count', models.PositiveIntegerField(default=1)),
                ('path', models.CharField(unique=True, max_length=255)),
                ('dependency_labels', models.ManyToManyField(to='afe.Label', db_table=b'afe_autotests_dependency_labels', blank=True)),
            ],
            options={
                'db_table': 'afe_autotests',
            },
            bases=(models.Model, autotest.frontend.afe.model_logic.ModelExtensions),
        ),
        migrations.CreateModel(
            name='TestEnvironment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('distro', models.ForeignKey(to='afe.LinuxDistro')),
                ('installed_software_components', models.ManyToManyField(to='afe.SoftwareComponent', db_table=b'test_environment_installed_software_components')),
            ],
            options={
                'db_table': 'test_environment',
            },
            bases=(models.Model, autotest.frontend.afe.model_logic.ModelExtensions),
        ),
        migrations.CreateModel(
            name='TestParameter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('test', models.ForeignKey(to='afe.Test')),
            ],
            options={
                'db_table': 'afe_test_parameters',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('login', models.CharField(unique=True, max_length=255)),
                ('access_level', models.IntegerField(default=0, blank=True)),
                ('reboot_before', models.SmallIntegerField(default=1, blank=True, choices=[(0, b'Never'), (1, b'If dirty'), (2, b'Always')])),
                ('reboot_after', models.SmallIntegerField(default=2, blank=True, choices=[(0, b'Never'), (1, b'If all tests passed'), (2, b'Always')])),
                ('show_experimental', models.BooleanField(default=False)),
                ('drone_set', models.ForeignKey(blank=True, to='afe.DroneSet', null=True)),
            ],
            options={
                'db_table': 'afe_users',
            },
            bases=(models.Model, autotest.frontend.afe.model_logic.ModelExtensions),
        ),
        migrations.CreateModel(
            name='AbortedHostQueueEntry',
            fields=[
                ('queue_entry', models.OneToOneField(primary_key=True, serialize=False, to='afe.HostQueueEntry')),
                ('aborted_on', models.DateTimeField()),
                ('aborted_by', models.ForeignKey(to='afe.User')),
            ],
            options={
                'db_table': 'afe_aborted_host_queue_entries',
            },
            bases=(models.Model, autotest.frontend.afe.model_logic.ModelExtensions),
        ),
        migrations.AddField(
            model_name='specialtask',
            name='queue_entry',
            field=models.ForeignKey(blank=True, to='afe.HostQueueEntry', null=True),
        ),
        migrations.AddField(
            model_name='specialtask',
            name='requested_by',
            field=models.ForeignKey(to='afe.User'),
        ),
        migrations.AddField(
            model_name='softwarecomponent',
            name='arch',
            field=models.ForeignKey(to='afe.SoftwareComponentArch', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='softwarecomponent',
            name='kind',
            field=models.ForeignKey(to='afe.SoftwareComponentKind', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='recurringrun',
            name='owner',
            field=models.ForeignKey(to='afe.User'),
        ),
        migrations.AddField(
            model_name='parameterizedjobprofiler',
            name='profiler',
            field=models.ForeignKey(to='afe.Profiler'),
        ),
        migrations.AddField(
            model_name='parameterizedjobparameter',
            name='test_parameter',
            field=models.ForeignKey(to='afe.TestParameter'),
        ),
        migrations.AddField(
            model_name='parameterizedjob',
            name='profilers',
            field=models.ManyToManyField(to='afe.Profiler', through='afe.ParameterizedJobProfiler'),
        ),
        migrations.AddField(
            model_name='parameterizedjob',
            name='test',
            field=models.ForeignKey(to='afe.Test'),
        ),
        migrations.AddField(
            model_name='linuxdistro',
            name='available_software_components',
            field=models.ManyToManyField(to='afe.SoftwareComponent', db_table=b'linux_distro_available_software_components'),
        ),
        migrations.AlterUniqueTogether(
            name='kernel',
            unique_together=set([('version', 'cmdline')]),
        ),
        migrations.AddField(
            model_name='job',
            name='dependency_labels',
            field=models.ManyToManyField(to='afe.Label', db_table=b'afe_jobs_dependency_labels', blank=True),
        ),
        migrations.AddField(
            model_name='job',
            name='drone_set',
            field=models.ForeignKey(blank=True, to='afe.DroneSet', null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='parameterized_job',
            field=models.ForeignKey(blank=True, to='afe.ParameterizedJob', null=True),
        ),
        migrations.AddField(
            model_name='ineligiblehostqueue',
            name='job',
            field=models.ForeignKey(to='afe.Job'),
        ),
        migrations.AddField(
            model_name='hostqueueentry',
            name='atomic_group',
            field=models.ForeignKey(blank=True, to='afe.AtomicGroup', null=True),
        ),
        migrations.AddField(
            model_name='hostqueueentry',
            name='host',
            field=models.ForeignKey(blank=True, to='afe.Host', null=True),
        ),
        migrations.AddField(
            model_name='hostqueueentry',
            name='job',
            field=models.ForeignKey(to='afe.Job'),
        ),
        migrations.AddField(
            model_name='hostqueueentry',
            name='meta_host',
            field=models.ForeignKey(db_column=b'meta_host', blank=True, to='afe.Label', null=True),
        ),
        migrations.AddField(
            model_name='host',
            name='labels',
            field=models.ManyToManyField(to='afe.Label', db_table=b'afe_hosts_labels', blank=True),
        ),
        migrations.AddField(
            model_name='host',
            name='locked_by',
            field=models.ForeignKey(blank=True, editable=False, to='afe.User', null=True),
        ),
        migrations.AddField(
            model_name='aclgroup',
            name='hosts',
            field=models.ManyToManyField(to='afe.Host', db_table=b'afe_acl_groups_hosts', blank=True),
        ),
        migrations.AddField(
            model_name='aclgroup',
            name='users',
            field=models.ManyToManyField(to='afe.User', db_table=b'afe_acl_groups_users'),
        ),
        migrations.AlterUniqueTogether(
            name='testparameter',
            unique_together=set([('test', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='softwarecomponent',
            unique_together=set([('kind', 'name', 'version', 'release', 'checksum', 'arch')]),
        ),
        migrations.AlterUniqueTogether(
            name='parameterizedjobprofilerparameter',
            unique_together=set([('parameterized_job_profiler', 'parameter_name')]),
        ),
        migrations.AlterUniqueTogether(
            name='parameterizedjobprofiler',
            unique_together=set([('parameterized_job', 'profiler')]),
        ),
        migrations.AlterUniqueTogether(
            name='parameterizedjobparameter',
            unique_together=set([('parameterized_job', 'test_parameter')]),
        ),
        migrations.AlterUniqueTogether(
            name='linuxdistro',
            unique_together=set([('name', 'version', 'release', 'arch')]),
        ),
    ]
