#!/bin/bash

TAG=1.0

docker build -t vitalyrepin/zoom-recordings-downloader .
docker tag vitalyrepin/zoom-recordings-downloader vitalyrepin/zoom-recordings-downloader:${TAG}
