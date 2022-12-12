# Generated by Django 3.2.13 on 2022-12-12 13:21

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
                ('board', models.CharField(choices=[('상대법', '상대법'), ('특징', '특징'), ('주의할 점', '주의할 점')], max_length=50)),
                ('mbti', models.CharField(choices=[('INTP', 'INTP'), ('ESTP', 'ESTP'), ('ESFJ', 'ESFJ'), ('INFJ', 'INFJ'), ('ENFJ', 'ENFJ'), ('ISPT', 'ISTP'), ('ESFP', 'ESFP'), ('ISTJ', 'ISTJ'), ('INTJ', 'INTJ'), ('ISFJ', 'ISFJ'), ('ENTP', 'ENTP'), ('ESTJ', 'ESTJ'), ('ENFP', 'ENFP'), ('ISFP', 'ISFP'), ('INFP', 'INFP'), ('ENTJ', 'ENTJ')], max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
            ],
        ),
    ]
