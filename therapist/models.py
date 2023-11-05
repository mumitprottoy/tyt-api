from django.db import models
from django.contrib.auth.models import User



class Therapist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username



class ExpertiseField(models.Model):
    field = models.CharField(max_length=250)
    
    def __str__(self):
        return self.field



class TherapistExpertise(models.Model):
    therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    expertise = models.ForeignKey(ExpertiseField, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.therapist} : {self.expertise}'
    
    
    
class TherapistExperience(models.Model):
    therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    started_prof_therapy = models.DateField()
    
    def __str__(self):
        return f'{self.therapist} : {self.started_prof_therapy}'



class TherapistProfilePicture(models.Model):
    therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    url = models.TextField()
    
    def __str__(self):
        return str(self.therapist)
    
    
    
class TherapistWorkplace(models.Model):
    therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    workplace = models.CharField(max_length=250)
    
    def __str__(self):
        return f'{self.therapist} : {self.workplace}'



class TherapistQualification(models.Model):
    therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=250)
    
    def __str__(self):
        return f'{self.therapist} : {self.qualification}'
