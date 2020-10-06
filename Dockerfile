FROM ubuntu:latest
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
    && apt-get install tesseract-ocr -y \
    python3 \
    python3-pip \
    && apt-get clean \
    && apt-get autoremove

ADD . /project
WORKDIR /project

RUN pip3 install -r requirements.txt

CMD ["python3","transcribe.py"]

EXPOSE 5000
