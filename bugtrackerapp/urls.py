from django.urls import path
from . import views

app_name = 'bugtracker'

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  # path('admin/', views.admin_dashboard, name='admin_dashboard'),
  # path('tester/', views.tester_dashboard, name='tester_dashboard'),
  # path('developer/', views.developer_dashboard, name='developer_dashboard'),
  path('manage_role_assignment/', views.manage_role_assignment, name='manage_role_assignment'),
  path('manage_role_assignment/role_update/<int:roleassignment_id>/', views.role_update, name='role_update'),
  path('projects/', views.projects_view, name='projects_view'),
  path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
  path('projects/add_project/', views.add_project, name='add_project'),
  path('tickets/', views.tickets_view, name='tickets_view'),
  path('tickets/history_delete/', views.history_delete, name='history_delete'),
  path('tickets/<int:ticket_id>/', views.ticket_detail, name='ticket_detail'),
  path('projects/add_ticket/', views.add_ticket, name='add_ticket'),
  path('tickets/ticket_update/<int:ticket_id>/', views.ticket_update, name='ticket_update'),
  path('tickets/ticket_delete/<int:ticket_id>/', views.ticket_delete, name='ticket_delete'),
  path('comment_delete/<int:comment_id>/', views.comment_delete, name='comment_delete'),

  path('tickets/tickets_tester', views.tickets_tester, name='tickets_tester'),
  path('tickets/tickets_developer', views.tickets_developer, name='tickets_developer'),
  path('reports/', views.reports, name='reports'),
  path('export-to-csv/', views.tickets_export_to_csv, name='tickets_export_to_csv'),
  path('export-to-xlsx/', views.tickets_export_to_xlsx, name='tickets_export_to_xlsx'),
]

