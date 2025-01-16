# Dockerfile for nginx 1.19:

Created a Dockerfile , you can get file inside `nginx-dockerfile` folder
Used base image is `ubuntu:20.04`

used this site to download nginx packages 

Ref[https://nginx.org/en/linux_packages.html#Ubuntu]

Note:                        
  Added default.conf .because after building i tested container , no logs are showed , so i added that file to replace default one

**Security test**

Used trivy tool to test the image

