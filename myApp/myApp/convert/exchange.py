import requests
import json

api_key = "81f484dd36a55efdaac972a253b1fba6"
url = "http://api.exchangeratesapi.io/v1/latest?access_key=" + api_key

dataURL = requests.get(url).text

dataJson = json.loads(dataURL)

dataRates = dataJson["rates"]

def currencyConversion(amount, fromCurrency, toCurrency):
    convertedAmount = round(amount * dataRates[toCurrency]/dataRates[fromCurrency], 2)
    result = {fromCurrency: amount, toCurrency: convertedAmount}
    return json.dumps(result)
