from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.views.decorators.http import require_POST
from .models import Task
from django.core.paginator import Paginator


@login_required
def home(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        description = request.POST.get("description", "").strip()

        if title:
            Task.objects.create(
                user=request.user,
                title=title,
                description=description,
            )
            messages.success(request, "Task added successfully!")
            return redirect("home")

        messages.error(request, "Please enter a task title.")

    # Get the logged-in user's tasks
    tasks = Task.objects.filter(
        user=request.user
    ).order_by("-created_at")

    # Search
    search_query = request.GET.get("search", "").strip()

    if search_query:
        tasks = tasks.filter(title__icontains=search_query)

    # Filter by status
    status = request.GET.get("status", "")

    if status == "completed":
        tasks = tasks.filter(completed=True)
    elif status == "pending":
        tasks = tasks.filter(completed=False)

    # Calculate statistics for all of this user's tasks
    all_tasks = Task.objects.filter(user=request.user)

    total_tasks = all_tasks.count()
    completed_tasks = all_tasks.filter(completed=True).count()
    pending_tasks = all_tasks.filter(completed=False).count()

    # Render the page (keep this INSIDE home())
    # Paginate filtered tasks: 5 tasks per page
    paginator = Paginator(tasks, 5)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "tasks/home.html", {
    "tasks": page_obj,
    "page_obj": page_obj,
    "total_tasks": total_tasks,
    "completed_tasks": completed_tasks,
    "pending_tasks": pending_tasks,
    "search_query": search_query,
    "status": status,
})

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        description = request.POST.get("description", "").strip()

        if title:
            task.title = title
            task.description = description
            task.save()
            messages.success(request, "Task updated successfully!")
            return redirect("home")

        messages.error(request, "Task title cannot be empty.")

    return render(request, "tasks/edit.html", {"task": task})
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()

    return render(request, "tasks/register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("home")
    else:
        form = AuthenticationForm(request)

    return render(request, "tasks/login.html", {"form": form})



@require_POST
def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save(update_fields=["completed"])
    messages.success(request, "Task status updated!")
    return redirect("home")


@require_POST
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    messages.success(request, "Task deleted successfully!")
    return redirect("home")
