from django.db import models

# 学部
class Department(models.Model):
    department = models.CharField(max_length=150)

    class Meta:
        db_table = 'department'
        verbose_name_plural = '学部'

    def __str__(self):
        return self.department

# 学科
class Subjects(models.Model):
    subject = models.CharField(max_length=150)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'subjects'
        verbose_name_plural = '学科'
    
    def __str__(self):
        return self.subject
    
# 講義名
class Lectures(models.Model):
    lecture = models.CharField(max_length=150)
    lecture_number = models.IntegerField()
    lecture_teacher = models.CharField(max_length=255)
    subject = models.ForeignKey(
        Subjects, on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'lectures'
        verbose_name_plural = '講義名'
    
    def __str__(self):
        return self.lecture
    
#　問題
class Questions(models.Model):
    question = models.FileField(upload_to='questions/')
    lecture = models.ForeignKey(
        Lectures,
        on_delete=models.CASCADE,
        limit_choices_to={'lecture_number':311502}
    )

    class Meta:
        db_table = 'questions'
    
    def __str__(self):
        return str(self.lecture)
