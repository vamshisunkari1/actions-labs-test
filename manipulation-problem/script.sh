#!/bin/bash

log_file="nginx.log"  


echo -e "\nUnique Request IPs:"
awk '{print $1}' $log_file | sort | uniq

echo -e "\nCount of HTTP 200 Success Codes:"
awk '$9 == 200' $log_file | wc -l

echo -e "\nCount of HTTP 304 Codes:"
awk '$9 == 304' $log_file | wc -l
