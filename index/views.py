from django.shortcuts import render
from .models import ContactDetails, Portfolio, TechnicalSkill, ProfessionalSkill, Experience,Project, Tools, education, SocialLink
from django.conf import settings
from django.core.mail import EmailMessage

    
def index_view(request):
    print("Index view called")
    contact_details = ContactDetails.objects.first()
    portfolio = Portfolio.objects.first()
    skills_list = []
    if portfolio.skills:
        skills_list = [skill.strip() for skill in portfolio.skills.split(',')]

    technical_skill = TechnicalSkill.objects.all() 
    professional_skills = ProfessionalSkill.objects.all()
    tools = Tools.objects.all()
    education_list = education.objects.all()
    projects = Project.objects.all()  # Assuming you have a Project model
    experiences = Experience.objects.all()
    social = SocialLink.objects.first()
    print (f"Skills List: {skills_list}")
    if request.method == "POST":
        print("Form submitted ✅")
        print(request.POST)

        name = request.POST.get("name")
        sender_email = request.POST.get("email")   # visitor’s email
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        
        print(f"Name: {name}, Email: {sender_email}, Subject: {subject}, Message: {message}")
        # get your destination email from model
        my_email = ContactDetails.objects.first().email if ContactDetails.objects.first() else settings.EMAIL_HOST_USER

        full_message = f"From: {name} <{sender_email}>\n\n{message}"

        # send email
        email = EmailMessage(
            subject=subject,
            body=full_message,
            from_email=settings.EMAIL_HOST_USER,  # ✅ from settings.py
            to=[my_email],                         # your email from model
            reply_to=[sender_email],               # visitor’s email
        )
        try:
            email.send()
            print("✅ Email sent successfully")
        except Exception as e:
            print("❌ Email failed:", e)

   
    return render(request, 'index.html', context={
        'contact_details': contact_details,
        'portfolio': portfolio,
        'technical_skill': technical_skill,
        'professional_skills': professional_skills,
        'skills_list': skills_list,
        'tools': tools,
        'experiences': experiences,
        'education_list': education_list,
        'projects': projects,
        'social': social,
    })

def all_projects_view(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})