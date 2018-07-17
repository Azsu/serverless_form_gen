import boto3

class cloudformation:
    def create_stack(self):
        response = client.create_stack(
            StackName='string',
            TemplateBody='string',
            TemplateURL='string',
            Parameters=[
                {
                    'ParameterKey': 'string',
                    'ParameterValue': 'string',
                    'UsePreviousValue': True | False,
                    'ResolvedValue': 'string'
                },
            ],
            DisableRollback=True | False,
            RollbackConfiguration={
                'RollbackTriggers': [
                    {
                        'Arn': 'string',
                        'Type': 'string'
                    },
                ],
                'MonitoringTimeInMinutes': 123
            },
            TimeoutInMinutes=123,
            NotificationARNs=[
                'string',
            ],
            Capabilities=[
                'CAPABILITY_IAM' | 'CAPABILITY_NAMED_IAM',
            ],
            ResourceTypes=[
                'string',
            ],
            RoleARN='string',
            OnFailure='DO_NOTHING' | 'ROLLBACK' | 'DELETE',
            StackPolicyBody='string',
            StackPolicyURL='string',
            Tags=[
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            ClientRequestToken='string',
            EnableTerminationProtection=True | False
        )


def main():
    client = boto3.client('cloudformation')

if __name__ == "__main__":
    main()
