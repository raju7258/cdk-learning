from aws_cdk import (
    # Duration,
    Stack,
    RemovalPolicy,
    Tags,
    CfnOutput,
    # aws_sqs as sqs,
    aws_s3 as s3,
)
from constructs import Construct

class Project1Stack(Stack):

    def __init__(self, scope: Construct, construct_id, *, stage : str = "dev", **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "Project1Queue",
        #     visibility_timeout=Duration.seconds(300),
        # )
        bucket = s3.Bucket(
                self, "DevBucketT",
                versioned=False,
                block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
                encryption=s3.BucketEncryption.S3_MANAGED,
                removal_policy=RemovalPolicy.DESTROY,
                auto_delete_objects=True,
        )

        Tags.of(self).add("env", stage)
        Tags.of(self).add("app", "cdk-dev-bucket")
        CfnOutput(self, "BucketName", value=bucket.bucket_name)
        CfnOutput(self, "BucketARN", value=bucket.bucket_arn)
