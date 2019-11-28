"""cap_medical_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Order.views import home_view, dashboard_view, s_view, RulesCreateView, RuleDeleteView, RuleEditView, \
    load_sub_groups, apply_rules
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView

from Order.views import index_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sales/', include('Order.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('', TemplateView.as_view(template_name='home.html')),
    # path('', LoginView.as_view()),
    path('', home_view),
    path('dashboard/', dashboard_view, name='dashboard'),
    # path('teamsettings/', s_view, name='teamsettings'),
    path('teamsettings/', s_view, name='teamsettings'),
    path('teamsettings/create/', RulesCreateView.as_view(), name='create_rules'),
    path('teamsettings/apply_rules/', apply_rules, name='apply_rules'),
    path('teamsettings/<int:id>/delete/', RuleDeleteView.as_view(), name='delete_rule'),
    path('teamsettings/<int:id>/edit/', RuleEditView.as_view(), name='edit_rule'),
    path('ajax/load-subgroups/', load_sub_groups, name='ajax_load_subgroups')
]
