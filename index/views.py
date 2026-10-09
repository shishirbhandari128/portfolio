from django.conf import settings
from django.core.mail import EmailMessage
from django.shortcuts import render

from .models import (
    ContactDetails,
    Experience,
    Portfolio,
    Project,
    ProfessionalSkill,
    SocialLink,
    TechnicalSkill,
    Tools,
    education,
)


def _site_context():
    return {
        'portfolio': Portfolio.objects.first(),
        'social': SocialLink.objects.first(),
    }


def index_view(request):
    site_context = _site_context()
    contact_details = ContactDetails.objects.first()
    portfolio = site_context['portfolio']
    skills_list = [
        skill.strip()
        for skill in portfolio.skills.split(',')
        if skill.strip()
    ] if portfolio and portfolio.skills else []

    technical_skill = TechnicalSkill.objects.all()
    professional_skills = ProfessionalSkill.objects.all()
    tools = Tools.objects.all()
    education_list = education.objects.all()
    projects = Project.objects.all()
    experiences = Experience.objects.all()

    if request.method == "POST":
        name = request.POST.get("name")
        sender_email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        my_email = (
            contact_details.email
            if contact_details
            else settings.EMAIL_HOST_USER
        )
        full_message = f"From: {name} <{sender_email}>\n\n{message}"
        email = EmailMessage(
            subject=subject,
            body=full_message,
            from_email=settings.EMAIL_HOST_USER,
            to=[my_email],
            reply_to=[sender_email],
        )
        try:
            email.send()
        except Exception as e:
            print("Email failed:", e)

    return render(request, 'index.html', context={
        **site_context,
        'contact_details': contact_details,
        'technical_skill': technical_skill,
        'professional_skills': professional_skills,
        'skills_list': skills_list,
        'tools': tools,
        'experiences': experiences,
        'education_list': education_list,
        'projects': projects,
    })


def all_projects_view(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {
        **_site_context(),
        'projects': projects,
    })
