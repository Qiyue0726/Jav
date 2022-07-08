FROM python:3.8-slim

MAINTAINER sakura

COPY ./ /Jav/

WORKDIR /Jav

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple beautifulsoup4 \
    requests lxml Django django-cors-headers django-rest-framework

EXPOSE 8080

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
