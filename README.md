## Youtube-comment-count

### Requirements

You will need python3 installed and an [API key from google](https://developers.google.com/youtube/v3/getting-started). Once you get that key and have enabled the YouTube Data API v3, you need to store it into a file called `apikey.py` like so :

```python
api_key = 'YOUR_API_KEY'
```
 please note that this needs to be kept private. This is why `apikey.py` is listed in the `.gitignore` file.


### Usage
Using this little script, one can see the total number of comments left on a Youtube channel by specifying the channelId. For that, run 

`python allcomms.py CHANNEL_ID`

where `CHANNEL_ID` can be found [in your settings](https://support.google.com/youtube/answer/3250431) if you are the owner, or using the method(s) described on [this stackexchange question](https://stackoverflow.com/questions/14366648/how-can-i-get-a-channel-id-from-youtube).

