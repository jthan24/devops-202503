from instancia import get_aws_session

def terminate_instance(ec2_client):
    response = ec2_client.terminate_instances(
        InstanceIds=[
            'i-096e48aaf417dfe05', ### Change here the InstanceID
        ],
        DryRun=False
    )

    print(response)


if __name__ == "__main__":
    session = get_aws_session()
    ec2_client = session.client("ec2")
    terminate_instance(ec2_client)
