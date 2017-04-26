import json, boto3, uuid
import sys

def  main(argv):
        sqs = boto3.resource('sqs', region_name="eu-central-1")

        tweets = sqs.get_queue_by_name(QueueName='mq2017')
        response = tweets.send_message(MessageBody=argv, MessageAttributes={
                'Author': {
                        'StringValue': 'Jakub',
                        'DataType': 'String'
                }
        })

if __name__ == "__main__":
        main(sys.argv[1])
