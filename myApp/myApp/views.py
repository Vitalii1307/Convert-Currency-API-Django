from django.shortcuts import render
from .convert.exchange import currencyConversion

def home(request):
    querySum = request.GET.get('sum')
    queryFromSign = request.GET.get('fromCur')
    queryToSign = request.GET.get('toCur')

    try:
        message = currencyConversion(float(querySum), str(queryFromSign).upper(), str(queryToSign).upper())
    except:
        message ="You entered wrong input"

    template = "home.html"
    context = {
        'message': message,
    }
    return render(request, template, context)
