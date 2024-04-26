from django.urls import path

from . import views

urlpatterns = [
    path("dashboard/", views.DashboardView, name="dashboard"),
    path("subscription/", views.SubscriptionView, name="subscription"),
    path("subscribe-now/", views.UserBookingCreateView.as_view(), name="subscribe-now"),
    path("activity/", views.ActivityView, name="activity"),
    
    path("gym-plans/", views.GymPlanListView.as_view(), name="gym-plans"),
    path("add-plan/", views.GymPlanCreateView.as_view(), name="add-plan"),
    path("update-plan/<int:pk>/", views.GymPlanUpdateView.as_view(), name="update-plan"),
    path("delete-plan/<int:pk>/", views.GymPlanDeleteView.as_view(), name="delete-plan"),
    
    path("update-profile/<int:pk>/", views.ProfileUpdateView.as_view(), name="update-profile"),
    
    path("list-users/", views.UserListView.as_view(), name="list-users"),
    path("add-user/", views.UserCreateView.as_view(), name="add-user"),
    path("update-user/<int:pk>/", views.UserUpdateView.as_view(), name="update-user"),
    path("delete-user/<int:pk>/", views.UserDeleteView.as_view(), name="delete-user"),
    
    path("class-schedules/", views.ClassScheduleListView.as_view(), name="class-schedules"),
    path("schedule-class/", views.ClassScheduleCreateView.as_view(), name="schedule-class"),
    path("update-scheduled-class/<int:pk>/", views.ClassScheduleUpdateView.as_view(), name="update-scheduled-class"),
    path("delete-scheduled-class/<int:pk>/", views.ClassScheduleDeleteView.as_view(), name="delete-scheduled-class"),
]