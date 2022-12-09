# Generated by Django 3.2.13 on 2022-12-08 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MBTI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mbti',
            name='board',
            field=models.CharField(choices=[('특징', '특징'), ('주의할 점', '주의할 점'), ('상대법', '상대법')], max_length=50),
        ),
        migrations.AlterField(
            model_name='mbti',
            name='mbti',
            field=models.CharField(choices=[('INFP', 'INFP'), ('ENFJ', 'ENFJ'), ('INFJ', 'INFJ'), ('INTP', 'INTP'), ('ISFP', 'ISFP'), ('ESFJ', 'ESFJ'), ('ESTJ', 'ESTJ'), ('ESFP', 'ESFP'), ('ISPT', 'ISTP'), ('ISTJ', 'ISTJ'), ('ESTP', 'ESTP'), ('INTJ', 'INTJ'), ('ENTP', 'ENTP'), ('ISFJ', 'ISFJ'), ('ENTJ', 'ENTJ'), ('ENFP', 'ENFP')], max_length=50),
        ),
    ]
