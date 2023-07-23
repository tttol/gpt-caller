FROM public.ecr.aws/lambda/python:3.10

COPY . /var/task

CMD ["app.lambda_handler"]
