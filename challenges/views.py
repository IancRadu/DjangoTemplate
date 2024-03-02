from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

monthly_challenges = {
    "january": "See for yourself!",
    "february": "Got it!",
    "march": "Go go go!",
    "april": "Do what you want!",
    "may": "See for yourself!",
    "june": "Go go go!",
    "july": "Do what you want!",
    "august": "See for yourself!",
    "september": "Got it!",
    "october": "Go go go!",
    "november": "Do what you want!",
    "december": None
}


def all_months(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {"months": months})


def monthly_challenge(request, month):

    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month})
    except:
        raise Http404()


def monthly_challenge_by_number(request, month):

    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Month is not added in the database")

    redirect_month = months[month - 1]
    redirect_path = reverse("month_challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
