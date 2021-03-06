# Generated by Django 2.2 on 2019-04-13 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth2_provider', '0010_auto_20190406_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='authorization_grant_type',
            field=models.CharField(choices=[('authorization-code', 'Authorization code'), ('implicit', 'Implicit'), ('password', 'Resource owner password-based'), ('client-credentials', 'Client credentials'), ('openid-hybrid', 'OpenID connect hybrid')], max_length=32),
        ),
    ]
