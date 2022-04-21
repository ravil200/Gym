# Generated by Django 4.0.4 on 2022-04-19 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='aboutus',
            options={},
        ),
        migrations.RenameField(
            model_name='aboutus',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='phone',
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='content',
        ),
        migrations.RemoveField(
            model_name='classes',
            name='content',
        ),
        migrations.RemoveField(
            model_name='classes',
            name='price',
        ),
        migrations.RemoveField(
            model_name='classes',
            name='title',
        ),
        migrations.RemoveField(
            model_name='classes',
            name='trainer',
        ),
        migrations.AddField(
            model_name='aboutus',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='classes',
            name='class_image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='classes',
            name='class_name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='classes',
            name='trainer_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.aboutus'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Trainer',
        ),
        migrations.AddField(
            model_name='schedules',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.classes'),
        ),
    ]