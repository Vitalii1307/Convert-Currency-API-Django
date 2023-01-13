# Convert-Currency-API-Django
The Python language and the Django framework were used to write the program.

Interaction with the API is shown in the exchange.py file:
ExchangeApiDjango\myApp\myApp\convert\exchange.py

Getting the GET parameters in the views.py file:
ExchangeApiDjango\myApp\myApp\views.py

To start the program, you need to go to the directory: ExchangeApiDjango\myApp
and enter the command: python manage.py runserver

To get the result, the user can enter in the URl line:
(for example) http://127.0.0.1:8000/?sum=4555&fromCur=USD&toCur=UAH

or enter all data in the forms and press the "Submit" button

Expected result: {"USD": 4555.0, "UAH": 165963.2}
