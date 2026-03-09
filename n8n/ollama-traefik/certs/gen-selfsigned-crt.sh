#!/bin/sh

KEYPASS=`echo $$RANDOM | md5sum | head -c 20`
rm traefik*

# generate new private key (n8n.key) and cert request file (n8n.csr)
openssl req \
    -newkey rsa:2048 -noenc -keyout traefik.key \
    -out traefik.csr -config request.config
    
# sign the request and generate the cert file
openssl x509 \
    -signkey traefik.key \
    -in traefik.csr -req -days 30 -out traefik.crt

openssl x509 -in traefik.crt -text

echo $KEYPASS
