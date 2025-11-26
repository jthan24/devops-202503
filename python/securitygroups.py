from instancia import get_aws_session

def get_default_securitygroup(ec2_resource):
    for sg in ec2_resource.security_groups.limit(10):
        print(f"{sg.id}: {sg.group_name}")


if __name__ == "__main__":
    session = get_aws_session()
    ec2_resource = session.resource("ec2")
    get_default_securitygroup(ec2_resource)