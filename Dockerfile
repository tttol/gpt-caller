FROM public.ecr.aws/lambda/python:3.8

COPY . /var/task

CMD ["app.lambda_handler"]
