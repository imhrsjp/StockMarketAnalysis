from django.shortcuts import render
from . import OPS

# Create your views here.

def MainPage(request):
    return render(request, 'mainPage.html')

def HomePage(request):
    return render(request, 'homePage.html')

def FeaturePage(request):
    data_details, stock_details = None, None
    if request.method == 'GET':
        OPS.DATA_AVAILABLE = False
        display_message = 'Select validate information and move ahead'
    elif request.method == 'POST':
        func_value = request.POST.get('function_input')
        stock_symbol = request.POST.get('stock_symbol')
        duration = request.POST.get('duration_input')
        display_message = "Showing result for: "+func_value+" : "+stock_symbol+" : "+duration
        data_details, stock_details = OPS.getDataFromAPI(func_value, stock_symbol, duration)
        # print('POST Called', OPS.DATA_AVAILABLE, stock_data)
    return render(request, 'featurePage.html', {
        "DATA_AVAILABLE": OPS.DATA_AVAILABLE,
        "DISPLAY_MESSAGE": display_message,
        "STOCK_META_DATA": data_details,
        "STOCK_ORIG_DATA": stock_details
    })


def Testing(request):
     return "Testing"




def SendMail():
    print("Email sent successfully")