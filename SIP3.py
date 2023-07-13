#!/usr/bin/env python
# coding: utf-8

# In[10]:


from pydub import AudioSegment
from pydub.playback import play
 
# Read in audio file
AUDIO_FILENAME = 'sip_lab2.wav'
audio = AudioSegment.from_wav(AUDIO_FILENAME)
 
# Define start and end times of segment to play
start_time = 3000  # in milliseconds
end_time = 11000  # in milliseconds
 
# Extract segment of audio to play
segment = audio[start_time:end_time]
 
# Play audio segment
play(segment)


# In[3]:


get_ipython().run_line_magic('pip', 'install pydub')


# In[17]:


from pydub import AudioSegment
sound = AudioSegment.from_file('sip_lab2.wav')

def speed_change(sound, speed=1.0):
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * speed)
    })

    # convert the sound with altered frame rate to a standard frame rate
    # so that regular playback programs will work right. They often only
    # know how to play audio at standard frame rate (like 44.1k)
    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)

slow_sound = speed_change(sound, 0.7)
fast_sound = speed_change(sound, 1.8)

play(slow_sound)


# In[15]:


play(fast_sound)


# In[ ]:




