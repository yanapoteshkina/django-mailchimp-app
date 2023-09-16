from django.shortcuts import redirect, render
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError

api_key = "064fd3074b8ad0348f663b209f403416-us21"
list_id = "3d2db5446b"

# function to manage subscriber
def subscribeToNewsLetter(request):
	if request.method == "POST":

		# getting users input from the form
		email = request.POST['email']
		firstName = request.POST['firstName']
		lastName = request.POST['lastName']

		# initializing the mailchimp client with api key
		mailchimpClient = Client()
		mailchimpClient.set_config({
			"api_key": api_key,
		})

		userInfo = {
			"email_address": email,
			"status": "subscribed",
			"merge_fields": {
				"FNAME": firstName,
				"LNAME": lastName
			}
		}

		try:
			# adding member to mailchimp audience list
			mailchimpClient.lists.add_list_member(list_id, userInfo)
			return redirect("success")
		except ApiClientError as error:
			print(error.text)
			return redirect("error")

	return render(request, "home.html")

def success(request):
	return render(request, 'success.html')

def error(request):
	return render(request, 'error.html')
