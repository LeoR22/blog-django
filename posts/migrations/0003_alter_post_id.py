# Generated by Django 4.2.15 on 2024-08-09 17:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0002_post_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="id",
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
