podman run -d \
  --name=nginx \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -p 8080:80 \
  -v /run/media/emil/e9bc19c3-707a-4d06-965d-67359bd2c4c6/orkened/content:/config \
  --restart unless-stopped \
  ghcr.io/linuxserver/nginx
