from dotenv import load_dotenv
import boto3
import os

# Cargar variables del archivo .env
load_dotenv()

# Crear sesión boto3
session = boto3.Session(
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION")
)

# Cliente EC2
ec2 = session.client("ec2")

# Obtener instancias
response = ec2.describe_instances()

print("\n=== LISTADO DE INSTANCIAS EC2 ===\n")

for reservation in response.get("Reservations", []):
    for instance in reservation.get("Instances", []):

        instance_id = instance.get("InstanceId", "N/A")
        instance_type = instance.get("InstanceType", "N/A")
        private_ip = instance.get("PrivateIpAddress", "N/A")
        state = instance.get("State", {}).get("Name", "N/A")
        platform = instance.get("PlatformDetails", "N/A")

        # Obtener etiqueta Name
        instance_name = "N/A"
        if "Tags" in instance:
            for tag in instance["Tags"]:
                if tag["Key"].lower() == "name":
                    instance_name = tag["Value"]

        # Obtener rol de instancia (IAM Instance Profile)
        iam_role = "N/A"
        if "IamInstanceProfile" in instance:
            iam_role = instance["IamInstanceProfile"].get("Arn", "N/A")

        print(f"""
-------------------------------------------------
Instance ID       : {instance_id}
Instance Name     : {instance_name}
Instance Type     : {instance_type}
Private IP        : {private_ip}
State             : {state}
OS / Platform     : {platform}
IAM Role          : {iam_role}
-------------------------------------------------
""")


