from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotFound
from django.urls import reverse
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

