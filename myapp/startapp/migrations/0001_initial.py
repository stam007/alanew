# Generated by Django 2.2.6 on 2019-11-02 04:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_Name', models.TextField(blank=True, default=None, null=True)),
                ('Category_Commercial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_for_commercial', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SousCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SousCategory_Name', models.TextField(blank=True, default=None, null=True)),
                ('SousCategory_Commercial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='souscategory_for_commercial', to='startapp.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Name', models.TextField(blank=True, default=None, null=True)),
                ('Description', models.TextField(blank=True, default=None, null=True)),
                ('Price', models.IntegerField(blank=True, null=True)),
                ('Color', jsonfield.fields.JSONField(blank=True, default=None, null=True)),
                ('Demonsion', jsonfield.fields.JSONField(blank=True, default=None, null=True)),
                ('Image1', models.FileField(blank=True, default=None, null=True, upload_to='')),
                ('Image2', models.FileField(blank=True, default=None, null=True, upload_to='')),
                ('Image3', models.FileField(blank=True, default=None, null=True, upload_to='')),
                ('Image4', models.FileField(blank=True, default=None, null=True, upload_to='')),
                ('Product_Commercial_Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_for_commercial_category', to='startapp.Category')),
                ('Product_Commercial_SousCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_for_commercial_souscategory', to='startapp.SousCategory')),
            ],
        ),
        migrations.CreateModel(
            name='Oders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Color', models.TextField(blank=True, default=None, null=True)),
                ('Demonsion', models.TextField(blank=True, default=None, null=True)),
                ('Quantity', models.IntegerField(blank=True, default=None, null=True)),
                ('Remove', models.BooleanField(blank=True, default=False, null=True)),
                ('Confirm', models.BooleanField(blank=True, default=False, null=True)),
                ('See', models.BooleanField(blank=True, default=False, null=True)),
                ('Order_Client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_for_client', to=settings.AUTH_USER_MODEL)),
                ('Order_Commercial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_for_commercial', to=settings.AUTH_USER_MODEL)),
                ('Order_Product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_for_product', to='startapp.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Details_Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Picture', models.TextField(blank=True, default=None, null=True)),
                ('ClientDetails', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='details_client', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
