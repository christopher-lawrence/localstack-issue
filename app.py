#!/usr/bin/env python3

import aws_cdk as cdk

from localstack_issue.localstack_issue_stack import LocalstackIssueStack


app = cdk.App()
LocalstackIssueStack(app, "localstack-issue")

app.synth()
