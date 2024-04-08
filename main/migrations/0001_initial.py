# Generated by Django 4.2.9 on 2024-02-08 06:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Hobby",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=200, verbose_name="name of hobby"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("bio", models.TextField(blank=True)),
                ("photo", models.ImageField(default=None, upload_to="avatars/")),
                (
                    "hobby",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.hobby",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Stories",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=200, verbose_name="title of stories"),
                ),
                ("content", models.TextField(verbose_name="text of stories")),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("likes", models.IntegerField(verbose_name="likes of stories")),
                ("photo", models.ImageField(default=None, upload_to="images_stories/")),
                (
                    "hobby",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.hobby"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Statistics",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("second", models.IntegerField(default=0)),
                ("numberofhappy", models.IntegerField()),
                ("timeofhappy", models.DateTimeField(auto_now_add=True)),
                ("numberofanger", models.IntegerField()),
                ("timeofanger", models.DateTimeField(auto_now_add=True)),
                ("numberofcontempt", models.IntegerField()),
                ("timeofcontempt", models.DateTimeField(auto_now_add=True)),
                ("numberofdisgust", models.IntegerField()),
                ("timeofdisgust", models.DateTimeField(auto_now_add=True)),
                ("numberoffear", models.IntegerField()),
                ("timeofear", models.DateTimeField(auto_now_add=True)),
                ("numberofneutral", models.IntegerField()),
                ("timeofneutral", models.DateTimeField(auto_now_add=True)),
                ("numberofsad", models.IntegerField()),
                ("timeofsad", models.DateTimeField(auto_now_add=True)),
                ("numberofsurprise", models.IntegerField()),
                ("timeofsurprise", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.userprofile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "content",
                    models.CharField(max_length=200, verbose_name="text of comments"),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "stories",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.stories"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
