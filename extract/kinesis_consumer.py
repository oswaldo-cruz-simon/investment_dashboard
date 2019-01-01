import boto3
import json
from datetime import datetime
import time

from common import config


class ProjectConsumer(object):

    def __init__(self, stream_name):
        self._stream_name = stream_name
        self._kinesis_client = boto3.client(
            'kinesis',
            region_name='us-west-2',
            aws_access_key_id=config()['aws']['credentials']['access_key'],
            aws_secret_access_key=config()['aws']['credentials']['secret_key'])
        response = self._kinesis_client.describe_stream(
            StreamName=self._stream_name)

        self._shard_id = response['StreamDescription'][
            'Shards'][0]['ShardId']

    def get_data(self):
        shard_iterator = self._kinesis_client.get_shard_iterator(
            StreamName=self._stream_name,
            ShardId=self._shard_id,
            ShardIteratorType='LATEST')

        my_shard_iterator = shard_iterator['ShardIterator']

        record_response = self._kinesis_client.get_records(
            ShardIterator=my_shard_iterator,
            Limit=2)

        while 'NextShardIterator' in record_response:
            record_response = self._kinesis_client.get_records(
                ShardIterator=record_response['NextShardIterator'],
                Limit=2)
            if len(record_response['Records']) > 0:
                print(record_response)
            time.sleep(5)

if __name__ == '__main__':
    producer = ProjectConsumer('python-stream')
    producer.get_data()
