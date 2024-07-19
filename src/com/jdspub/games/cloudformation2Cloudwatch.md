To make Amazon CloudWatch report CloudFormation events, you can use CloudWatch Events and create a rule that captures CloudFormation events. Here are the steps to set this up: [1]

Open the AWS CloudWatch console.

In the navigation pane, under "Events", choose "Rules".

Click "Create rule".

Under "Event Source", choose "AWS services" and then select "CloudFormation" from the list of services. [2]

Under "Event Type", select the specific CloudFormation events you want to capture. For example, you can choose "AWS CloudFormation Stack Status-change Notification" to capture all stack status changes.

Click "Next".

Under "Targets", choose the target where you want to send the CloudFormation events. You can choose from various targets like Amazon SNS, AWS Lambda, Amazon SQS, etc.

Configure the target as per your requirements.

Click "Next".

Review the rule details and click "Create rule".

Once the rule is created, CloudWatch Events will capture the specified CloudFormation events and send them to the target you configured.

Alternatively, you can also create the CloudWatch Events rule using AWS CloudFormation. Here's an example CloudFormation template that creates a CloudWatch Events rule to capture CloudFormation stack status changes and send them to an SNS topic: [3]

Resources:
  CloudFormationEventRule:
    Type: AWS::Events::Rule
    Properties:
      Description: Capture CloudFormation stack status changes
      EventPattern:
        source:
          - aws.cloudformation
        detail-type:
          - CloudFormation Stack Status-change Notification
        detail:
          StackStatus:
            - CREATE_IN_PROGRESS
            - CREATE_FAILED
            - CREATE_COMPLETE
            - DELETE_IN_PROGRESS
            - DELETE_FAILED
            - DELETE_COMPLETE
            - UPDATE_IN_PROGRESS
            - UPDATE_COMPLETE_CLEANUP_IN_PROGRESS
            - UPDATE_COMPLETE
            - UPDATE_ROLLBACK_IN_PROGRESS
            - UPDATE_ROLLBACK_FAILED
            - UPDATE_ROLLBACK_COMPLETE
            - REVIEW_IN_PROGRESS
      State: ENABLED
      Targets:
        - Arn: !Ref CloudFormationEventTopic
          Id: CloudFormationEventTarget

  CloudFormationEventTopic:
    Type: AWS::SNS::Topic
    Properties:
      TopicName: CloudFormationEvents

Copy

Insert at cursor
yaml
