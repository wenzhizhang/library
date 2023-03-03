FROM python:3.8.0
ENV PYTHONUNBUFFERED=1

# install nginx
RUN export HTTP_PROXY=http://10.144.1.10:8080 HTTPS_PROXY=http://10.144.1.10:8080 http_proxy=http://10.144.1.10:8080 https_proxy=http://10.144.1.10:8080 \
    && apt-get clean && apt-get update && apt-get install nginx vim -y --no-install-recommends \
    && unset HTTP_PROXY HTTPS_PROXY http_proxy https_proxy
COPY study/config/nginx_docker.conf /etc/nginx/sites-enabled/study.conf
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

# copy source and install dependencies
RUN mkdir -p /opt/library
RUN mkdir -p /opt/library/pip_cache
RUN mkdir -p /opt/library/study
COPY requirements.txt start-server.sh /opt/library/
COPY study /opt/library/study/
WORKDIR /opt/library
RUN export HTTP_PROXY=http://10.144.1.10:8080 HTTPS_PROXY=http://10.144.1.10:8080 http_proxy=http://10.144.1.10:8080 https_proxy=http://10.144.1.10:8080 \
    && pip install -r requirements.txt --cache-dir /opt/library/pip_cache \
    && unset HTTP_PROXY HTTPS_PROXY http_proxy https_proxy
RUN chown -R www-data:www-data /opt/library

# Start server
EXPOSE 8080
EXPOSE 8443
STOPSIGNAL SIGTERM
RUN nginx -t
RUN service nginx start
CMD ["/opt/library/start-server.sh"]