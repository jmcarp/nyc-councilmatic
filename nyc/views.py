from django.shortcuts import render
from datetime import date, timedelta
from nyc.models import NYCBill
from councilmatic_core.models import Event

def index(request):
    one_month_ago = date.today() + timedelta(days=-30)
    recent_legislation = NYCBill.objects.exclude(last_action_date=None).filter(last_action_date__gt=one_month_ago).order_by('-last_action_date').all()
    recently_passed = [l for l in recent_legislation if l.inferred_status == 'Passed' and l.bill_type == 'Introduction']

    context = {
        'recent_legislation': recent_legislation,
        'recently_passed': recently_passed,
        'next_council_meeting': Event.next_city_council_meeting(),
        'upcoming_committee_meetings': list(Event.upcoming_committee_meetings()),
    }

    return render(request, 'nyc/index.html', context)
