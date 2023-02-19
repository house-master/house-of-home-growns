FROM nginx:alpine

RUN rm /etc/nginx/conf.d/*.conf
COPY ./nginx/ui.conf /etc/nginx/conf.d

ADD frontend/build /usr/share/nginx/html/
ADD frontend/build /var/www/html/