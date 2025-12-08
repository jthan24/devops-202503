import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_instances()

# Count instances
instance_count = sum(
    len(reservation.get('Instances', []))
    for reservation in response.get('Reservations', [])
)

print(f"EC2 Instances: {instance_count} instances")
print("=" * 50)

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        instance_type = instance['InstanceType']
        state = instance['State']['Name']

        # Get public IP if available
        public_ip = instance.get('PublicIpAddress', 'N/A')

        # Get private IP if available
        private_ip = instance.get('PrivateIpAddress', 'N/A')

        # Get name tag if available
        name = 'N/A'
        for tag in instance.get('Tags', []):
            if tag['Key'] == 'Name':
                name = tag['Value']
                break

        print(f"ID: {instance_id}")
        print(f"Name: {name}")
        print(f"Type: {instance_type}")
        print(f"State: {state}")
        print(f"Public IP: {public_ip}")
        print(f"Private IP: {private_ip}")
        print("-" * 30)
