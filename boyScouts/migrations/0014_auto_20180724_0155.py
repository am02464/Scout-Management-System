# Generated by Django 2.0.4 on 2018-07-23 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boyScouts', '0013_scoutbadge'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scout_Proficiency_Badge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateOfPassing', models.DateField()),
                ('certificateNo', models.CharField(blank=True, max_length=4)),
                ('badge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boyScouts.Badge')),
                ('scout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boyScouts.Scout')),
            ],
        ),
        migrations.RenameModel(
            old_name='ScoutBadge',
            new_name='Scout_Rank_Badge',
        ),
    ]