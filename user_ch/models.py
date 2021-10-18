from django.db import models



class ClientUser(models.Model):
    u_mobile = models.CharField(max_length=11)
    u_password = models.CharField(max_length=40)
    u_nickname = models.CharField(max_length=60)
    u_image = models.CharField(max_length=200)
    u_mbtype = models.PositiveIntegerField()
    u_bind = models.PositiveIntegerField()
    u_dvcid = models.CharField(max_length=40)
    u_uuid = models.CharField(max_length=32)
    u_cid = models.CharField(max_length=40)
    u_status = models.PositiveIntegerField()
    u_online = models.PositiveIntegerField()
    u_lgtype = models.PositiveIntegerField()
    u_sex = models.PositiveIntegerField()
    expand = models.CharField(max_length=300)
    invite_code = models.CharField(db_column='Invite_code', max_length=32, blank=True, null=True)  # Field name made lowercase.
    u_last_login_time = models.IntegerField()
    u_create_time = models.IntegerField()
    u_update_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'client_user'





# Create your models here.
