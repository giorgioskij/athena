# Athena



Athena, which happens to be the name of my computer, is a vocal assistant project that I have been fiddling around for quite some time.

It is meant to run in the background as a daemon, so it detaches from the terminal when launched and closes the stdin, stdout and stderr streams.

You can monitor it through the log file located in `temp/output.txt`

It uses [Snowboy](https://github.com/Kitt-AI/snowboy) as a Hotword Detection Engine, and then Google's speech recognition APIs to interpret the recorded message.

## Obtain a hotword detection model

Snowboy works with trained models (`.pmdl` or `.umdl` files) that determine what keyword to respond to.

You can either use one of the universal models offered by Snowboy (included in `resources/models/`) or get a personal one using Snowboy's API, through a project like [this](https://github.com/Aculeasis/snowboy-pmdls).

## Installation

To install:

- edit the `src/config.py` file, adding the absolute paths to the `temp/` directory, `resources/` directory, and the model file
- in the main directory, run `pip install -e .`



## Usage 

To start the daemon, run `athena start`, to stop it `athena stop`


