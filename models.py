from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser, User
# ~ from django.contrib.contenttypes.models import ContentType
# ~ from django.contrib.contenttypes.fields import GenericForeignKey


class CustomUser(AbstractUser):
    usr_id = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    phone = models.BigIntegerField(unique=True, null=True, blank=True)
    # full_name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.username)


class UsersBaseProfiles(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to="pics/profiles")

    def __str__(self):
        return str(self.user.usr_id)

class CreatorsModel(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    creator_id = models.UUIDField(default=uuid4(), primary_key=True, editable=False)
    creator_page_name = models.TextField()
    page_description = models.TextField()
    page_cover = models.ImageField(upload_to='creators/covers', null=True)
    about_author = models.TextField()
    creation_timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "Creator account for {}".format(self.user.username)

class CoursesModel(models.Model):
	course_owner=models.ForeignKey(CreatorsModel,on_delete=models.CASCADE)
	course_id=models.UUIDField(default=uuid4(),primary_key=True,editable=False)
	course_title=models.CharField(max_length=200)
	course_desc=models.TextField()
	course_image=models.ImageField(upload_to='courses/',null=False,blank=False)
	course_slug=models.SlugField(max_length=200,unique=True,null=True)
	course_hour=models.IntegerField()
	# ~ sub_courses
	
	#//////////////////
	BEGGINERS='begginers'
	INTERMEDIATE='Intermediate'
	ADVANCED='advanced'
	
	#////////
	COURSE_LEVEL_CHOICE=[
		(BEGGINERS,'begginers'),(INTERMEDIATE,'Intermediate'),(ADVANCED,'advanced')
	]
	course_level=models.CharField(choices=COURSE_LEVEL_CHOICE,max_length=15,default=BEGGINERS)
	def __str__(self):
		return self.course_title


class SubcoursesModels(models.Model):
	sub_course_id=models.UUIDField(default=uuid4(),primary_key=True,editable=False)
	sub_course_title=models.CharField(max_length=200)
	sub_course_desc=models.TextField()
	course_video=models.UUIDField(default=uuid4(),editable=True)
	courses=models.ForeignKey(CoursesModel,on_delete=models.CASCADE)
	def __str__():
		return self.sub_course_title

class SubcourseVideoModels(models.Model):
	sub_course_video_id=models.UUIDField(default=uuid4(),primary_key=True,editable=False)
	sub_course_video_title=models.CharField(max_length=200)
	sub_course_video_content=models.FileField(upload_to='courses/videos',null=False,blank=False)
	sub_course_video_image=models.ImageField(upload_to='courses/images',null=False,blank=False)
	subcourses=models.ForeignKey(SubcoursesModels,on_delete=models.CASCADE)
	
	def __str__():
		return self.sub_course_video_title




