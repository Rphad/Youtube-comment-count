# Youtube-comment-count

## Français [EN below]

### Prérequis

Ce script nécessite python3 et une [clé API de Google](https://developers.google.com/youtube/v3). Une fois que vous avez une clé et activé YouTube Data API v3, il faut la stocker dans un fichier appelé `apikey.py` comme suit:

```python
api_key = 'VOTRE_CLE_API'
```

notez qu'elle doit être gardée secrète, d'où l'inclusion de `apikey.py` dans le `.gitignore`.


### Utilisation

Ce script permet de déterminer le nombre de commentaires total qu'a reçu une chaîne Youtube, en spécifiant son identifiant (channelId). Pour cela, il faut exécuter la commande suivante dans un terminal:

`python allcomms.py ID_CHAINE`

où `ID_CHAINE` peut être trouvé [dans vos paramètres](https://support.google.com/youtube/answer/3250431?hl=fr) si vous êtes le propriétaire de la chaîne, ou en utilisant les méthodes décrites [dans cette question stackexchange (en anglais)](https://stackoverflow.com/questions/14366648/how-can-i-get-a-channel-id-from-youtube)

## English

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

