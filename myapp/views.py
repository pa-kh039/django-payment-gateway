from paymentproj.settings import RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY
from django.shortcuts import render
import razorpay #pip install razorpay

# Create your views here.
client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))
def index(request):
    DATA = {"amount": 100,"currency": "INR","receipt": "receipt#1","notes": {"Receiver": "Parth","Message": "Thanks!"},"payment_capture":1}
    payment_order=client.order.create(data=DATA)
    payment_order_id=payment_order['id']
    context={'amount':1, 'api_key':RAZORPAY_API_KEY,'order_id':payment_order_id} #this is in paise
    return render(request,'pay.html',context)