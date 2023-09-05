# Generated by Django 4.2.4 on 2023-08-29 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_profile_comment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="blog.category",
            ),
        ),
    ]