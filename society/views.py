from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_http_methods
from .models import SocietyRecord
from pathlib import Path

TEMPLATE_DIR = Path(__file__).resolve().parent.parent / "templates"
PAGE_TITLES = {p.stem: p.stem.replace("_", " ").title() for p in TEMPLATE_DIR.glob("*.html")}


def home(request):
    return render(request, "index.html")


def page(request, page):
    template = f"{page}.html"
    if not (TEMPLATE_DIR / template).is_file():
        return HttpResponseNotFound("Page not found")
    return render(request, template, {"page_title": PAGE_TITLES.get(page, page.title())})


def logout_view(request):
    logout(request)
    return redirect("home")


@require_http_methods(["GET", "POST"])
def action(request, action_name):
    if request.method != "POST":
        # Visiting an action URL directly should return to its related form.
        return redirect(f"/{action_name}/")

    payload = {k: v for k, v in request.POST.items() if k != "csrfmiddlewaretoken"}

    # Authenticate the admin using the Django account created with createsuperuser.
    if action_name == "admin_login":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active and user.is_staff:
            login(request, user)
            return redirect("/admin_dashboard/")
        messages.error(request, "Invalid admin username/password, or this account is not an admin. Create an admin using createsuperuser.")
        return redirect("/admin_login/")

    # Keep all legacy page form submissions functional and store their fields in SQLite.
    category = action_name.replace("_", " ")[:80]
    title = (payload.get("name") or payload.get("username") or payload.get("eventname") or payload.get("title") or action_name)
    SocietyRecord.objects.create(category=category, title=title[:200], details=payload)
    messages.success(request, "Form submitted successfully.")

    # Successful registration/payment/complaint forms return to their own page.
    return redirect(request.META.get("HTTP_REFERER", f"/{action_name}/"))
