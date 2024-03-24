FROM public.ecr.aws/lambda/python:3.10

COPY requirements.txt ${LAMBDA_TASK_ROOT}

RUN pip install -r requirements.txt

COPY src/ ${LAMBDA_TASK_ROOT}/src
COPY handler.py ${LAMBDA_TASK_ROOT}

CMD [ "handler.handler" ]
