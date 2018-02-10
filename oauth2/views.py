import os
import httplib2

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from apiclient.discovery import build

CLIENT_SECRETS = os.path.join(
    os.path.dirname(__file__), 'client_secrets.json')
    
SCOPE='https://www.googleapis.com/auth/spreadsheets'

REDIRECT_URI='http://localhost:8000/oauth2/oauth2callback'

FLOW=flow_from_clientsecrets(CLIENT_SECRETS,SCOPE, REDIRECT_URI)

@login_required
def Oauth2View(request):
		
		#need if no credential
		authorize_url=FLOW.step1_get_authorize_url()
		
		return HttpResponseRedirect(authorize_url)
		
@login_required
def Oauth2CallbackView(request):
	code=request.GET.get("code")
	
	credential=FLOW.step2_exchange(request.GET['code'])
	
	storage=Storage(os.path.join(os.path.dirname(__file__),'credentials.dat'))
	storage.put(credential)

	http=httplib2.Http()
	http=credential.authorize(http)
	
	service=build('sheets', 'v4', http=http)
	
	a=service.spreadsheets().values().get(
		spreadsheetId='1fX4TfxfoieBUrz17oso8Kwk4PqAvSmd1I-rP8ZegcI0',
		range='A1:E1').execute()
	a=b

	return HttpResponseRedirect(reverse('homepage-view'))
		
	


	
