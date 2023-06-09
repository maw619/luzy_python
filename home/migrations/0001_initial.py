# Generated by Django 4.1.7 on 2023-03-15 00:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncios',
            fields=[
                ('an_key', models.AutoField(primary_key=True, serialize=False)),
                ('an_title', models.CharField(blank=True, max_length=50, null=True)),
                ('an_date', models.CharField(blank=True, max_length=50, null=True)),
                ('an_remarks', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'anuncios',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Diccionario',
            fields=[
                ('dic_key', models.AutoField(primary_key=True, serialize=False)),
                ('dic_palabra', models.CharField(blank=True, max_length=50, null=True)),
                ('dic_definicion', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Diccionario',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Displayverso',
            fields=[
                ('dv_key', models.AutoField(primary_key=True, serialize=False)),
                ('dv_verso', models.IntegerField()),
                ('dv_nro', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'displayVerso',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='EstudioVersos',
            fields=[
                ('ve_key', models.AutoField(primary_key=True, serialize=False)),
                ('ve_fk_e_id_key', models.IntegerField(blank=True, null=True)),
                ('ve_fk_v_idversiculo', models.IntegerField(blank=True, db_column='ve_fk_V_IdVersiculo', null=True)),
            ],
            options={
                'db_table': 'estudio_versos',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('eve_key', models.AutoField(primary_key=True, serialize=False)),
                ('eve_title', models.CharField(blank=True, max_length=50, null=True)),
                ('eve_date', models.CharField(blank=True, max_length=50, null=True)),
                ('eve_remarks', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'eventos',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Lcapitulos',
            fields=[
                ('c_idcapitulo', models.IntegerField(db_column='C_IdCapitulo', primary_key=True, serialize=False)),
                ('c_capitulo_desc', models.IntegerField(blank=True, db_column='C_Capitulo_Desc', null=True)),
            ],
            options={
                'db_table': 'lCapitulos',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Lectura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lec_key', models.FloatField()),
                ('lec_fecha', models.CharField(blank=True, max_length=255, null=True)),
                ('lec_am_libro', models.IntegerField(blank=True, null=True)),
                ('lec_am_cap_start', models.IntegerField(blank=True, null=True)),
                ('lec_am_cap_end', models.IntegerField(blank=True, null=True)),
                ('lec_am_vers_start', models.IntegerField(blank=True, null=True)),
                ('lec_am_vers_end', models.IntegerField(blank=True, null=True)),
                ('lec_pm_libro', models.IntegerField(blank=True, null=True)),
                ('lec_pm_cap_start', models.IntegerField(blank=True, null=True)),
                ('lec_pm_cap_end', models.IntegerField(blank=True, null=True)),
                ('lec_pm_vers_start', models.IntegerField(blank=True, null=True)),
                ('lec_pm_vers_end', models.IntegerField(blank=True, null=True)),
                ('lec_am_start', models.IntegerField(blank=True, null=True)),
                ('lec_am_end', models.IntegerField(blank=True, null=True)),
                ('lec_pm_start', models.IntegerField(blank=True, null=True)),
                ('lec_pm_end', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Lectura',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Lestudios',
            fields=[
                ('e_id_key', models.AutoField(primary_key=True, serialize=False)),
                ('e_estudio', models.CharField(blank=True, max_length=200, null=True)),
                ('e_http', models.CharField(blank=True, max_length=200, null=True)),
                ('e_fk_id_cat', models.IntegerField(blank=True, null=True)),
                ('e_remarks', models.CharField(blank=True, max_length=200, null=True)),
                ('e_short_url', models.CharField(blank=True, max_length=10, null=True)),
                ('e_flag_activo', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'lEstudios',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Llibros',
            fields=[
                ('l_idlibro', models.IntegerField(db_column='L_IdLibro', primary_key=True, serialize=False)),
                ('l_libro_desc', models.CharField(blank=True, db_column='L_Libro_Desc', max_length=200, null=True)),
                ('l_link', models.CharField(blank=True, db_column='L_link', max_length=200, null=True)),
                ('l_link2', models.CharField(blank=True, db_column='L_link2', max_length=200, null=True)),
            ],
            options={
                'db_table': 'lLibros',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='LpaCara',
            fields=[
                ('ca_key', models.AutoField(primary_key=True, serialize=False)),
                ('ca_fk_pa_key', models.IntegerField(blank=True, null=True)),
                ('ca_verso', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'lPa_cara',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Lparadojas',
            fields=[
                ('pa_key', models.AutoField(primary_key=True, serialize=False)),
                ('pa_titulo_cara', models.TextField(blank=True, null=True)),
                ('pa_titulo_sello', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'lParadojas',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='LpaSello',
            fields=[
                ('se_key', models.AutoField(primary_key=True, serialize=False)),
                ('se_fk_pa_key', models.IntegerField(blank=True, null=True)),
                ('se_verso', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'lPa_sello',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Ltema',
            fields=[
                ('t_id_key', models.AutoField(db_column='T_id_key', primary_key=True, serialize=False)),
                ('t_titulo', models.CharField(blank=True, db_column='T_titulo', max_length=200, null=True)),
                ('t_id_verso_start', models.IntegerField(blank=True, db_column='T_id_verso_start', null=True)),
                ('t_id_verso_end', models.IntegerField(blank=True, db_column='T_id_verso_end', null=True)),
            ],
            options={
                'db_table': 'lTema',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='RndVersos',
            fields=[
                ('rv_key', models.AutoField(primary_key=True, serialize=False)),
                ('rv_fk_v_idversiculo', models.IntegerField(blank=True, db_column='rv_fk_V_IdVersiculo', null=True)),
            ],
            options={
                'db_table': 'rnd_Versos',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('user_key', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(blank=True, max_length=50, null=True)),
                ('user_password', models.TextField(blank=True, null=True)),
                ('user_nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('user_apellido', models.CharField(blank=True, max_length=50, null=True)),
                ('user_email', models.CharField(blank=True, max_length=50, null=True)),
                ('user_fk_cia_key', models.IntegerField(blank=True, null=True)),
                ('user_role', models.IntegerField(blank=True, null=True)),
                ('user_address', models.CharField(blank=True, max_length=50, null=True)),
                ('user_llave', models.TextField(blank=True, null=True)),
                ('user_celular', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'Usuarios',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Lversiculos',
            fields=[
                ('v_idversiculo', models.IntegerField(db_column='V_IdVersiculo', primary_key=True, serialize=False)),
                ('v_contenido', models.TextField(blank=True, db_column='V_Contenido', null=True)),
                ('v_versiculo', models.IntegerField(blank=True, db_column='V_versiculo', null=True)),
                ('v_lbla', models.TextField(blank=True, db_column='V_LBLA', null=True)),
                ('v_nas', models.TextField(blank=True, db_column='V_NAS', null=True)),
                ('v_idcapitulo', models.ForeignKey(blank=True, db_column='V_IdCapitulo', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.lcapitulos')),
            ],
            options={
                'db_table': 'lVersiculos',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='lcapitulos',
            name='c_idlibro',
            field=models.ForeignKey(blank=True, db_column='C_IdLibro', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.llibros'),
        ),
    ]
