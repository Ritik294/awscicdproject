from aws_cdk import (
    # Duration,
    Stack,
    App,
    pipelines
    
    # aws_sqs as sqs,
)

from constructs import Construct

class CicdpipelineStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        #AWS CICD
        cicd=modern_pipeline = pipelines.CodePipeline(self, "Pipeline",
    self_mutation=False,
    synth=pipelines.ShellStep("Synth",
        input=pipelines.CodePipelineSource.github("Ritik294/awscicdproject", "main" ),
        commands=["npm ci", "npm run build", "npx cdk synth"
        ]
    )
)
app =App()
CicdpipelineStack(app, "cicdstack")