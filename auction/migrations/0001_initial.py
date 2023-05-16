# Generated by Django 3.2 on 2023-05-16 22:48

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
            name='Bidder',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('bid', models.DecimalField(decimal_places=2, max_digits=30)),
            ],
            options={
                'db_table': 'bidder',
                'ordering': ['bid'],
            },
        ),
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=30)),
                ('increment', models.DecimalField(decimal_places=2, max_digits=10)),
                ('auction_date', models.DateTimeField()),
                ('sold', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Properties',
                'db_table': 'property',
            },
        ),
        migrations.CreateModel(
            name='LotImage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='property')),
                ('image_url', models.URLField(editable=False, max_length=2048)),
                ('lot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auction.lot')),
            ],
            options={
                'verbose_name_plural': 'Property Images',
            },
        ),
        migrations.AddIndex(
            model_name='lot',
            index=models.Index(fields=['name', 'price', 'increment'], name='property_name_c22598_idx'),
        ),
        migrations.AddField(
            model_name='bidder',
            name='lot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auction.lot'),
        ),
        migrations.AddField(
            model_name='bidder',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddIndex(
            model_name='lotimage',
            index=models.Index(fields=['image_url'], name='img_idx'),
        ),
        migrations.AddIndex(
            model_name='bidder',
            index=models.Index(fields=['user', 'bid'], name='bid_idx'),
        ),
    ]
