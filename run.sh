#!/bin/sh

TAG=latest

docker run -it --rm --name zoom-import -v "$PWD":/var/spool/zoom-downloader-out -w /var/spool/zoom-downloader-out --env-file .env vitalyrepin/zoom-recordings-downloader:${TAG}
