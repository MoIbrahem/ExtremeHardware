# Generated by Django 4.0 on 2021-12-31 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_alter_product_unit_price'),
        ('core', '0017_alter_psu_plus_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('productimage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='store.productimage')),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='caseimages', to='core.case')),
                ('cpu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cpuimages', to='core.cpu')),
                ('gpu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gpuimages', to='core.gpu')),
                ('motherboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='motherboardimages', to='core.motherboard')),
                ('psu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='psuimages', to='core.psu')),
            ],
            bases=('store.productimage',),
        ),
    ]
