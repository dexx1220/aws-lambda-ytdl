import youtube_dl
import json

def generateLink(event, context):
  opts = {'simulate': True, 'forceurl': True, 'quiet': True}
  body = json.loads(event["body"])
  url = body["videoUrl"]

  with youtube_dl.YoutubeDL(opts) as ydl:
    result = ydl.extract_info(url, False)
  
  response = {
    "statusCode": 200,
    "body": json.dumps(result)
  }

  return response
