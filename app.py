#!/usr/bin/env python3
import os

from aws_cdk import (
    # Duration,
    Stack,
    aws_ec2 as ec2,
    App
    # aws_sqs as sqs,
)

from cicdpipeline.cicdpipeline_stack import CicdpipelineStack


app = cdk.App()
CicdpipelineStack(app, "CicdpipelineStack",
   env='851725621998',region='us-east-1'
    )

app.synth()
