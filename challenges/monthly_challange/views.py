from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotFound
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

months = {
    "janaury": "pray every morning",
    "feburary": "walk 10k steps minimum daily",
    "march": "listen to motivational stuff every morning",
    "april": "learn the act of affirmation",
    "may": "activate the act of meditation",
    "june": "look for opportunites to always speak and express self",
    "july": "do weight execise daily",
    "august": "learn web application via django",
    "september": "lunce my frst product",
    "october": "incumbate more deployment ideas",
    "november": "focus on continuos improvement and heilth",
    "december": "learn how to impact my kids with the know of God and the power in Jesus"
}

   

def index(response):
    str = ""
    for i in months.keys():
        r = reverse("mntname",args=[i])
        str += f'<li><a href="{r}">{i.capitalize()}</a></li>' 
    res = f"<ul> {str} </ul>" 
    return HttpResponse(res)
def mnt_int(response,mnt):
    r = list(months.keys())
    res = r[mnt -1]
    reply = reverse("mntname",args=[res])
    return HttpResponseRedirect(reply)

def mnt_str(response,mnt):
    try:
        res = months[mnt]
        respond = render_to_string("monthly_challange/ex.html")
        return HttpResponse(respond)
    except:
        return HttpResponseNotFound("Invalid month selected")
    