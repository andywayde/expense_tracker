from django.urls import path
from .views import (
    ExpenseListView,
    ExpenseDetailView,
    ExpenseCreateView,
    ExpenseUpdateView,
)

urlpatterns = [
    path("expenses/", ExpenseListView.as_view(), name="expense_list"),
    path("expenses/<int:pk>/", ExpenseDetailView.as_view(), name="expense_detail"),
    path("expense/add/", ExpenseCreateView.as_view(), name="expense_add"),
    path("expence/<int:pk>/edit", ExpenseUpdateView.as_view(), name="expense_update"),
]
