# Generated by Django 2.0.3 on 2018-03-26 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spa_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='RecordLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='spa_app.Musician'),
        ),
        migrations.AddField(
            model_name='album',
            name='record_label',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='spa_app.RecordLabel'),
        ),
        migrations.AddField(
            model_name='musician',
            name='pet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='spa_app.Pet'),
        ),
    ]
