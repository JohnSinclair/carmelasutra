from django.db import models
from django.utils import timezone
import datetime
from django.utils.html import escape, mark_safe
# Create your models here.

class Picture(models.Model):
    upload = models.ImageField(upload_to ='uploads/images/'+str(datetime.datetime.now().year)+'/'+str(datetime.datetime.now().month)+'/'+str(datetime.datetime.now().day)+'/') 
    name = models.CharField(max_length=100, default="")
    path= models.CharField(default='uploads/images/'+str(datetime.datetime.now().year)+'/'+str(datetime.datetime.now().month)+'/'+str(datetime.datetime.now().day)+'/', max_length=40)

  
    @property
    def url(self):
        return self.upload.url

    def thumbnail(self):
        return  mark_safe('<img src="%s" width="150" height="100"/><br><br>' % (self.url))
    thumbnail.short_description = 'Thumbnail'

    def image_tag(self):
        return mark_safe('<img src="/'+self.path+'/%s" width="150" height="100" /><br> <br>' % (self.upload))
    image_tag.short_description = 'Image'
    

    def __str__(self):
        return mark_safe("<div>"+str(self.name)+'<br> '+self.thumbnail()+"</div>")


class PictureCollection(models.Model):
    name = models.CharField(max_length=100, default="")
    preview_image = models.ForeignKey(Picture, on_delete=models.PROTECT)
    pictures = models.ManyToManyField(Picture, related_name="picture_collection", blank=True)

    

    @property
    def thumbnail_url(self):
        return self.preview_image.url

    def thumbnail(self):
        return  mark_safe('<img src="%s" width="150" height="100"/><br><br>' % (self.thumbnail_url))
    thumbnail.short_description = 'Thumbnail'

    def thumbnails(self):
        html=""
        for pic in self.pictures.all():
            html+=mark_safe("<div>"+str(pic.name)+'<br> ''<img src="%s" width="150" height="100"/><br><br>' % pic.upload.url)+' '
        return  mark_safe(html)
    thumbnails.short_description = 'Thumbnails'


    def __str__(self):
        return mark_safe("<div>"+str(self.name)+'<br> '+self.thumbnail()+"</div>")



class CourseOfLife(models.Model):#apparently cv is a type lol
    title = models.CharField(max_length=100, default="")
    bio = models.TextField("bio", null=True, blank=True)
    image = models.ImageField(upload_to ='uploads/cv/images/'+str(datetime.datetime.now().year)+'/'+str(datetime.datetime.now().month)+'/'+str(datetime.datetime.now().day)+'/') 
    experience = models.TextField("work experience", null=True, blank=True)
    education = models.TextField("education", null=True, blank=True)
    works= models.TextField("published works", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'CV'
        verbose_name_plural = 'CVs'

    def __str__(self):
        return self.title

    @property
    def url(self):
        return self.path+'/'+self.title

