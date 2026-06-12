#!/bin/bash

certs=/home/zdb/Documents/'Public Certificates'

for f in $certs/*.cer; do
    base=$(basename "$f" .cer)
    certutil -A -n "$base" -t ",," -i "$f" -d sql:$HOME/.pki/nssdb
done
