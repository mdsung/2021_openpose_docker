# Openpose docker for python
- Author: MinDong Sung.M.D.
- Last Updteed Date: 2021.09.27
## Objective
- Run openpose on targeted folder 
- Ignore already processed videos.
## Prerequisite
- cuda 10.1 or higher
- docker
- [nvidia-docker](https://github.com/NVIDIA/nvidia-docker)
- [docker-compose](https://docs.docker.com/compose/)

## Project structure
* `code/build_docker.sh`: script for build docker image
* `code/run_docker.sh`: script for run docker container 
* `code/process.py`: python script to list target movies and to run openpose to target movies.
* `code/postprocess.py`: python script to change chown and add "_out" if the name doesn't contain '_out' after openpose was applied
* `code/get_progress.py`: python script to create csv file about processed files, and to calculate progress of the work
* `dockerfile`: dockerfile for running openpose in any environment
* `docker-compose.yml`: docker-compose file for all process

## Process
1. Run `docker-compose --env-file .env up`

or 

1. Run `code/build_docker.sh`
2. Run `code/run_docker.sh`
    - run docker /bin/bash
3. Run in docker `./process.py`

## Reference
* [https://github.com/CMU-Perceptual-Computing-Lab/openpose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)
* [https://hub.docker.com/r/cwaffles/openpose](https://hub.docker.com/r/cwaffles/openpose)
* [https://github.com/u0251077/openpose-docker/commit/f7cb071b6cca51de7c0404e064b4344eb1c075df](https://github.com/u0251077/openpose-docker/commit/f7cb071b6cca51de7c0404e064b4344eb1c075df)