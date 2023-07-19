import boto3
import json

# Instance created for AWS SNS and AWS SQS service using boto3 package.
sqs_client = boto3.client('sqs')
sns_client = boto3.client('sns')

# SQS Queue URL for polling Taxi orders messages.
SQS_QUEUE_URL = 'https://sqs.us-east-1.amazonaws.com/621130241729/HalifaxTaxiQueue'

# SNS Topic ARN for sending Taxi order messages to subscribed emails..
SNS_TOPIC_ARN = 'arn:aws:sns:us-east-1:621130241729:SendMail'

def lambda_handler(event, context):

    # polling a single message from the SQS queue. 
    # This will eliminate use of for loop as I'm polling only a message at time.
    response = sqs_client.receive_message(
        QueueUrl=QUEUE_URL,
        MaxNumberOfMessages=1,
        WaitTimeSeconds=20
    )
    
    # Check if any message was received 
    if 'Messages' in response:
        message = response['Messages'][0]
        
        # get only order taxi message from the SQS order message body.
        taxi_order_message = json.loads(message['Body'])['Message']
        
        # Send the order message to SNS for email notification
        sns_client.publish(
            TopicArn=TOPIC_ARN,
            Message=taxi_order_message,
            Subject='New Car Delivery Order'
        )
        
        # Delete the message from the SQS queue after processing
        sqs_client.delete_message(
            QueueUrl=QUEUE_URL,
            ReceiptHandle=message['ReceiptHandle']
        )
        
        print('Order sent to SNS for email notification:', taxi_order_message)

    return {
        'statusCode': 200,
        'body': 'SQS order taxi order message sent SNS successfully for email notifications.'
    }
