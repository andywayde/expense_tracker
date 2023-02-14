import calendar
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import ExpenseCategory, DailyExpense
from .forms import ExpenseCategoryForm, DailyExpenseForm
from django.urls import reverse_lazy

from django.db.models import Sum, Avg
from datetime import datetime


class ExpenseCategoryListView(ListView):
    model = ExpenseCategory
    context_object_name = "expense_categories"
    template_name = "expense_category_list.html"


class ExpenseCategoryCreateView(CreateView):
    model = ExpenseCategory
    form_class = ExpenseCategoryForm
    template_name = "expense_category_form.html"
    success_url = reverse_lazy("expense_category_list")


class ExpenseCategoryUpdateView(UpdateView):
    model = ExpenseCategory
    form_class = ExpenseCategoryForm
    template_name = "expense_category_form.html"
    success_url = reverse_lazy("expense_category_list")


class ExpenseCategoryDeleteView(DeleteView):
    model = ExpenseCategory
    template_name = "expense_category_confirm_delete.html"
    success_url = reverse_lazy("expense_category_list")


class DailyExpenseListView(ListView):
    model = DailyExpense
    context_object_name = "expenses"
    template_name = "daily_expense_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        current_day = datetime.now().day
        current_month = datetime.now().month
        current_year = datetime.now().year

        # Get total spent for this month
        total_this_month = DailyExpense.objects.filter(
            date__month=current_month, date__year=current_year
        ).aggregate(Sum("amount"))["amount__sum"]
        context["total_this_month"] = total_this_month

        # Get daily average for this month
        context["daily_average"] = total_this_month / current_day

        return context


class DailyExpenseCreateView(CreateView):
    model = DailyExpense
    form_class = DailyExpenseForm
    template_name = "daily_expense_form.html"
    success_url = reverse_lazy("daily_expense_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = ExpenseCategory.objects.all()
        return context


class DailyExpenseUpdateView(UpdateView):
    model = DailyExpense
    form_class = DailyExpenseForm
    template_name = "daily_expense_form.html"
    success_url = reverse_lazy("daily_expense_list")


class DailyExpenseDeleteView(DeleteView):
    model = DailyExpense
    context_object_name = "expense"
    template_name = "daily_expense_confirm_delete.html"
    success_url = reverse_lazy("daily_expense_list")
