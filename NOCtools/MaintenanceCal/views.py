import time
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response

from dbs.cal.models import *

MONTH_NAMES = "January February March April May June July August September October November December"
MONTH_NAMES = MONTH_NAMES.split()

# Create your views here.

@login_required
def main(request, year=None):
	""" Shows a three year view """
	if year: year = int(year)
	else:    year = time.localtime()[0]

	nowYear, nowMonth = time.localtime()[:2]
	lst = []

	for y in [year, year+1, year+2]:
		monthLst = []
		for n, month in enumerate(MONTH_NAMES):
			entry	= current = False
			entries	= entry.objects.filter(date__year=y, date__month=n+1)

			if entries:
				entry = True
			if y == nowYear and n+1 == nowMonth:
				current = True
			monthLst.append(dict(n=n+1, name=month, entry=entry, current=current))
		lst.append((y, monthLst))

	return render_to_response("cal/", dict(years=lst, user=request.user, year=year, reminders=reminders(request)))


		
