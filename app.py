#!/usr/bin/env python3
import os

from aws_cdk import (
    # Duration,
    Stack,
    aws_ec2 as ec2,
    App,
    Environment
    # aws_sqs as sqs,
)

from cicdpipeline.cicdpipeline_stack import CicdpipelineStack


app = App()
env = Environment(account='851725621998', region='us-east-1')
CicdpipelineStack(app, "CicdpipelineStack",
   env=env
    )

app.synth()
