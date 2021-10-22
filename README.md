# discord-self-bot

Dependencies:
    Python3

This simple Python discord script (also called self-bot) is useful to send the same message all X seconds to a specific channel.
The message will be send as a user, not a bot.
You will need your private discord user token and the channel id. It's up to you to find it.

The user-agent used is Mozilla/5.0, it can be changed.

This script is functionnal with Discord v8 api.

Don't forget to add the right to execute this file with chmod command :

```chmod +x discord_self_bot.py```

USAGE:

```discord_self_bot.py [-h] [-ua USER_AGENT] -t TOKEN -m MESSAGE -s SECONDS -c CHANNEL

optional arguments:
  -h, --help            show this help message and exit
  -ua USER_AGENT, --user-agent USER_AGENT
                        User agent used by the program, default value : Mozilla/5.0
  -t TOKEN, --token TOKEN
                        Your discord user token, it's up to you to find it !
  -m MESSAGE, --message MESSAGE
                        The message you want to post on the channel
  -s SECONDS, --seconds SECONDS
                        Your discord unique token, it's up to you to find it (google is your friend) !
  -c CHANNEL, --channel CHANNEL```

I, Paul Surrans, am not responsable of any consequences using this script.

Made with love by Paul Surrans, Student at Epitech Lille, France.

EXEMPLE:

I want to post 'Hello world !' message every hour on the channel 862054292999999916 with my token NPUwMzI2444444MzQ0Nzg1OTWm.YW3MfQ.xeFeixLOK99CydWfRXNBO5JtE0oNk :

```python3 discord_self_bot.py -t "NPUwMzI2444444MzQ0Nzg1OTWm.YW3MfQ.xeFeixLOK99CydWfRXNBO5JtE0oNk" -m "Hello world !" -s 3600 -c 862054292999999916```

License: MIT

*All credits goes to Kim Cho, c.f :
[Quora topic](https://www.quora.com/I-want-to-automatically-post-a-message-every-24-hours-on-my-Discord-server-using-my-own-account-not-a-bot-account-Is-this-possible-and-if-so-how)*



