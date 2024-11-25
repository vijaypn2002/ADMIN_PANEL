from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import User, Role
import json  # Add import for JSON handling

# Dashboard View
def dashboard(request):
    return render(request, 'dashboard.html')  # Match the exact folder structure



from django.shortcuts import render, redirect
from .models import Role
from .forms import RoleForm

def roles_view(request):
    if request.method == "POST":
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("roles")
    else:
        form = RoleForm()

    roles = Role.objects.all()
    return render(request, "roles.html", {"roles": roles, "form": form})


# Permissions View
def permissions_view(request):
    roles = Role.objects.all()
    return render(request, "permissions.html", {"roles": roles})  # Match path

# Add Role
def add_role(request):
    if request.method == "POST":
        role_name = request.POST.get("role_name")
        permissions = request.POST.getlist("permissions[]")
        role = Role.objects.create(name=role_name, permissions={perm: True for perm in permissions})
        return redirect('roles')

# Delete Role
def delete_role(request, role_id):
    role = get_object_or_404(Role, id=role_id)
    role.delete()
    return redirect('roles')

# Update Permission
def update_permission(request, role_id):
    if request.method == "POST":
        role = get_object_or_404(Role, id=role_id)
        data = json.loads(request.body)
        permission = data.get("permission")
        value = data.get("value")
        role.permissions[permission] = value
        role.save()
        return JsonResponse({"status": "success"})

from django.http import Http404

from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import User, Role

# Users View with Filter
def users_view(request):
    # Get filter parameters from the request
    name_filter = request.GET.get("name", "")
    email_filter = request.GET.get("email", "")
    role_filter = request.GET.get("role", "")
    status_filter = request.GET.get("status", "")

    # Filter users based on the query parameters
    users = User.objects.all()

    if name_filter:
        users = users.filter(name__icontains=name_filter)
    if email_filter:
        users = users.filter(email__icontains=email_filter)
    if role_filter:
        users = users.filter(role__id=role_filter)
    if status_filter:
        users = users.filter(status=(status_filter == "1"))  # Active (1) or Inactive (0)

    roles = Role.objects.all()

    return render(
        request,
        "users.html",
        {
            "users": users,
            "roles": roles,
            "filters": {
                "name": name_filter,
                "email": email_filter,
                "role": role_filter,
                "status": status_filter,
            },
        },
    )



def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('users')



from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Role

def edit_user(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        role_id = request.POST.get('role')
        status = request.POST.get('status') == 'on'

        user = get_object_or_404(User, id=user_id)
        role = get_object_or_404(Role, id=role_id)

        # Update user details
        user.name = name
        user.email = email
        user.role = role
        user.status = status
        user.save()

        return redirect('users')


from django.shortcuts import render, redirect, get_object_or_404
from .models import Role

def roles_view(request):
    roles = Role.objects.all()
    return render(request, "roles.html", {"roles": roles})

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Role

from django.shortcuts import render, redirect
from .models import User, Role  # Assuming these models exist
from django.contrib import messages

def add_user(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        role_id = request.POST.get("role")
        status = request.POST.get("status") == "on"
        role = Role.objects.get(id=role_id)

        User.objects.create(name=name, email=email, role=role, status=status)
        messages.success(request, "User added successfully!")
        return redirect("users")  # Redirect to the users list page

    roles = Role.objects.all()
    return render(request, "add_user.html", {"roles": roles})



def edit_role(request, role_id):
    role = get_object_or_404(Role, id=role_id)
    if request.method == "POST":
        role.name = request.POST.get("role_name")
        permissions = request.POST.getlist("permissions[]")
        role.permissions = {perm: True for perm in permissions}
        role.save()
        return redirect("roles")

def delete_role(request, role_id):
    role = get_object_or_404(Role, id=role_id)
    role.delete()
    return redirect("roles")


def edit_user(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        user = User.objects.get(id=user_id)
        user.name = request.POST.get("name")
        user.email = request.POST.get("email")
        user.role = Role.objects.get(id=request.POST.get("role"))
        user.status = request.POST.get("status") == "on"
        user.save()
        messages.success(request, "User updated successfully!")
        return redirect("users")

def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    messages.success(request, "User deleted successfully!")
    return redirect("users")
