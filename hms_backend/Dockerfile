FROM python:3.9.7

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app
RUN apt-get update -yqq && apt-get upgrade -yqq && apt-get install -y --no-install-recommends && apt-get install -y locales

COPY requirements.txt /usr/src/app
RUN python3 -m pip install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

RUN echo "LC_ALL=en_US.UTF-8" >> /etc/environment
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
RUN echo "LANG=en_US.UTF-8" > /etc/locale.conf
RUN locale-gen en_US.UTF-8
RUN update-locale LANG=en_US.UTF-8 LC_MESSAGES=POSIX

COPY . /usr/src/app
EXPOSE 8000