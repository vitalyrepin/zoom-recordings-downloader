FROM python:3

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt && \
    rm -f requirements.txt
RUN mkdir -p /var/spool/zoom-downloader-out

COPY zoom-downloader.py /

CMD [ "python", "/zoom-downloader.py" ]
