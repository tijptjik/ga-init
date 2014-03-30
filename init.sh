#!/bin/bash
# Bootstrapping GA Initialiser
# 
# Example Usage : 
# 
# \curl -sSL ga.co/install > GA && sh GA install FEWD HK 5

echo "Running GA Initialiser"

mkdir -p /tmp/ga-init/payload
curl localhost:8000/payload.tar > /tmp/ga-init/payload.tar
tar xf /tmp/ga-init/payload.tar -C /tmp/ga-init/payload
# python /tmp/ga-init/payload/init/init.py
python ./init.py "$@"
rm GA