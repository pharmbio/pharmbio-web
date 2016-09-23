FROM nginx
# Loosely based on this link:
# https://github.com/kstaken/dockerfile-examples/blob/master/apache/Dockerfile
# (Thx, Kimbro Staken)

MAINTAINER Samuel Lampa <samuel.lampa@farmbio.uu.se>
COPY public /usr/share/nginx/html
