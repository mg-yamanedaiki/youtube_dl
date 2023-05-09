FROM python:3.9.16-bullseye

WORKDIR /root/app
RUN apt update && \
    apt upgrade -y && \
    apt install -y \
    ffmpeg \
    git


RUN pip install --upgrade pip && pip install yt-dlp