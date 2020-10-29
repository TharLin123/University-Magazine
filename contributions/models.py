from django.db import models
from users.models import Student,Marketing_Coordinator,Faculty,FacultyAcademicYear

class Contribution(models.Model):
    title = models.CharField(max_length=100,null=True,verbose_name='Title',default = 'No Title')
    author = models.ForeignKey(Student,on_delete=models.CASCADE,verbose_name='Author')
    date_posted = models.DateTimeField(null=True,verbose_name='Date Posted',auto_now=True)
    faculty = models.ForeignKey(FacultyAcademicYear, on_delete=models.CASCADE, verbose_name='Faculty',null=True)
    images = models.ImageField(upload_to='contributions',verbose_name='Image for Paragraph-1',null=True)
    images2 = models.ImageField(upload_to='contributions',verbose_name='Image for Paragraph-2',null=True)
    images3 = models.ImageField(upload_to='contributions',verbose_name='Image for Paragraph-3',null=True)
    word_docu = models.FileField(upload_to='word_documentation', verbose_name='Word Documentation',null=True)
    paragraphs = models.TextField(null=True,max_length=15000,blank=True, verbose_name='Paragraph1')
    is_selected = models.BooleanField(default=False,verbose_name="Selected")

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'Contributions'
        ordering = ['-date_posted']
        verbose_name = 'Contribution'
        verbose_name_plural = 'Contributions'


class Comment(models.Model):
    post = models.OneToOneField(Contribution,on_delete=models.CASCADE)
    commenter = models.ForeignKey(Marketing_Coordinator, on_delete= models.CASCADE)
    comment = models.TextField(null=True,verbose_name='Comment')
    date_posted = models.DateField(null=True,verbose_name='Date Posted')
    time_posted = models.TimeField(null=True,auto_now=True,verbose_name='Time Posted')

    class Meta:
        db_table = 'Comments'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f"{self.commenter} made a comment to {self.post.title}."
    



