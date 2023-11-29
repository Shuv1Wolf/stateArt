import os

from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import HttpResponseRedirect
from django.views.generic.edit import FormMixin
from django.contrib import messages
from django.core.mail import send_mail

from main.models import Article, News, Reviews, Project, Work_Example, Work_Example_In_Project,Main_menu_Model
from .forms import Form


def send_email(phone_number, time, name, url):
    subject = 'state-art'
    from_email = os.getenv("EMAIL_HOST_USER")
    recipient_list = os.getenv("EMAIL_RECIPIENT").split(",")
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Письмо ФОС state-art</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
            }}
            
            .container {{
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
                background-color: #f2f2f2;
                border: 1px solid #ccc;
            }}
    
            h1 {{
                text-align: center;
                color: #333;
            }}
    
            p {{
                margin-bottom: 10px;
            }}
    
            .info {{
                margin-bottom: 20px;
            }}
    
            .info span {{
                font-weight: bold;
            }}
    
            .footer {{
                text-align: center;
                margin-top: 20px;
                color: #666;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Письмо ФОС state-art</h1>
            <div class="info">
                <p><span>Номер телефона:</span> {phone_number}</p>
                <p><span>Удобное время:</span> {time}</p>
                <p><span>Имя:</span> {name}</p>
                <p><span>Адрес инициирования ФОС:</span> {url}</p>
            </div>
            <div class="footer">
                <p>Это автоматическое письмо, пожалуйста не отвечайте на него.</p>
            </div>
        </div>
    </body>
    </html>
    """
    send_mail(subject=subject, from_email=from_email, recipient_list=recipient_list, html_message=html, message='')


class HomePageView(FormMixin, ListView):
    form_class = Form
    model = News
    template_name = "html/index.html"
    context_object_name = "news"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['work_example'] = Work_Example.objects.all()
        return context


    def post(self, request, *args, **kwargs):
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            send_email(form.cleaned_data['phone_number'], form.cleaned_data['time'],
                       form.cleaned_data['name'], form.cleaned_data['url'])
            messages.success(request, 'Спасибо, Ваша заявка принята, мы перезвоним в ближайшее время')
            return HttpResponseRedirect(request.path, {'form': form})
        else:
            return HttpResponseRedirect(request.path, {'form': form})


class ArticleView(FormMixin, ListView):
    form_class = Form
    model = Article
    template_name = "html/article.html"

    def post(self, request, *args, **kwargs):
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Спасибо, Ваша заявка принята, мы перезвоним в ближайшее время')
            return HttpResponseRedirect(request.path, {'form': form})
        else:
            return HttpResponseRedirect(request.path, {'form': form})


class ArticleDetailView(FormMixin, DetailView):
    form_class = Form
    model = Article
    template_name = "html/article_detail.html"
    context_object_name = 'object'

    def post(self, request, *args, **kwargs):
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Спасибо, Ваша заявка принята, мы перезвоним в ближайшее время')
            return HttpResponseRedirect(request.path, {'form': form})
        else:
            return HttpResponseRedirect(request.path, {'form': form})

class ReviewsView(FormMixin, ListView):
    form_class = Form
    model = Reviews
    template_name = "html/reviews.html"
    context_object_name = "reviews"

    def post(self, request, *args, **kwargs):
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Спасибо, Ваша заявка принята, мы перезвоним в ближайшее время')
            return HttpResponseRedirect(request.path, {'form': form})
        else:
            return HttpResponseRedirect(request.path, {'form': form})


class ContactView(FormMixin, TemplateView):
    template_name = "html/contacts.html"
    form_class = Form

    def post(self, request, *args, **kwargs):
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Спасибо, Ваша заявка принята, мы перезвоним в ближайшее время')
            return HttpResponseRedirect(request.path, {'form': form})
        else:
            return HttpResponseRedirect(request.path, {'form': form})


class ProjectView(FormMixin, ListView):
    form_class = Form
    model = Project
    template_name = "html/project.html"

    def get_context_data(self, **kwargs):
        context = super(ProjectView, self).get_context_data(**kwargs)
        context['work_example'] = Work_Example_In_Project.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Спасибо, Ваша заявка принята, мы перезвоним в ближайшее время')
            return HttpResponseRedirect(request.path, {'form': form})
        else:
            return HttpResponseRedirect(request.path, {'form': form})


class ProjectDetailView(FormMixin, DetailView):
    form_class = Form
    model = Project
    template_name = "html/project_detail.html"
    context_object_name = 'object'

    def post(self, request, *args, **kwargs):
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Спасибо, Ваша заявка принята, мы перезвоним в ближайшее время')
            return HttpResponseRedirect(request.path, {'form': form})
        else:
            return HttpResponseRedirect(request.path, {'form': form})


class Work_ExampleDetailView(FormMixin, DetailView):
    form_class = Form
    model = Work_Example
    template_name = "html/work_example.html"
    context_object_name = 'object'

    def post(self, request, *args, **kwargs):
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Спасибо, Ваша заявка принята, мы перезвоним в ближайшее время')
            return HttpResponseRedirect(request.path, {'form': form})
        else:
            return HttpResponseRedirect(request.path, {'form': form})


class Work_Example_In_ProjectDetailView(FormMixin, DetailView):
    form_class = Form
    model = Work_Example_In_Project
    template_name = "html/work_example_2.html"
    context_object_name = 'object'

    def post(self, request, *args, **kwargs):
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Спасибо, Ваша заявка принята, мы перезвоним в ближайшее время')
            return HttpResponseRedirect(request.path, {'form': form})
        else:
            return HttpResponseRedirect(request.path, {'form': form})


class DeliveryView(TemplateView):
    template_name = 'html/delivery.html'

    def post(self, request, *args, **kwargs):
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Спасибо, Ваша заявка принята, мы перезвоним в ближайшее время')
            return HttpResponseRedirect(request.path, {'form': form})
        else:
            return HttpResponseRedirect(request.path, {'form': form})


class How_to_offerView(TemplateView, FormMixin):
    template_name = 'html/how_to_offer.html'
    form_class = Form

    def post(self, request, *args, **kwargs):
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Спасибо, Ваша заявка принята, мы перезвоним в ближайшее время')
            return HttpResponseRedirect(request.path, {'form': form})
        else:
            return HttpResponseRedirect(request.path, {'form': form})


class Main_menuDetailView(FormMixin, DetailView):
    form_class = Form
    model = Main_menu_Model
    template_name = "html/main_menu.html"
    context_object_name = 'object'

    def post(self, request, *args, **kwargs):
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Спасибо, Ваша заявка принята, мы перезвоним в ближайшее время')
            return HttpResponseRedirect(request.path, {'form': form})
        else:
            return HttpResponseRedirect(request.path, {'form': form})