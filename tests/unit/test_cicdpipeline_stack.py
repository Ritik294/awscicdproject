import aws_cdk as core
import aws_cdk.assertions as assertions

from cicdpipeline.cicdpipeline_stack import CicdpipelineStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cicdpipeline/cicdpipeline_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CicdpipelineStack(app, "cicdpipeline")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
