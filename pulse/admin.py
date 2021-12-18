from django.contrib import admin
from .models import Pulse
from django.contrib.admin import ModelAdmin



@admin.action(description='download')
def download_csv(modeladmin, request, queryset):
    import csv
    f = open('some.csv', 'wb')
    writer = csv.writer(f)
    writer.writerow(['owner', 'Preprocessed','Time_send','HeartRate','Temp','Auxiliary1','Auxiliary2','Auxiliary3','labeled'])
    for s in queryset:
        writer.writerow([s.owner, s.Preprocessed,s.Time_send,s.HeartRate,s.Temp,s.Auxiliary1,s.Auxiliary2,s.Auxiliary3,s.labeled])


# Register your models here.
@admin.register(Pulse)
class Pulse(ModelAdmin):
    fields = ('owner', 'Preprocessed','HeartRate','Temp','Auxiliary1','Auxiliary2','Auxiliary3','labeled')
    list_display = ('owner', 'Preprocessed','Time_send','HeartRate','Temp','Auxiliary1','Auxiliary2','Auxiliary3','labeled')
    actions = [download_csv]
'''
      owner = models.ForeignKey(user , on_delete = models.CASCADE , null = False)
    Preprocessed = models.CharField(max_length=20 , null = True)
    Device_ID = models.CharField(max_length=100 , unique=True)
    Time_send = models.DateTimeField(auto_now=True , null=False)
    HeartRate = models.CharField(max_length=100 , null = True)
    Temp = models.CharField(max_length= 100, null= True, blank= True)
    Auxiliary1 = models.CharField(max_length= 100 , null= True , blank= True)
    Auxiliary2 = models.CharField(max_length= 100 , null= True , blank= True)
    Auxiliary3 = models.CharField(max_length= 100 , null= True , blank= True)
    labeled = models.CharField(max_length=100 , null = True)
'''

