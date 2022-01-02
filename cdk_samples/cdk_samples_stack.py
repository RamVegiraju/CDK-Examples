from aws_cdk import (
    core,
    aws_s3 as s3,
    aws_lambda as _lambda)


class CdkSamplesStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        #S3 Bucket
        #Create S3 bucket
        bucket = s3.Bucket(self, "ram-sample-bucket-cdk-demo-12345")

        #Lambda Function
        #Create Lambda function
        sample_lambda = _lambda.Function(self, "Ram-CDK-Function-One", #lambda function name
                                        handler="lambda_handler.handler", #function name as defined
                                        runtime=_lambda.Runtime.PYTHON_3_7, #runtime
                                        code=_lambda.Code.from_asset('cdk_samples/lambda')) #path to lambda handler
