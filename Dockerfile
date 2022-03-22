FROM python:slim

ENV TECHLAND_AUTHZ_FLASK_ENV=production TECHLAND_AUTHZ_TIMEZONE=Asia/Tehran TECHLAND_AUTHZ_DATABASE_URI=NULL 

EXPOSE 8080/tcp

WORKDIR opt/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . . 

ARG GIT_COMMIT="nocommit"
ARG GIT_TAG="notag"
LABEL gitCommit=$GIT_COMMIT gitTag=$GIT_TAG

ENTRYPOINT ./start


