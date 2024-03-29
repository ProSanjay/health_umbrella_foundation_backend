from django.shortcuts import render
from django.views import View
from .models import key_value_table, ejournal_table, subscription_table
from django.http import JsonResponse
import logging
logger = logging.getLogger('file_log')

class EjournalView(View):
    logger.info("\nrequest to ejournal view")
    def get(self, request):
        try:
            # final data to send to user
            final_data = {}

            # getting the top 3 ejournal and text
            ejournals = []
            for ejournal in ejournal_table.objects.filter(show=True).order_by("-publish_date")[:3]:
                ejournals.append({
                    "imageLink": ejournal.image.url,
                    "fileLink": ejournal.file.url
                })
            logger.info("fetched top 3 ejournal data")
            
            final_data.update({
                "latestEjournalPage": {
                    "text": key_value_table.objects.get(key='ejournal_page_text').value,
                    "ejournals": ejournals
                }
            })
            logger.info("fetched data for latestEjournalPage")


            final_data.update({"allEjournalPage": {"text": key_value_table.objects.get(key='all_ejournal_page_text').value}})
            logger.info("fetched data for allEjournalPage")

            return JsonResponse(data=final_data, status=200)
        except Exception as e:
            logger.error(e)
            return JsonResponse(data={"message": "error while getting data"}, status=500)


class GetAllEjournal(View):
    logger.info("\nrequest to get all journal view")
    def get(self, request):
        try:
            # data to be sent to user
            final_data = {}

            # get year from request's query parameter
            year = int(request.GET.get('year'))
            logger.info("fetched year", year)

            ejournals = []
            for ejournal in ejournal_table.objects.filter(publish_date__year=year):
                ejournals.append({
                    "name": ejournal.name,
                    "imageLink": ejournal.image.url,
                    "fileLink": ejournal.file.url
                })
            final_data.update({"ejournals": ejournals})
            logger.info("fetched all ejournals")

            return JsonResponse(data=final_data, status=200)
        except Exception as e:
            logger.error(e)
            return JsonResponse(data={"message": "error while getting data"}, status=500)

def subscribe(request):
    logger.info("\nrequest to subscribe")
    try:
        # check if email already in database
        email = str(request.GET.get('email'))
        logger.info("fetched email")
        # create new user if not exist else set send=True
        if not subscription_table.objects.filter(email_address=email).exists():
            subscriber = subscription_table(
                email_address = email,
                send = True
            )
            subscriber.save()
            logger.info("creating new subscriber")
        else:
            subscriber = subscription_table.objects.get(email_address=email)
            subscriber.send = True
            subscriber.save()
            logger.info("subscriber already exists")
        return JsonResponse(data={"message": "subscribed successfully"}, status=200)
    except Exception as e:
        logger.error(e)
        return JsonResponse(data={"message": "error while subscribing"}, status=500)

def unsubscribe(request):
    logger.info("\nrequest to unsubscribe")
    try:
        # check if email already in database
        email = str(request.GET.get('email'))
        logger.info("email subscriber")
        # set send=False if user exist else return failed message
        if subscription_table.objects.filter(email_address=email).exists():
            subscriber = subscription_table.objects.get(email_address=email)
            subscriber.send = False
            subscriber.save()
            logger.info("subscriber unsubscribed")
        else:
            logger.error("subscriber do not exist")
            return JsonResponse(data={"message": "user not found"}, status=404)

        return JsonResponse(data={"message": "unsubscribed successfully"}, status=200)
    except Exception as e:
        logger.error(e)
        return JsonResponse(data={"message": "error while subscribing"}, status=500)