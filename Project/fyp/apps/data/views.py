import datetime
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView

from apps.authentication.models import CustomUser
from apps.data.forms import ClassScheduleForm, PlanForm, ProfileForm, UserBookingForm, UserForm
from apps.data.models import ClassSchedule, GymPlan, UserBooking


def DashboardView(request):
    msg = None
    
    return render(request, "home/dashboard.html")

def SubscriptionView(request):
    msg = None
    plan = None
    
    try:
        userBooking = UserBooking.objects.get(user_id_id=request.user.user_id)
        plan_detail = GymPlan.objects.get(pk=userBooking.plan_type_id)
        
        plan_end_date = userBooking.start_date + datetime.timedelta(days=int(plan_detail.plan_duration))
        
        plan = {
            'start_date' : userBooking.start_date,
            'plan_name' : plan_detail.plan_name,
            'end_date' : plan_end_date,
            'plan_cost' : plan_detail.plan_cost,
        }
        msg = 'Subscribed'
        
    except UserBooking.DoesNotExist:
        msg = 'Not Subscribed'
        
    return render(request, "home/subscription.html", { "msg" : msg, "plan" : plan })

def ActivityView(request):
    msg = None
    return render(request, "home/activity.html")

    
class UserBookingCreateView(CreateView):
    model = UserBooking
    form_class = UserBookingForm
    template_name = "data/entry.html"
    success_url = reverse_lazy('subscription')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Subscription"
        context['sub_title'] = "Subscribe to a Plan"
        context['plan_costs'] = GymPlan.objects.values_list("plan_cost")
        return context
    
    def form_valid(self, form):
        form.instance.user_id = CustomUser(pk=self.request.user.user_id)
        return super().form_valid(form)
    
    

class ProfileUpdateView(UpdateView):
    model = CustomUser
    form_class = ProfileForm
    template_name = "data/profile.html"
    success_url = reverse_lazy('dashboard')
    

class GymPlanListView(ListView):
    model = GymPlan
    template_name = "data/plans.html"
    context_object_name = 'plans'
    
class GymPlanCreateView(CreateView):
    model = GymPlan
    form_class = PlanForm
    template_name = "data/entry.html"
    success_url = reverse_lazy('gym-plans')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add custom data to the context
        context['title'] = "Gym Plan"
        context['sub_title'] = "Add Gym Plan"
        return context

class GymPlanUpdateView(UpdateView):
    model = GymPlan
    form_class = PlanForm
    template_name = "data/entry.html"
    success_url = reverse_lazy('gym-plans')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add custom data to the context
        context['title'] = "Gym Plan"
        context['sub_title'] = "Update Gym Plan"
        return context
    
class GymPlanDeleteView(DeleteView):
    model = GymPlan
    template_name = "data/plans.html"
    success_url = reverse_lazy('gym-plans')



class UserListView(ListView):
    model = CustomUser
    template_name = "data/user.html"
    context_object_name = 'users'

class UserCreateView(CreateView):
    model = CustomUser
    form_class = UserForm
    template_name = "data/profile.html"
    success_url = reverse_lazy('list-users')

class UserUpdateView(UpdateView):
    model = CustomUser
    form_class = UserForm
    template_name = "data/profile.html"
    success_url = reverse_lazy('list-users')
    
class UserDeleteView(DeleteView):
    model = CustomUser
    template_name = "data/user.html"
    success_url = reverse_lazy('list-users')
    
class UserDetailView(DetailView):
    model = CustomUser
    template_name = "TEMPLATE_NAME"


class ClassScheduleListView(ListView):
    model = ClassSchedule
    template_name = "data/schedules.html"
    context_object_name = 'classes'
    
class ClassScheduleCreateView(CreateView):
    model = ClassSchedule
    form_class = ClassScheduleForm
    template_name = "data/entry.html"
    success_url = reverse_lazy('list-users')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add custom data to the context
        context['title'] = "Class Schedule"
        context['sub_title'] = "Add Class Schedule"
        return context
    
    def post(self, request, *args, **kwargs):

        return super().post(request, *args, **kwargs)

class ClassScheduleUpdateView(UpdateView):
    model = ClassSchedule
    form_class = ClassScheduleForm
    template_name = "data/entry.html"
    success_url = reverse_lazy('list-users')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add custom data to the context
        context['title'] = "Class Schedule"
        context['sub_title'] = "Update Class Schedule"
        return context
    
class ClassScheduleDeleteView(DeleteView):
    model = ClassSchedule
    template_name = "data/schedules.html"
    success_url = reverse_lazy('list-users')