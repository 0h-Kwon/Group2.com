# Generated by Django 3.0.3 on 2020-07-23 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_date', models.CharField(max_length=10)),
                ('m_time', models.CharField(max_length=10)),
                ('m_place', models.CharField(max_length=60)),
                ('m_nname', models.CharField(max_length=30)),
                ('m_gender', models.CharField(max_length=10)),
                ('m_num', models.CharField(max_length=5)),
                ('m_rival', models.CharField(max_length=30)),
            ],
        ),
    ]
