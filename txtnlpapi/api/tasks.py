from celery import shared_task
from .serializers import BackLogSerializer
from .models import BackLogComment
from celery.utils.log import get_task_logger
import json
from django.contrib.auth.models import User


logger = get_task_logger(__name__)

@shared_task
def csv_to_usercomment(json_data):
    list_data = json.loads(json_data)
    for entry in list_data:    
        serializer = BackLogSerializer(data = {'owner' : list_data[entry]['owner'],
                                                        'topic' : list_data[entry][' topic'],
                                                        'comment' : list_data[entry][' comment']})
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
