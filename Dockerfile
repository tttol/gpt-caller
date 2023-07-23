FROM public.ecr.aws/lambda/python:3.10

COPY . /var/task

RUN pip install -r requirements.txt

CMD ["app.lambda_handler"]
