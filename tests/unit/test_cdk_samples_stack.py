import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_samples.cdk_samples_stack import CdkSamplesStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_samples/cdk_samples_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkSamplesStack(app, "cdk-samples")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
