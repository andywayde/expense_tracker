from django.urls import path
from .views import (
    ExpenseCategoryListView,
    ExpenseCategoryCreateView,
    ExpenseCategoryUpdateView,
    ExpenseCategoryDeleteView,
)
from .views import (
    DailyExpenseListView,
    DailyExpenseCreateView,
    DailyExpenseUpdateView,
    DailyExpenseDeleteView,
)

urlpatterns = [
    path(
        "expense_categories/",
        ExpenseCategoryListView.as_view(),
        name="expense_category_list",
    ),
    path(
        "expense_categories/create/",
        ExpenseCategoryCreateView.as_view(),
        name="expense_category_create",
    ),
    path(
        "expense_categories/<int:pk>/update/",
        ExpenseCategoryUpdateView.as_view(),
        name="expense_category_update",
    ),
    path(
        "expense_categories/<int:pk>/delete/",
        ExpenseCategoryDeleteView.as_view(),
        name="expense_category_delete",
    ),
    path("daily_expenses/", DailyExpenseListView.as_view(), name="daily_expense_list"),
    path(
        "daily_expenses/create/",
        DailyExpenseCreateView.as_view(),
        name="daily_expense_create",
    ),
    path(
        "daily_expenses/<int:pk>/update/",
        DailyExpenseUpdateView.as_view(),
        name="daily_expense_update",
    ),
    path(
        "daily_expenses/<int:pk>/delete/",
        DailyExpenseDeleteView.as_view(),
        name="daily_expense_delete",
    ),
]
