#!/bin/sh

KEYPASS=`echo $$RANDOM | md5sum | head -c 20`
rm n8n*

# generate new private key (n8n.key) and cert request file (n8n.csr)
openssl req \
    -newkey rsa:2048 -noenc -keyout n8n.key \
    -out n8n.csr -config request.config
    
# sign the request and generate the cert file
openssl x509 \
    -signkey n8n.key \
    -in n8n.csr -req -days 30 -out n8n.crt

openssl x509 -in n8n.crt -text

echo $KEYPASS
