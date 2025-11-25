from dotenv import load_dotenv
import boto3
import os

load_dotenv()

session = boto3.Session(
    aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name = os.getenv("AWS_REGION")
)


## client mode, more detailed
ec2_serv = session.client("ec2")

desc_instances = ec2_serv.describe_instances() 

for reserv in desc_instances["Reservations"]:
    for inst in reserv["Instances"]:
        #print(inst)
        id = inst["InstanceId"]
        state = inst["State"]["Name"]
        operationSystem = inst["PlatformDetails"]
        print("instance:", id , f"is in state: {state}", f" OS : {operationSystem}")
## in this mode we can extract more details about the instances
## like tags.