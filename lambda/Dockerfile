FROM public.ecr.aws/lambda/python:3.8

RUN yum -y update && yum -y install libsndfile

# RUN curl -O https://lambda-insights-extension.s3-ap-northeast-1.amazonaws.com/amazon_linux/lambda-insights-extension.rpm
# RUN rpm -U lambda-insights-extension.rpm

# Copy function code
COPY ./hello.py ./

CMD [ "hello.handler" ]        
