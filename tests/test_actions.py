import pytest

from awsmanifest import AwsManifest, manifest

@pytest.fixture(params=[False, True], scope="function")
def local(request):
    return request.param

def test_all(local):
    a = AwsManifest(local=local)
    test_svcs = ["Amazon EC2", "Amazon Comprehend"]

    svcs = a.services()
    assert all([svc in svcs for svc in test_svcs])

    prefixes = a.service_prefixes()
    assert all([prefix in prefixes for prefix in ["ec2", "comprehend", "s3"]])

    assert a.actions("Amazon EC2") == a.actions("ec2")
    assert "DescribeVolumes" in a.actions("Amazon EC2")
    assert a.actions("Amazon S3") == a.actions("s3")
    assert "PutObject" in a.actions("s3")

    svc_map = manifest(local=local)
    assert all([svc in svc_map["serviceMap"] for svc in test_svcs])