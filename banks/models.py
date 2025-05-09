from django.db import models

class Bank(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=49)

    class Meta:
        managed = False
        db_table = 'banks'

class Branch(models.Model):
    ifsc = models.CharField(max_length=11, primary_key=True)
    bank = models.ForeignKey(Bank, on_delete=models.DO_NOTHING, db_column='bank_id')
    branch = models.CharField(max_length=74)
    address = models.TextField()
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=26)

    class Meta:
        managed = False
        db_table = 'branches'