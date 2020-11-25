# zoom-recordings-downloader
Zoom cloud recordings downloader. This simple application fetches all the cloud recordings (video, audio and chats) from your Zoom account and stores them locally. 

# Configuration

First, install dockers support for you operation system: https://www.docker.com/

Second, register JWT application in Zoom marketplace. Instructions: https://marketplace.zoom.us/docs/guides/build/jwt-app

Third, create **.env** file with variables ZOOM_API_KEY and ZOOM_API_SECRET. Copy JWT app credentials to these variables.
PLace this file to the same directory with run.sh and run.command scripts.

# Running

You can run the downloader using either **run.sh** or **run.command** (MacOS).

Both commands pull the latest **zoom-recordings-downloader** image from Docker hub and run it.

All the recordings available in your Zoom will be downloaded and written to the directory __zoom_recordings__ created in the directory where run script is located. This downloader does not monitor for new recordings available for download and exits after downloading all files. If the file had been downloaded it is not downloaded again.

Download progress bar is shown.
