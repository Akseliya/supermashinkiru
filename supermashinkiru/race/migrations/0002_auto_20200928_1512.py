# Generated by Django 2.2.16 on 2020-09-28 12:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('race', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=50, null=True)),
                ('used', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ExtendUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin', models.BooleanField(default=False)),
                ('phrase', models.CharField(default='', max_length=100)),
                ('details', models.ManyToManyField(to='race.Details')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=False)),
                ('length', models.SmallIntegerField(null=True)),
                ('description', models.TextField(null=True)),
                ('first_prize', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='race_first_prize', to='race.Details')),
                ('prize', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='race_prize', to='race.Details')),
                ('winner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='race.ExtendUser')),
            ],
        ),
        migrations.CreateModel(
            name='Racer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step', models.SmallIntegerField(null=True)),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='race.Race')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='race.ExtendUser')),
            ],
        ),
        migrations.DeleteModel(
            name='Users',
        ),
        migrations.AddField(
            model_name='car',
            name='form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cars_form', to='race.Details'),
        ),
        migrations.AddField(
            model_name='car',
            name='sticker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cars_sticker', to='race.Details'),
        ),
        migrations.AddField(
            model_name='car',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='race.ExtendUser'),
        ),
        migrations.AddField(
            model_name='car',
            name='wheels',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cars_wheels', to='race.Details'),
        ),
        migrations.AddField(
            model_name='car',
            name='window',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cars_window', to='race.Details'),
        ),
    ]
