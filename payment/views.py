from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from rest_framework.utils import json

from Canteen_System_Automation import settings
from payment import Checksum
from payment.Checksum import generate_checksum, verify_checksum, generate_checksum_by_str, verify_checksum_by_str
from payment.models import PaytmTxnHistory as PaytmHistory


@csrf_exempt
def pay(request):

    merchantMid = settings.PAYTM_MERCHANT_ID
    merchantKey = settings.PAYTM_MERCHANT_KEY
    order_id = Checksum.__id_generator__()
    #order_id = pk
    channelId = 'WEB'
    custId = "dfsvfdc"
    txnAmount = '10.00'
    website = 'WEBSTAGING'
    industryTypeId = 'Retail'
    callbackUrl = settings.HOST_URL + settings.PAYTM_CALLBACK_URL

    paytmParams = {
        'MID': merchantMid,
        'ORDER_ID': order_id,
        'CUST_ID': custId,
        'INDUSTRY_TYPE_ID': industryTypeId,
        'CHANNEL_ID': channelId,
        'TXN_AMOUNT': txnAmount,
        'WEBSITE': website,
        'CALLBACK_URL': callbackUrl,

    }

    paytmChecksum = generate_checksum(paytmParams, merchantKey)

    paytmParams['CHECKSUMHASH'] = paytmChecksum

    context = {'paytmDict': paytmParams}
    return render(request, 'payment/form1.html', context)


@csrf_exempt
def check(request):

    merchantKey = settings.PAYTM_MERCHANT_KEY

    if request.method == 'POST':

        data_dict = {}
        for key in request.POST:
            data_dict[key] = request.POST[key]

        if 'CHECKSUMHASH' in data_dict.keys():

            paytmChecksum = request.POST['CHECKSUMHASH']

        else:
            paytmChecksum = ''

        #isValidChecksum = verify_checksum_by_str(data_dict, merchantKey, paytmChecksum)
        isValidChecksum = verify_checksum(
            data_dict, merchantKey, paytmChecksum)
        context = {'paytmDict': data_dict}

        if (isValidChecksum):
            PaytmHistory.objects.create(**data_dict)
            return render(request, 'payment/form2.html', context)
        else:
            return HttpResponse("checksum verify failed")
    else:

        return HttpResponse(status=200)


def status(request):
    return render(request, 'payment/status.html')
