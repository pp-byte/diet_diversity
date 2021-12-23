from django.db import models
from django.db.models.enums import Choices
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

# Create your models here.
Recipe_List=[('','Select'),
("Roti","Roti"),
("Dudhi sabji" ,"Dudhi sabji"),
("Egg","Egg"),
("rava porridge"),
("Apple","Apple"),
]

Frequency_Days=[('','Select'),
("1","1"),
("2","2"),
("3","3"),
("4","4"),
("5","6"),
("7","7"),
("8","8"),
("9","9"),
("10","10"),
("11","11"),
("12","12"),
("13","13"),
("14","14"),
("15","15"),
("16","16"),
("17","17"),
("18","18"),
("19","19"),
("20","20"),
("21","21"),
("22","22"),
("23","24"),
("25","25"),
("26","26"),
("27","27"),
("28","29"),
("30","30"),
("31","31"),
]

Frequency_Weeks=[('','Select'),
("1","1"),
("2","2"),
("3","3"),
("4","4"),
("5","6"),
("7","7"),
("8","8"),
("9","9"),
("10","10"),
("11","11"),
("12","12"),
("13","13"),
("14","14"),
("15","15"),
("16","16"),
("17","17"),
("18","18"),
("19","19"),
("20","20"),
("21","21"),
("22","22"),
("23","24"),
("25","25"),
("26","26"),
("27","27"),
("28","29"),
("30","30"),
("31","31"),
]

Frequency_Months=[('','Select'),
("1","1"),
("2","2"),
("3","3"),
("4","4"),
("5","6"),
("7","7"),
("8","8"),
("9","9"),
("10","10"),
("11","11"),
("12","12"),
]

Amount=[('','Select'),
("1","1"),
("2","2"),
("3","3"),
("4","4"),
("5","6"),
("7","7"),
("8","8"),
("9","9"),
("10","10"),
("11","11"),
("12","12"),
("13","13"),
("14","14"),
("15","15"),
("16","16"),
("17","17"),
("18","18"),
("19","19"),
("20","20"),
("21","21"),
("22","22"),
("23","24"),
("25","25"),
("26","26"),
("27","27"),
("28","29"),
("30","30"),
("31","31"),
]

Amount_Measure=[('','Select'),
("1","1"),
("2","2"),
("3","3"),
("4","4"),
("5","6"),
("7","7"),
("8","8"),
("9","9"),
("10","10"),
("11","11"),
("12","12"),
("13","13"),
("14","14"),
("15","15"),
("16","16"),
("17","17"),
("18","18"),
("19","19"),
("20","20"),
("21","21"),
("22","22"),
("23","24"),
("25","25"),
("26","26"),
("27","27"),
("28","29"),
("30","30"),
("31","31"),
]

Consistency=[('','Select'),
("pieces","pieces"),
("vati/katori","vati/katori"),
("cup","cup"),
("tablespoon","tablespoon"),
("glass","glass"),
("teaspoon","teaspoon"),
]


class table(models.Model): 
    #  SrNo=models.IntegerField(default=5)
     recipe_name=models.CharField(max_length=122 ,null=True,blank=True)
     daily_freq=models.IntegerField(default=1)
     weekly_freq=models.IntegerField(default=1)
     monthly_freq=models.IntegerField(default=2)
     quan=models.IntegerField(default=3)
    #  unit=models.IntegerField(default=4)
     unit=models.CharField( max_length=122, default='pieces',null=True,blank=True )
     consistency=models.CharField( max_length=122, default='thick',null=True,blank=True )
     remark=models.TextField(default='Test',null=True,blank=True)

class new_item(models.Model):
    recipe_name=models.TextField(default='Test',null=True,blank=True)
    daily_freq=models.IntegerField(default=1)
    weekly_freq=models.IntegerField(default=1)
    monthly_freq=models.IntegerField(default=2)
    quan=models.IntegerField(default=3)
    #  unit=models.IntegerField(default=4)
    unit=models.CharField( max_length=122, default='pieces',null=True,blank=True )
    consistency=models.CharField( max_length=122, default='thick',null=True,blank=True )
    remark=models.TextField(default='Test',null=True,blank=True)



class UploadWellPictureModel(models.Model):
    picture = models.ImageField( upload_to='WellPics/', blank=True, null=True,default='WellPics/noImage.jpg')
    name = models.CharField(max_length=100, blank=True, null=True)
    well_nm = models.CharField(max_length=100, blank=True, null=True)
    def save(self, *args, **kwargs):
        if not self.id:
            self.picture = self.compressImage(self.picture)
        super(UploadWellPictureModel, self).save(*args, **kwargs)
    def compressImage(self,picture):
        imageTemproary = Image.open(picture)
        imageTemproary = imageTemproary.convert('RGB')
        outputIoStream = BytesIO()
        imageTemproary = imageTemproary.resize( (1020,573) ) 
        imageTemproary.save(outputIoStream , format='JPEG', quality=60)
        outputIoStream.seek(0)
        picture = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % picture.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        return picture
