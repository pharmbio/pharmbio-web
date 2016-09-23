FROM ubuntu:16.04
# Loosely based on this link:
# https://github.com/kstaken/dockerfile-examples/blob/master/apache/Dockerfile
# (Thx, Kimbro Staken)

MAINTAINER Samuel Lampa <samuel.lampa@farmbio.uu.se>

RUN apt-get update && apt-get install -y apache2 && apt-get clean

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2

EXPOSE 80

CMD ["/usr/sbin/apache2", "-D", "FOREGROUND"]

ADD public/* /var/www/html/
