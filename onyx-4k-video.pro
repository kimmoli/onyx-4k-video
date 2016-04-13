TARGET = onyx-4k-video
TEMPLATE = aux

system.files = system/*
system.path = /system

INSTALLS = system

OTHER_FILES += \
    rpm/onyx-4k-video.spec \
    system/etc/media_profiles.xml \
    system/lib/hw/camera.msm8974.so \
    system/lib/libmmcamera_interface.so \
    system/lib/libmmjpeg_interface.so \
    system/lib/libqomx_core.so \
    system/vendor/lib/libmmjpeg.so
