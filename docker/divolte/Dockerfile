FROM ubuntu:16.04

WORKDIR /opt/app

RUN apt-get update && \
    apt-get install -y curl default-jre && \
    curl -O http://divolte-releases.s3-website-eu-west-1.amazonaws.com/divolte-collector/0.8.0/distributions/divolte-collector-0.8.0.tar.gz && \
    tar zxpf divolte-collector-0.8.0.tar.gz -C /opt/app/ && \
    rm -rf /opt/app/divolte-collector-0.8.0/conf && \
    mv /opt/app/divolte-collector-0.8.0/ /opt/app/divolte-collector/ && \
    rm -rf /var/tmp/* /tmp/* /opt/app/divolte-collector-0.8.0/