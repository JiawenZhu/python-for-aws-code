import json
import boto3
import logging
from datetime import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    try:
        response = ec2.create_snapshot(
            VolumeId='vol-02a8dc1cdc379e562',
            Description='My EC2 Snapshot',
            TagSpecifications=[
                {
                    'ResourceType': 'snapshot',
                    'Tags': [
                        {
                            'Key': 'Name',
                            'Value': f"My EC2 snapshot {current_date}"
                            }
                        ]
                    
                    }
                ]              
            )
        logger.info(f"Successfully a created snapshot: {json.dumps(response, default=str)}")
    
    except Exception as e:
        logger.error(f"Error creating snapshot: {str(e)}")