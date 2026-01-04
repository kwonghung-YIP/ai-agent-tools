#!/bin/bash

#Update ens33 with your primary NIC
export VM_IP_ADDRESS=$(/sbin/ip -o -4 addr list ens33 | awk '{print $4}' | cut -d/ -f1)
echo $VM_IP_ADDRESS
docker compose up