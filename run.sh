docker run --rm -it \
--gpus all \
--network='host' \
-v `pwd`/scripts:/text-classification \
-v `pwd`/models:/models \
igormcsouza/ml:text-classification \
$@