# Generated by Django 3.2.17 on 2023-03-01 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0005_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('M', 'Mobile'), ('L', 'Laptop'), ('TW', 'Top Wear'), ('BW', 'Bottom Wear'), ('N', 'Nuts'), ('O', 'Oil'), ('P', 'Pasta'), ('A', 'Atta'), ('C', 'Chhola'), ('CO', 'Cooking Oil'), ('K', 'Kitchen'), ('R', 'Rice'), ('DP', 'Dal/Pulses'), ('SO', 'Special Offer')], max_length=2),
        ),
    ]
