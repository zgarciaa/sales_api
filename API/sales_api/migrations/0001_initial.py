# Generated by Django 4.0.5 on 2022-06-20 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('document', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('roles_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales_api.role')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('qty', models.IntegerField()),
                ('sale_at', models.DateTimeField()),
                ('products_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales_api.product')),
                ('users_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales_api.user')),
            ],
        ),
    ]
