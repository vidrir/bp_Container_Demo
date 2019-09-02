FROM alpine:latest
RUN apk add --update nginx
#FROM nginx:alpine

RUN mkdir -p /usr/share/nginx/html
RUN chown -R 0644 /usr/share/nginx/html
COPY index.html /usr/share/nginx/html/index.html

RUN mkdir -p /etc/nginx/sites/default
RUN chown -R 0644 /etc/nginx/sites/default
COPY nginx.conf /etc/nginx/sites/default/nginx.conf

# place file that will contain extra include stmts
COPY include.conf /etc/nginx/conf.d/include.conf

RUN mkdir -p /run/nginx
EXPOSE 8888
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]
