import boto3
import json
from datetime import datetime
import calendar
import random
import time

from common import credentials

# ScrappingProducer('python-stream')


class ScrappingProducer(object):

    def __init__(self, stream_name):
        self._stream_name = stream_name
        self._kinesis_client = boto3.client(
            'kinesis',
            region_name='us-west-2',
            aws_access_key_id=credentials()['aws']['access_key'],
            aws_secret_access_key=credentials()['aws']['secret_key'])

    def put_to_stream(self, thing_id, payload):

        print(payload)

        put_response = self._kinesis_client.put_record(
            StreamName=self._stream_name,
            Data=json.dumps(payload),
            PartitionKey=thing_id)
        return put_response

    def get_payload(self):

        payload = {
            'prop': str(random.randint(40, 120)),
            'timestamp': str(calendar.timegm(datetime.utcnow().timetuple())),
            'thing_id': thing_id
        }
        return payload

if __name__ == '__main__':
    producer = ScrappingProducer('python-stream')
    thing_id = 'aa-bb'
    while True:
        payload = producer.get_payload()
        put_response = producer.put_to_stream(thing_id, payload)

        # wait for 5 second
        time.sleep(5)
