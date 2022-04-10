# Game-of-Life
A game of life "simulator" built to identify sequences of patterns.

## Usage
Currently not very user friendly I'm afraid... When the files are downloaded, run "Game_of_life_main.py". The program will ask the user to choose setup configuration. Enter "standard". The "Manual" option is supposed to let the user specify canvas size, number of squares etc, but it currently suffers from a bug where the program won't accept any format of canvas size specification.

## Additional feature: Trimming
The program includes the module "Field_operator.py" that can "trim"/remove certain specified patterns. Currently these are the Square, Beehive and Boat. The purpose of this is to limit these patterns ability to break up and destroy sequences of patterns that the user wants to study.
