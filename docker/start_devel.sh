#!/bin/bash

docker run \
    -itd \
    --rm \
    --ipc host \
    -e "DISPLAY" \
    -e "QT_X11_NO_MITSHM=1" \
    -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
    -p 1025:1025 \
    --name online_inference \
    --net=host \
    made_mail.ru/online_inference

docker exec \
    -it \
    --user root \
    online_inference \
    bash -c "cd /home/online_inference; bash"
