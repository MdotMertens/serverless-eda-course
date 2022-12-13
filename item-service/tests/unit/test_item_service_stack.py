import aws_cdk as core
import aws_cdk.assertions as assertions

from item_service.item_service_stack import ItemServiceStack

# example tests. To run these tests, uncomment this file along with the example
# resource in item_service/item_service_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ItemServiceStack(app, "item-service")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
