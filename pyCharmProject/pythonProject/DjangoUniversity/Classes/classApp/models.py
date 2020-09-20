from django.db import models

class djangoClasses(models.Model):
    Title = models.CharField(max_length=50)
    Course_Number = models.IntegerField(null = False, default=0)
    Instructor_Name = models.CharField(max_length=30)
    Duration = models.FloatField(max_length=20)

    objects = models.Manager()



pythonCourse = djangoClasses();
pythonCourse.Title = "Python101";
pythonCourse.Course_Number = 404;
pythonCourse.Instructor_Name = "Bob Marley";
pythonCourse.Duration = 60

htmlCourse = djangoClasses();
htmlCourse.Title = "Html";
htmlCourse.Course_Number = 504;
htmlCourse.Instructor_Name = "Ziggy Marley";
htmlCourse.Duration = 60

csharpCourse = djangoClasses();
csharpCourse.Title = "C Sharp";
csharpCourse.Course_Number = 604;
csharpCourse.Instructor_Name = "Fred";
csharpCourse.Duration = 60



