### base image
FROM python:3.9-slim-buster AS compile-image


### install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc


### virtualenv
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"


### add and install requirements
RUN pip install pip-tools
COPY ./requirements.in .
RUN pip-compile requirements.in > requirements.txt && pip-sync
RUN pip install -r requirements.txt



## build image
FROM python:3.9-slim-buster AS runtime-image


### install nc
RUN apt-get update && \
    apt-get install -y --no-install-recommends netcat-openbsd


### copy Python dependencies from build image
COPY --from=compile-image /opt/venv /opt/venv


### set working directory
WORKDIR /usr/src/app


### add user
RUN addgroup --system user && adduser --system --no-create-home --group user
RUN chown -R user:user /usr/src/app && chmod -R 755 /usr/src/app


### switch to non-root user
USER user


### add app
COPY . /usr/src/app/


### set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
ENV PATH="/opt/venv/bin:$PATH"

### run the app
CMD python publisher.py