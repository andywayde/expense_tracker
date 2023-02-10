from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.db.models import Sum

from .models import Expense
from .forms import ExpenseForm


# Create your views here.
class ExpenseListView(ListView):
    model = Expense
    template_name = "expense_list.html"
    context_object_name = "expenses"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_money_spent"] = Expense.objects.aggregate(Sum("money_spent"))[
            "money_spent__sum"
        ]
        return context


class ExpenseDetailView(DetailView):
    model = Expense
    template_name = "expense_detail.html"
    context_object_name = "expense"


class ExpenseCreateView(CreateView):
    model = Expense
    fields = ["money_spent", "date"]
    template_name = "expense_form.html"
    success_url = reverse_lazy("expense_list")


class ExpenseUpdateView(UpdateView):
    model = Expense
    form_class = ExpenseForm
    template_name = "expense_update.html"
    success_url = reverse_lazy("expense_list")
