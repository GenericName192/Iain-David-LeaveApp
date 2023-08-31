from time import strftime
from django.shortcuts import redirect, render
import holidays
from datetime import datetime, date

# Create your views here.
def dashBoard(request):
    return render(request, "WYWMLeaveApp/dashboard.html")

def companyHolidays(request):
    return render(request, "WYWMLeaveApp/company_holidays.html")

def leaveApproval(request):
    return render(request, "WYWMLeaveApp/leave_approval.html")

def leaveBalance(request):
    return render(request, "WYWMLeaveApp/leave_balance.html")

def leaveRequest(request):
    return render(request, "WYWMLeaveApp/leave_request.html")

def profileSettings(request):
    return render(request, "WYWMLeaveApp/profile_settings.html")

def loginUser(request):
    return render(request, "WYWMLeaveApp/login.html")

def logOutUser(request):
    return redirect("dashBoard")



def holidayList(request):
    date = datetime.now()
    year = date.year
    uk_holidays = sorted(holidays.UK(years=year, subdiv="ENG").items(), key=lambda x: x[0])
    ca_holidays = sorted(holidays.CA(years=year).items(), key=lambda x: x[0])
    au_holidays = sorted(holidays.AU(years=year).items(), key=lambda x: x[0])
    us_holidays = sorted(holidays.US(years=year).items(), key=lambda x: x[0])

    
    for date in uk_holidays:
        if datetime.now().date() < date[0]:
            print("its doing the thing")


    context = {
        'uk_holidays': uk_holidays,
        'ca_holidays': ca_holidays,
        'au_holidays': au_holidays,
        'us_holidays': us_holidays,
    }

    return render(request, 'WYWMLeaveApp/holiday_list.html', context)