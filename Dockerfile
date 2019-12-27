# use base python image with python 3.6.5
FROM python:3.6.5

# set working directory to /app/
WORKDIR /app/
# create log directory
RUN mkdir -p /log

# add requirements.txt to the image
ADD requirements.txt /app/requirements.txt

# install python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# create unprivileged user
# RUN adduser --disabled-password --gecos '' myuser
#
CMD python wechat.py
