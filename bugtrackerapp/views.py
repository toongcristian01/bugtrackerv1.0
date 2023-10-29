from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from .models import Comment, Project, Ticket, Type, Priority, Status
from accounts.models import EmployeeProfile
from .forms import CommentForm, EditTicketForm, CreateProjectFormAdmin, EditProjectFormAdmin, CreateTicketForm,  ManageRoleAssignment, EditManageRoleAssignment
from django.contrib.auth.models import User
from django.db.models import Q
from django.db.models import Count
from .tables import ProjectTable
from django.contrib.auth.decorators import login_required

@login_required(login_url="/")
def home(request):
  labels = []
  projects_data = []
  tickets_type = []
  num_tickets = []
  projects = Project.objects.all()
  projects_table = ProjectTable()
  projects_tickets = Ticket.objects.filter()
  tickets = Ticket.objects.all()
  tickets_with_project_counts = Project.objects.annotate(ticket_count=Count('ticket'))

  tickets_type_issue_count = Ticket.objects.filter(type__type="issue").count()
  tickets_type_bug_count = Ticket.objects.filter(type__type="bug").count()
  tickets_type_featurerequired_count = Ticket.objects.filter(type__type="feature required").count()

  tickets_priority_low_count = Ticket.objects.filter(priority__priority="low").count()
  tickets_priority_intermediate_count = Ticket.objects.filter(priority__priority="intermediate").count()
  tickets_priority_high_count = Ticket.objects.filter(priority__priority="high").count()

  tickets_priority_open_count = Ticket.objects.filter(status__status="open").count()
  tickets_priority_inprogress_count = Ticket.objects.filter(status__status="in progress").count()
  tickets_priority_resolved_count = Ticket.objects.filter(status__status="resolved").count()
  tickets_priority_closed_count = Ticket.objects.filter(status__status="closed").count()

  tickets_priorities_counts = Ticket.objects.annotate(ticket_priorities_count=Count('priority'))
  tickets_status_counts = Ticket.objects.annotate(ticket_status_count=Count('status'))
  types = Type.objects.all()
  priorities = Priority.objects.all()
  status = Status.objects.all()
  for project in projects:
    labels.append(project.name)
    projects_data.append(project.name)
    num_tickets.append(project.name)
  context={
    'projects': projects,
    'projects_data': projects_data,
    'labels': labels,
    'projects_data': projects_data,
    'projects_table': projects_table,
    'tickets':tickets,
    'types':types,
    'priorities':priorities,
    'status':status,
    'tickets_with_project_counts':tickets_with_project_counts,
    'tickets_type_issue_count':tickets_type_issue_count,
    'tickets_type_bug_count':tickets_type_bug_count,
    'tickets_type_featurerequired_count':tickets_type_featurerequired_count,
    'tickets_priority_low_count':tickets_priority_low_count,
    'tickets_priority_intermediate_count':tickets_priority_intermediate_count,
    'tickets_priority_high_count':tickets_priority_high_count,
    'tickets_priority_open_count':tickets_priority_open_count,
    'tickets_priority_inprogress_count':tickets_priority_inprogress_count,
    'tickets_priority_resolved_count':tickets_priority_resolved_count,
    'tickets_priority_closed_count':tickets_priority_closed_count,

    
  }

  return render(request, 'bugtrackerapp/home.html', context)

@login_required(login_url="/")
def manage_role_assignment(request):
  employees = EmployeeProfile.objects.all()
  manage_role_form = ManageRoleAssignment(request.POST or None, request.FILES or None)
  if request.method == 'POST':
    manage_role_form = ManageRoleAssignment(request.POST or None, request.FILES or None)
    if manage_role_form.is_valid():
      manage_role_form.save()
      return redirect('bugtracker:manage_role_assignment')
  context = {
    'manage_role_form':manage_role_form,
    'employees': employees
  }
  return render(request, 'bugtrackerapp/add_user_roles.html', context)

@login_required(login_url="/")
def role_update(request, roleassignment_id):
  roleassignment = get_object_or_404(EmployeeProfile, id=roleassignment_id)
  roleupdate_form = EditManageRoleAssignment(instance=roleassignment)
  if request.method == 'POST':
    roleupdate_form = EditManageRoleAssignment(request.POST or None, request.FILES or None, instance=roleassignment)
    if roleupdate_form.is_valid():
      roleupdate_form.save()
      return redirect('bugtracker:manage_role_assignment')
  return render(request, 'bugtrackerapp/role_update.html', {'roleupdate_form': roleupdate_form, 'roleassignment':roleassignment})

@login_required(login_url="/")
def projects_view(request):
  projects = Project.objects.all().order_by('-created')
  return render(request, 'bugtrackerapp/projects.html', {'projects':projects})

@login_required(login_url="/")
def project_detail(request, project_id):
  project = get_object_or_404(Project, id=project_id)
  tickets_by_project = Ticket.objects.filter(project=project)
  tickets_by_project_count = tickets_by_project.count()
  context = {
    'project':project,
    'tickets_by_project':tickets_by_project,
    'tickets_by_project_count':tickets_by_project_count,
  }
  return render(request, 'bugtrackerapp/project_detail.html', context)

@login_required(login_url="/")
def add_project(request):
  add_project_form = CreateProjectFormAdmin(request.POST or None, request.FILES or None)
  if request.method == 'POST':
    add_project_form = CreateProjectFormAdmin(request.POST or None, request.FILES or None)
    if add_project_form.is_valid():
      add_project_form.save()
      return redirect('bugtracker:projects_view')
  return render(request, 'bugtrackerapp/add_project.html', {'add_project_form':add_project_form})

@login_required(login_url="/")
def add_ticket(request):
  add_ticket_form = CreateTicketForm(request.POST or None, request.FILES or None)
  if request.method == 'POST':
    add_ticket_form = CreateTicketForm(request.POST or None, request.FILES or None)
    if add_ticket_form.is_valid():
      add_ticket_form.save()
      return redirect('bugtracker:projects_view')
  return render(request, 'bugtrackerapp/add_ticket.html', {'add_ticket_form':add_ticket_form})

@login_required(login_url="/")
def tickets_view(request):
  #display all tickets except resolved status
  tickets = Ticket.objects.exclude(status=3)
  resolved_tickets = Ticket.objects.filter(status=3)
  tickets_count = tickets.count()
  resolved_tickets_count = resolved_tickets.count()
  context = {
    'resolved_tickets':resolved_tickets,
    'tickets':tickets,
    'tickets_count':tickets_count,
    'resolved_tickets_count':resolved_tickets_count,
  }
  return render(request, 'bugtrackerapp/tickets.html', context)

@login_required(login_url="/")
def ticket_detail(request, ticket_id):
  comment = ''
  comment_form = CommentForm(request.POST or None)
  ticket = get_object_or_404(Ticket, id=ticket_id)
  ticket_developer = Ticket.objects.filter(assign_members=request.user)
  # show/hide buttons based on current user
  is_user_ticket = ticket.author == request.user.profile
  is_developer_ticket = ticket.assign_members.contains(request.user)
  # comment
  comments = Comment.objects.filter(ticket=ticket).order_by('-date')
  # create comment form
  if request.method == 'POST':
    comment_form = CommentForm(request.POST or None)
    if comment_form.is_valid():
      comment = comment_form.save(commit=False)
      comment.ticket = ticket
      comment.name = request.user.profile
      comment.save()
      return redirect(reverse('bugtracker:ticket_detail', args=[ticket.id]))
  context = {
  'ticket':ticket, 
  'is_user_ticket':is_user_ticket,
  'is_developer_ticket':is_developer_ticket,
  'comments': comments,
  'comment_form':comment_form
  }
  return render(request, 'bugtrackerapp/ticket_detail.html', context)

def comment_delete(ticket_id):
  ticket = get_object_or_404(Ticket, id=ticket_id)
  comment = get_object_or_404(Comment, id=ticket.project.id)
  ticket_project_id = ticket.project.id
  comment.delete()
  return redirect(reverse('bugtracker:ticket_detail', args=[ticket.id]))

@login_required(login_url="/")
def ticket_update(request, ticket_id):
  ticket = get_object_or_404(Ticket, id=ticket_id)
  ticket_form = EditTicketForm(instance=ticket)
  ticket_project_id = ticket.project.id
  if request.method == 'POST':
    ticket_form = EditTicketForm(request.POST or None, request.FILES or None, instance=ticket)
    if ticket_form.is_valid():
      ticket_form.save()
      #return redirect(reverse('bugtracker:project_detail', args=[ticket_project_id]))
      return redirect('bugtracker:tickets_view')
  return render(request, 'bugtrackerapp/ticket_update.html', {'ticket_form': ticket_form})

@login_required(login_url="/")
def ticket_delete(request, ticket_id):
  ticket = get_object_or_404(Ticket, id=ticket_id)
  ticket_project_id = ticket.project.id
  ticket.delete()
  return redirect(reverse('bugtracker:project_detail', args=[ticket_project_id]))

@login_required(login_url="/")
def tickets_tester(request):
    employee = EmployeeProfile.objects.get(user=request.user)
    tickets = Ticket.objects.filter(
      Q(assign_members=request.user) | Q(author=employee)
    )
    context = {
      'tickets':tickets
    }
    print(tickets)
    return render(request, 'bugtrackerapp/tickets_tester.html', context)

@login_required(login_url="/")
def tickets_developer(request):
    employee = EmployeeProfile.objects.get(user=request.user)
    tickets = Ticket.objects.filter(
      Q(assign_members=request.user) | Q(author=employee)
    )
    context = {
      'tickets':tickets
    }
    return render(request, 'bugtrackerapp/tickets_developer.html', context)