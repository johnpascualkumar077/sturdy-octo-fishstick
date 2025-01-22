from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import MealRecord
from django.contrib.auth.decorators import login_required

@login_required
def meal_list(request):
    # 現在のユーザーの食事記録を取得
    records = MealRecord.objects.filter(user=request.user).order_by('-date')
    return render(request, 'records/meal_list.html', {'records': records})

from django.http import HttpResponse

def meal_list(request):
    return HttpResponse("Hello, FoodDiary!")
