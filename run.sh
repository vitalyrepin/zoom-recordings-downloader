#!/bin/sh

TAG=latest

docker run -it --rm --name zoom-import -v "$PWD":/usr/src/myapp -w /usr/src/myapp --env-file .env vitalyrepin/zoom-recordings-downloader:${TAG}
