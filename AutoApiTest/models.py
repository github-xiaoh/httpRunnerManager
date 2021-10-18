from django.db import models


class CaseInfo(models.Model):
    '''用例表'''
    case_name = models.CharField(max_length=50)
    status = models.IntegerField()
    request_info = models.TextField()
    author = models.CharField(max_length=20)
    belong_project = models.CharField(max_length=10)
    belong_module = models.CharField(max_length=10)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    type = models.IntegerField()
    include = models.TextField()
    expect = models.TextField()
    validate = models.TextField()

    class Meta:
        managed = False
        db_table = 'case_info'



class ReportInfo(models.Model):
    '''报告表'''
    report_name = models.CharField(max_length=50)
    status = models.IntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    report_html = models.TextField()

    class Meta:
        managed = False
        db_table = 'report_info'


class ProjectInfo(models.Model):
    '''项目表'''
    project_name = models.CharField(max_length=50)
    status = models.IntegerField()
    test_user = models.CharField(max_length=50)
    dev_user = models.CharField(max_length=50)
    responsible_name = models.CharField(max_length=50)
    publish_app = models.CharField(max_length=20)
    simple_desc = models.TextField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'project_info'


class ModuleInfo(models.Model):
    '''模块表'''
    module_name = models.CharField(max_length=50)
    status = models.IntegerField()
    test_user = models.CharField(max_length=50)
    belong_project_id = models.IntegerField()
    simple_desc = models.TextField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    def __str__(self):
        return self.module_name

    class Meta:
        managed = False
        db_table = 'module_info'




# Create your models here.
