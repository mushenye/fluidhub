# Generated by Django 4.2.2 on 2023-07-28 19:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('content', models.TextField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('date_created', models.DateField(auto_now=True)),
                ('school_name', models.CharField(max_length=100)),
                ('school_code', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('passcode', models.CharField(default='34CDC893CCCC', max_length=12)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='teacher_profile')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('teach_grade', models.CharField(choices=[('RE', 'Reception'), ('P1', 'Pre-Primary 1'), ('P2', 'Pre-Primary 2'), ('G1', 'Grade 1'), ('G2', 'Grade 2'), ('G3', 'grade 3'), ('G4', 'Grade 4'), ('G5', 'Grade 5'), ('G6', 'grade 6'), ('Junior Secondary', 'Junior Secondary')], max_length=50)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learner.school')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('adm_no', models.IntegerField()),
                ('date_of_birth', models.DateField()),
                ('date_joined', models.DateField(auto_now=True)),
                ('grade', models.CharField(choices=[('RE', 'Reception'), ('P1', 'Pre-Primary 1'), ('P2', 'Pre-Primary 2'), ('G1', 'Grade 1'), ('G2', 'Grade 2'), ('G3', 'grade 3'), ('G4', 'Grade 4'), ('G5', 'Grade 5'), ('G6', 'grade 6'), ('Junior Secondary', 'Junior Secondary')], max_length=50)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learner.school')),
            ],
        ),
        migrations.CreateModel(
            name='StrandCreate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(choices=[('RE', 'Reception'), ('P1', 'Pre-Primary 1'), ('P2', 'Pre-Primary 2'), ('G1', 'Grade 1'), ('G2', 'Grade 2'), ('G3', 'grade 3'), ('G4', 'Grade 4'), ('G5', 'Grade 5'), ('G6', 'grade 6'), ('Junior Secondary', 'Junior Secondary')], max_length=50)),
                ('strand', models.CharField(help_text='Enter strand only', max_length=50)),
                ('sub_strand1', models.CharField(blank=True, max_length=200, null=True)),
                ('sub_strand2', models.CharField(blank=True, max_length=200, null=True)),
                ('sub_strand3', models.CharField(blank=True, max_length=200, null=True)),
                ('sub_strand4', models.CharField(blank=True, max_length=200, null=True)),
                ('sub_strand5', models.CharField(blank=True, max_length=200, null=True)),
                ('sub_strand6', models.CharField(blank=True, max_length=200, null=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learner.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default=2023)),
                ('term', models.CharField(max_length=20)),
                ('exam', models.CharField(max_length=20)),
                ('Mathematics', models.IntegerField(default=0)),
                ('English_language', models.IntegerField(default=0)),
                ('Kiswahili', models.IntegerField(default=0)),
                ('Hygiene_and_Nutrition', models.IntegerField(default=0)),
                ('Environmental', models.IntegerField(default=0)),
                ('Art_and_Craft', models.IntegerField(default=0)),
                ('Music', models.IntegerField(default=0)),
                ('Movement', models.IntegerField(default=0)),
                ('Psychomotorcreative', models.IntegerField(default=0)),
                ('Religious_education', models.IntegerField(default=0)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learner.student')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now=True)),
                ('school_logo', models.ImageField(upload_to='profile_pics')),
                ('about', models.TextField(max_length=500)),
                ('school', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='learner.school')),
            ],
        ),
        migrations.CreateModel(
            name='Myclub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('club_name', models.CharField(max_length=80)),
                ('about_club', models.CharField(max_length=400)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learner.school')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('title', models.CharField(blank=True, max_length=30, null=True)),
                ('image', models.ImageField(upload_to='gallery')),
                ('caption', models.TextField(max_length=200)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learner.school')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Exam', 'Exam'), ('Fee Structure', 'Fee Structure'), ('Lesson plan', 'Lesson plan '), ('Schemes', 'Schemes')], max_length=255)),
                ('grade', models.CharField(choices=[('RE', 'Reception'), ('P1', 'Pre-Primary 1'), ('P2', 'Pre-Primary 2'), ('G1', 'Grade 1'), ('G2', 'Grade 2'), ('G3', 'grade 3'), ('G4', 'Grade 4'), ('G5', 'Grade 5'), ('G6', 'grade 6'), ('Junior Secondary', 'Junior Secondary')], default='none', max_length=50)),
                ('document', models.FileField(upload_to='documents/')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('school', models.ForeignKey(default='none', on_delete=django.db.models.deletion.CASCADE, to='learner.school')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now=True)),
                ('address', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=20)),
                ('mobile_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('physical_address', models.CharField(max_length=20)),
                ('pin_location', models.CharField(max_length=20)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learner.school')),
            ],
        ),
        migrations.CreateModel(
            name='ClubActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('activity', models.TextField(max_length=400)),
                ('activity_image', models.ImageField(upload_to='club gallery')),
                ('myclub', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learner.myclub')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learner.school')),
            ],
        ),
        migrations.CreateModel(
            name='Assesment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True, null=True)),
                ('expectation', models.CharField(choices=[('BE', 'BE'), ('AP', 'AP'), ('MT', 'MT'), ('EX', 'EX')], help_text='KEY: EX- Exceeding expextation, MT-Meet Expectation, AP- Approaches epectation, BE- below expectation', max_length=10)),
                ('comment', models.TextField(max_length=200)),
                ('strand', models.ForeignKey(max_length=200, on_delete=django.db.models.deletion.CASCADE, to='learner.strandcreate')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learner.student')),
            ],
        ),
        migrations.CreateModel(
            name='AddtoClub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learner.myclub')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learner.student')),
            ],
        ),
    ]
