# Errbot test playground

This is my errbot test playground

## How to get it running

    git clone https://github.com/VerosK/errbot-playground
    cd errbot-playground

Setup the plugins

    pipenv install 

Setup the plugins

    cp -v environment.sample environment


## Start errbot in text mode 
  
Start the errbot in test text mode

    errbot -T

## Connect errbot

You should provide config in `config.py` or in `environment` file. 
After updating configuration just run
 
    errbot

## Play with the plugins

Errbot contains some basic plugins, some plugins are added to this installation.

Some basic commands

  * `!ping`   - returns `pong`

  * `!whoami` 

  * `!help`  - returns help 

  * Try to mention Chuck Noris. The bot should reply with Chuck Norris joke.

  * `!restore` - flow example

You can send the commands to the bot directly (without `!` prefix). You can also send the room
which the bot listens to - you should use the `!` prefix then.


## License

Errbot itself is under GPL3 license, this repository is under CC0.
