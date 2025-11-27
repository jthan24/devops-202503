import boto3

def get_instance_name(instance):
    if instance.tags:
        for tag in instance.tags:
            if tag['Key'] == 'Name':
                return tag['Value']
    # Devuelve un valor por defecto si la etiqueta 'Name' no existe
    return "(Sin Nombre Definido)"

def list_all_instances(ec2_resource):
    for instance in ec2_resource.instances.all():
        instance_name = get_instance_name(instance)
        print(f"{instance.id}: {instance_name}")

if __name__ == "__main__":
    ec2_resource = boto3.resource("ec2", region_name='us-east-1')
    list_all_instances(ec2_resource)