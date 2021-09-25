#!/bin/bash

docker run --rm --gpus all --name openpose -v /tmp/.X11-unix:/tmp/.X11-unix -v /dev/snd:/dev/snd -e DISPLAY=unix$DISPLAY -v /home/nia_data/raw:/data/raw -v /home/nia_data/processed:/data/processed -it openpose:latest