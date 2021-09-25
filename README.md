# Openpose docker for python
## Author
    MinDong Sung.M.D.
## Date
    2021.09.25
## Objective
- run openpose 
## Prerequisite
- cuda 10.1 or higher
- docker
- [nvidia-docker](https://github.com/NVIDIA/nvidia-docker)

## Project structure
* `code/build_docker.sh`: script for build docker image
* `code/run_docker.sh`: script for run docker container 
* `code/process.py`: python script to list target movies and to run openpose to target movies.
* `dockerfile`: dockerfile for running openpose in any environment

## Process
1. build dockerfile
    ```
    code/build_docker.sh
    ```
2. run docker image
    ```
    code/run_docker.sh
    ```

## Reference
* [https://github.com/CMU-Perceptual-Computing-Lab/openpose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)
* [https://hub.docker.com/r/cwaffles/openpose](https://hub.docker.com/r/cwaffles/openpose)
* [https://github.com/u0251077/openpose-docker/commit/f7cb071b6cca51de7c0404e064b4344eb1c075df](https://github.com/u0251077/openpose-docker/commit/f7cb071b6cca51de7c0404e064b4344eb1c075df)