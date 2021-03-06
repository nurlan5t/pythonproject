# Generated by Django 3.1.4 on 2021-01-25 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=100, verbose_name='Article title')),
                ('article_text', models.TextField(verbose_name='Article text')),
                ('publication_date', models.DateTimeField(verbose_name='Date of publication')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=50, verbose_name='Author_name')),
                ('comment_text', models.CharField(max_length=200, verbose_name='Comment_text')),
                ('lenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lenta.lenta')),
            ],
        ),
    ]
