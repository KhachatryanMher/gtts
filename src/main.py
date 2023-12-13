from gtts import gTTS 

import os 

text = 'Hey there! Welcome back to another exciting episode. Are you feeling bored or just searching for some life hacks? Great! Let\'s dive in!'
lang = 'en'
  
gttsObject = gTTS(text, lang, slow=False)

gttsObject.save("gtts-version.mp3") 
  
os.system('mpg321 gtts-version.mp3') 