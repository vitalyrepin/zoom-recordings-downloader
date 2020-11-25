#!/usr/bin/python3

import os
import humanize
from pyzoom import ZoomClient
import requests
import progressbar

def download_zoom_file(zoomClient, url, fname, fsize):
    # Display download progress
    widgets = [
        '\x1b[33mDownloading\x1b[39m',
        progressbar.Percentage(),
        progressbar.Bar(marker='\x1b[32m#\x1b[39m'),
    ]
    bar = progressbar.ProgressBar(widgets=widgets, max_value=fsize).start()

    params = {
           'access_token': zoomClient.raw.bearer_token()

    }
    # NOTE the stream=True parameter below
    sz = 0
    with requests.get(url, stream=True, params=params) as r:
        r.raise_for_status()
        with open(fname, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                sz += 8192
                if(sz>fsize):
                  sz = fsize
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk:
                f.write(chunk)
                bar.update(sz)

    bar.finish()


video_zoom_dir = '/usr/src/myapp/zoom-videos'

print ('Starting video import')

# Set ZOOM_API_KEY and ZOOM_API_SECRET in the .env file
client = ZoomClient.from_environment()

# 1: Getting user ids
r = client.raw.get('/users')
user_ids = []
for user in r.json()['users']:
  print (user)
  user_ids.append([ user['id'], user['email'] ] )

print(user_ids)

# 2: Getting cloud recordings
for user in user_ids:
  user_email = user[1]
  user_id = user[0]

  out_user_dir = os.path.join(video_zoom_dir, user_email.replace('@', '-'))
  body = {
           'from': '2020-11-01'
         }
  r = client.raw.get('/users/%s/recordings' % (user_id), query=body)
  for meeting in r.json()['meetings']:
    # Creating directory to store downloaded video
    out_dir = os.path.join(out_user_dir, meeting['topic'])
    os.makedirs(out_dir, exist_ok = True)

    print('Processing recordings for the meeting %s' % (meeting['topic']))
    for rec in meeting['recording_files']:
      file_path = os.path.join(out_dir, rec['recording_start'] + '-' + rec['recording_end'] + '.' + rec['file_type'])
      if(os.path.isfile(file_path)):
        print('File %s is already downloaded' % (file_path))
      else:
        print('Storing %s of size %s at %s' % (rec['download_url'], humanize.naturalsize(rec['file_size']), file_path))
        download_zoom_file(client, rec['download_url'], file_path, rec['file_size'])

