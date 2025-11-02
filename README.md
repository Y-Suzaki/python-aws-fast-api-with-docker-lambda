# python-aws-fast-api-with-docker-lambda
## Technical Stack
* AWS Resource
    * APIGateway
    * Lambda (Docker runtime)
    * [Lambda Web Adapter](https://github.com/awslabs/aws-lambda-web-adapter)
* CI/CD
    * AWS SAM 
* Python
    * Python 3.12 
    * Fast API 

## Build Steps
1. sam build
    ```
    REPOSITORY                                  TAG             IMAGE ID       CREATED          SIZE
    fastapifunction                             python3.12-v1   f3ca9a90268f   35 seconds ago   155MB
    public.ecr.aws/docker/library/python        3.12-slim       324231aabbd8   3 weeks ago      119MB
    public.ecr.aws/awsguru/aws-lambda-adapter   0.9.1           5fbdb541b887   6 months ago     3.57MB
    ```
2. sam validate
3. sam deploy
    * CloudFormation Stacks that are created.
        1. aws-sam-cli-managed-default
            * s3 bucket, Bucket policy
        2. fastapi-with-lambda-docker-runtime-stack-c5e55a3e-CompanionStack
            * ECR repository
        3. fastapi-with-lambda-docker-runtime-stack
