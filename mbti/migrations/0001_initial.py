# Generated by Django 3.2.13 on 2022-12-14 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mbti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board', models.CharField(choices=[('상대법', '상대법'), ('주의할 점', '주의할 점'), ('특징', '특징')], max_length=50)),
                ('character', models.CharField(max_length=50)),
                ('summary', models.CharField(max_length=200)),
                ('mbti', models.CharField(choices=[('ESFJ', 'ESFJ'), ('ISTJ', 'ISTJ'), ('ENTP', 'ENTP'), ('ENFP', 'ENFP'), ('ENTJ', 'ENTJ'), ('ESTJ', 'ESTJ'), ('INTP', 'INTP'), ('ESTP', 'ESTP'), ('ENFJ', 'ENFJ'), ('ISFJ', 'ISFJ'), ('ISTP', 'ISTP'), ('ESFP', 'ESFP'), ('ISFP', 'ISFP'), ('INFP', 'INFP'), ('INFJ', 'INFJ'), ('INTJ', 'INTJ')], max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/images/')),
            ],
        ),
    ]
