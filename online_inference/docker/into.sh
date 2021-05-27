#!/bin/bash

docker exec \
    -it \
    --user root \
    online_inference bash -c "cd /home/online_inference; bash"
