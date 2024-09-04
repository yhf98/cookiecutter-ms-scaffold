FROM python:3.10

COPY ./requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

WORKDIR /app

COPY ./apps /app/apps
COPY ./application /app/application
COPY ./core /app/core
COPY ./db /app/db
COPY ./scripts /app/scripts
COPY ./static /app/static
COPY ./utils /app/utils
COPY ./main.py /app/main.py

CMD ["python", "main.py", "{{cookiecutter.repo_port}}"]
