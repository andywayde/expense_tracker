# Generated by Django 4.1.6 on 2023-02-14 05:30

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("expenses", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="dailyexpense",
            options={"ordering": ["date"]},
        ),
    ]
