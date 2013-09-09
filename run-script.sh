#! /system/bin/sh
mkdir /data/tmp
mount -t tmpfs tmpfs /data/tmp
chmod 1777 /data/tmp

export EXTERNAL_STORAGE=/mnt/sdcard
PYTHONPATH=/mnt/sdcard/com.googlecode.pythonforandroid/extras/python
PYTHONPATH=${PYTHONPATH}:/data/data/com.googlecode.pythonforandroid/files/python/lib/python2.6/lib-dynload
export PYTHONPATH
export TEMP=/data/tmp
export PYTHON_EGG_CACHE=$TEMP
export PYTHONHOME=/data/data/com.googlecode.pythonforandroid/files/python
export LD_LIBRARY_PATH=/data/data/com.googlecode.pythonforandroid/files/python/lib
/data/data/com.googlecode.pythonforandroid/files/python/bin/python "$@"