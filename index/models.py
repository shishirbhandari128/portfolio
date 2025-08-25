from django.db import models
from django.core.exceptions import ValidationError

class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='logo/')
    intro = models.TextField()
    description = models.TextField()
    skills = models.TextField()
    image = models.ImageField(upload_to='portfolio_images/')
    project_count = models.PositiveIntegerField(default=0)
    footer_text = models.TextField(max_length=200, blank=True, null=True)
    cv = models.FileField(upload_to='cv/', blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Allow saving if this is the first object or if it's an update
        if not self.pk and Portfolio.objects.exists():
            raise ValidationError("Only one portfolio instance is allowed.")
        return super().save(*args, **kwargs)
    
class ContactDetails(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    location = models.TextField()
    country_code = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"

    def save(self, *args, **kwargs):
        # Prevent creation of a new object if one already exists
        if not self.pk and ContactDetails.objects.exists():
            raise ValidationError("Only one ContactDetails instance is allowed.")
        return super().save(*args, **kwargs)
    

class TechnicalSkill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField()  # 0-100 scale

    def __str__(self):
        return f"{self.name} ({self.proficiency}%)"
    
class ProfessionalSkill(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)


class Tools(models.Model):
    name = models.CharField(max_length=50)
    icon_class = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Experience(models.Model):
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.job_title} at {self.company}"
    
class education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    start_date = models.CharField()
    end_date = models.CharField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    institution_image = models.ImageField(upload_to='education_images/')

    def __str__(self):
        return f"{self.degree} from {self.institution}"


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    tools_used = models.ManyToManyField(Tools, blank=True)
    url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
    

class SocialLink(models.Model):
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    stackoverflow = models.URLField(blank=True, null=True)

    def __str__(self):
        return "Social Links"
    
    def save(self, *args, **kwargs):
        # Prevent creation of a new object if one already exists
        if not self.pk and SocialLink.objects.exists():
            raise ValidationError("Only one SocialLink instance is allowed.")
        return super().save(*args, **kwargs)