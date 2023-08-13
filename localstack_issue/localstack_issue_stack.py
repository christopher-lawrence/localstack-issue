from constructs import Construct
from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
)

class LocalstackIssueStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        my_lambda = _lambda.DockerImageFunction(self, 'HelloHandler',
                code = _lambda.DockerImageCode.from_image_asset('./lambda'),
        )

        # apigw.LambdaRestApi(
        #     self, 'Endpoint',
        #     handler=my_lambda
        # )

