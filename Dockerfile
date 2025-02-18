FROM ubuntu:latest

# Install required dependencies
RUN apt-get update && apt-get install -y \
    curl \
    gnupg2 \
    python3 \
    software-properties-common

# Install specific chrome version
RUN apt-get -y install wget
ENV CHROME_VERSION=122.0.6261.128-1
RUN wget -q https://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_${CHROME_VERSION}_amd64.deb
RUN apt-get -y update
RUN apt-get install -y ./google-chrome-stable_${CHROME_VERSION}_amd64.deb
RUN apt-get install -y x11vnc xvfb
RUN mkdir ~/.vnc
RUN x11vnc -storepasswd 1234 ~/.vnc/passwd

# Copy code
COPY . /app
WORKDIR /app

ENV DISPLAY=:99

