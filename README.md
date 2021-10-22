# discord-self-bot

Dependencies:
    Python3

This simple Python discord script (also called self-bot) is useful to send the same message all X milliseconds to a specific channel or conversation.<br/>
The message will be send as a user, not a bot.<br/>
Be aware : I personnaly don't recommand to submit milliseconds value under 1000 to avoid being blocked by discord.<br/>
You will need your private discord user token and the channel id. It's up to you to find it.<br/>

The user-agent used is Mozilla/5.0, it can be changed.<br/>

This script is functionnal with Discord v8 api.<br/>

Don't forget to add the right to execute this file with chmod command :

```chmod +x discord_self_bot.py```

USAGE:

```discord_self_bot.py [-h] [-ua USER_AGENT] -t TOKEN -m MESSAGE -s MILLISECONDS -c CHANNEL```

optional arguments:<br/>
  -h,                 --help                      => show this help message and exit<br/>
  -ua   USER_AGENT,   --user-agent USER_AGENT     => User agent used by the program, default value : Mozilla/5.0<br/>
  -t    TOKEN,        --token TOKEN               => Your discord user token, it's up to you to find it !<br/>
  -m    MESSAGE,      --message MESSAGE           => The message you want to post on the channel<br/>
  -ms   MILLISECONDS, --milliseconds MILLISECONDS => Time in milliseconds between each message (a good valud is 1000 for 1 second)<br/>
  -c    CHANNEL,      --channel CHANNEL           => Id of the discord channel / conversation, again, it's up to you to find it (google is your friend) !<br/>

I, Paul Surrans, am not responsable of any consequences using this script (please avoid to spam peoples or channels...).<br/>

Made with love by Paul Surrans, Student at Epitech Lille, France.<br/>

EXEMPLE:

I want to post 'Hello world !' message every hour on the channel 862054292999999916 with my token NPUwMzI2444444MzQ0Nzg1OTWm.YW3MfQ.xeFeixLOK99CydWfRXNBO5JtE0oNk :<br/>

```python3 discord_self_bot.py -t "NPUwMzI2444444MzQ0Nzg1OTWm.YW3MfQ.xeFeixLOK99CydWfRXNBO5JtE0oNk" -m "Hello world !" -s 3600 -c 862054292999999916```

License: MIT<br/>

*All credits goes to Kim Cho, c.f : [Quora topic](https://www.quora.com/I-want-to-automatically-post-a-message-every-24-hours-on-my-Discord-server-using-my-own-account-not-a-bot-account-Is-this-possible-and-if-so-how)*



