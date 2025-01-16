FROM ubuntu:20.04

RUN apt update && \
    apt install -y \
    curl \
    gnupg2 \
    ca-certificates \
    lsb-release \
    ubuntu-keyring && \
    curl https://nginx.org/keys/nginx_signing.key | gpg --dearmor | tee /usr/share/keyrings/nginx-archive-keyring.gpg >/dev/null && \
    echo "deb [signed-by=/usr/share/keyrings/nginx-archive-keyring.gpg] http://nginx.org/packages/mainline/ubuntu `lsb_release -cs` nginx" | tee /etc/apt/sources.list.d/nginx.list && \
    apt update && \
    apt install -y nginx=1.19.0-1~focal && \
    apt-get purge -y --auto-remove curl gnupg lsb-release && \
    rm -rf /var/lib/apt/lists/*

COPY default.conf /etc/nginx/conf.d/default.conf

CMD ["nginx", "-g", "daemon off;"]
