from aws_cdk import (
   aws_lambda as _lambda,
    aws_apigateway as api,
    core
)


class CdkworkshopStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.lambdaStack=_lambda.Function(
            self,'Handler',runtime=_lambda.Runtime.PYTHON_3_6,
            code=_lambda.Code.asset('lambda'),
            handler='lambda_function.lambda_handler'
        )
        self.api_g=api.LambdaRestApi(
            self,'Endpoint',handler=self.lambdaStack
        )

