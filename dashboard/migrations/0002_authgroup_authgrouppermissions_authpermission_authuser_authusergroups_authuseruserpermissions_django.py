# Generated by Django 3.1.2 on 2020-10-30 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tab1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indicator_id', models.IntegerField(blank=True, null=True)),
                ('indicator_name', models.CharField(blank=True, max_length=255, null=True)),
                ('classification_id', models.IntegerField(blank=True, null=True)),
                ('indicator_order', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('unit_id', models.IntegerField(blank=True, null=True)),
                ('unit_name', models.CharField(blank=True, max_length=40, null=True)),
                ('subgroup_id', models.IntegerField(blank=True, null=True)),
                ('subgroup_name', models.CharField(blank=True, max_length=20, null=True)),
                ('subgroup_order', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('area_id', models.IntegerField(blank=True, null=True)),
                ('area_parent_id', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('area_code', models.CharField(blank=True, max_length=20, null=True)),
                ('area_name', models.CharField(blank=True, max_length=50, null=True)),
                ('area_level', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('timeperiod_id', models.IntegerField(blank=True, null=True)),
                ('timeperiod', models.CharField(blank=True, max_length=90, null=True)),
                ('data_value', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'tab1',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tab2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indicator_id', models.IntegerField(blank=True, null=True)),
                ('indicator_name', models.CharField(blank=True, max_length=255, null=True)),
                ('classification_id', models.IntegerField(blank=True, null=True)),
                ('indicator_order', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('unit_id', models.IntegerField(blank=True, null=True)),
                ('unit_name', models.CharField(blank=True, max_length=40, null=True)),
                ('subgroup_id', models.IntegerField(blank=True, null=True)),
                ('subgroup_name', models.CharField(blank=True, max_length=20, null=True)),
                ('subgroup_order', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('area_id', models.IntegerField(blank=True, null=True)),
                ('area_parent_id', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('area_code', models.CharField(blank=True, max_length=20, null=True)),
                ('area_name', models.CharField(blank=True, max_length=50, null=True)),
                ('area_level', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('timeperiod_id', models.IntegerField(blank=True, null=True)),
                ('timeperiod', models.CharField(blank=True, max_length=90, null=True)),
                ('data_value', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'tab2',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tab3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indicator_id', models.IntegerField(blank=True, null=True)),
                ('indicator_name', models.CharField(blank=True, max_length=255, null=True)),
                ('classification_id', models.IntegerField(blank=True, null=True)),
                ('indicator_order', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('unit_id', models.IntegerField(blank=True, null=True)),
                ('unit_name', models.CharField(blank=True, max_length=40, null=True)),
                ('subgroup_id', models.IntegerField(blank=True, null=True)),
                ('subgroup_name', models.CharField(blank=True, max_length=20, null=True)),
                ('subgroup_order', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('area_id', models.IntegerField(blank=True, null=True)),
                ('area_parent_id', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('area_code', models.CharField(blank=True, max_length=20, null=True)),
                ('area_name', models.CharField(blank=True, max_length=50, null=True)),
                ('area_level', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('timeperiod_id', models.IntegerField(blank=True, null=True)),
                ('timeperiod', models.CharField(blank=True, max_length=90, null=True)),
                ('data_value', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'tab3',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tab4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indicator_id', models.IntegerField(blank=True, null=True)),
                ('indicator_name', models.CharField(blank=True, max_length=255, null=True)),
                ('classification_id', models.IntegerField(blank=True, null=True)),
                ('indicator_order', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('unit_id', models.IntegerField(blank=True, null=True)),
                ('unit_name', models.CharField(blank=True, max_length=40, null=True)),
                ('subgroup_id', models.IntegerField(blank=True, null=True)),
                ('subgroup_name', models.CharField(blank=True, max_length=20, null=True)),
                ('subgroup_order', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('area_id', models.IntegerField(blank=True, null=True)),
                ('area_parent_id', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('area_code', models.CharField(blank=True, max_length=20, null=True)),
                ('area_name', models.CharField(blank=True, max_length=50, null=True)),
                ('area_level', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('timeperiod_id', models.IntegerField(blank=True, null=True)),
                ('timeperiod', models.CharField(blank=True, max_length=90, null=True)),
                ('data_value', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'tab4',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tabs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indicator_id_tab4', models.IntegerField(blank=True, null=True)),
                ('indicator_name_tab4', models.CharField(blank=True, max_length=255, null=True)),
                ('classification_id_tab4', models.IntegerField(blank=True, null=True)),
                ('indicator_order_tab4', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('unit_id_tab4', models.IntegerField(blank=True, null=True)),
                ('unit_name_tab4', models.CharField(blank=True, max_length=40, null=True)),
                ('subgroup_id_tab4', models.IntegerField(blank=True, null=True)),
                ('subgroup_name_tab4', models.CharField(blank=True, max_length=20, null=True)),
                ('subgroup_order_tab4', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('area_id_tab4', models.IntegerField(blank=True, null=True)),
                ('area_parent_id_tab4', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('area_code_tab4', models.CharField(blank=True, max_length=20, null=True)),
                ('area_name_tab4', models.CharField(blank=True, max_length=50, null=True)),
                ('area_level_tab4', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('timeperiod_id_tab4', models.IntegerField(blank=True, null=True)),
                ('timeperiod_tab4', models.CharField(blank=True, max_length=90, null=True)),
                ('data_value_tab4', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'tabs',
                'managed': False,
            },
        ),
    ]
