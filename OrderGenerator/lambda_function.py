import boto3
import random

# Instance created for AWS SNS service using boto3 package.
sns_client = boto3.client('sns')

# Static data Lists of car types and accessories and addresses for generating Taxi orders.
STATIC_CAR_TYPES = ['Compact', 'Mid-size Sedan', 'SUV', 'Luxury', 'Hatchback', 'Convertible', 'Coupe', 'Pickup Truck', 'Minivan', 'Electric Vehicle (EV)', 'Sports Car', 'Crossover']
STATIC_CAR_ACCESSORIES = ['GPS', 'Camera', 'Bluetooth Hands-Free Kit', 'Seat Covers', 'Floor Mats', 'Roof Rack', 'Dash Cam', 'USB Charger', 'Car Organizer', 'Blind Spot Mirrors', 'Car Phone Mount', 'LED Interior Lights', 'Sunshade', 'Car Air Purifier', 'Heated Seat Cushion', 'Portable Jump Starter']
STATIC_CLIENT_ADDRESSES = ['6050 University Avenue', '123 Main Street', '456 Elm Street', '789 Oak Avenue', '111 Park Road', '222 Maple Lane', '333 Pine Street', '444 Cedar Avenue', '555 Birch Court', '666 Willow Drive', '777 Elmwood Place', '888 Magnolia Boulevard', '999 Spruce Terrace', '1010 Cherry Lane', '1212 Sycamore Street']

# SNS Topic ARN for sending Taxi order messages.
SNS_TOPIC_ARN = 'arn:aws:sns:us-east-1:621130241729:PublishOrder'

def lambda_handler(event, context):
    # Randomly select car type, accessory, and client address using pyhton inbuilt finction random
    selected_car_type = random.choice(CAR_TYPES)
    selected_accessory = random.choice(CAR_ACCESSORIES)
    client_address = random.choice(CLIENT_ADDRESSES)
    
    # Create Taxi order message dictonary body
    order_details = {
        'car_type': selected_car_type,
        'accessory': selected_accessory,
        'address': client_address
    }
    
    # Send created Taxi order message to SNS topic
    response = sns_client.publish(
        TopicArn=SNS_TOPIC_ARN,
        Message=str(order_details)
    )

    return {
        'statusCode': 200,
        'body': 'Halifax Taxi Order sent successfully to SNS Topic' 
    }
