## Youtube-comment-count

### Requirements

You will need python3 installed and an [API key from google](https://developers.google.com/youtube/v3/getting-started). Once you get that key and have enabled the YouTube Data API v3, you need to store it into a file called `apikey.py` like so :

```python
api_key = 'YOUR_API_KEY'
```
 please note that this needs to be kept private. This is why `apikey.py` is listed in the `.gitignore` file.


### Usage
Using this little script, one can see the number of comments left on a Youtube video by specifying its videoId. For that, run 

`python comms.py VIDEO_ID`

where `VIDEO_ID` is obviously the Id of the video you want to fetch the number of comments from.

The `allcomms.py` file is not exactly finished yet but the plan is to add an option to fetch all the comments from a single channel.
