TARGET = onyx-4k-video
TEMPLATE = aux

system.files = system/*
system.path = /system
etc.files = etc/*
etc.path = /etc

INSTALLS = system etc

OTHER_FILES += \
    rpm/onyx-4k-video.spec \
    etc/camera-settings/camera-resolutions.json \
    system/etc/media_profiles_4k.xml \
    system/lib/hw/camera.msm8974.so \
    system/lib/libmmcamera_interface.so \
    system/lib/libmmjpeg_interface.so \
    system/lib/libqomx_core.so \
    system/vendor/lib/libmmjpeg.so \
    system/vendor/lib/libchromatix_s5k3m2_hfr_60fps.so \
    system/vendor/lib/libchromatix_s5k3m2_hfr_90fps.so \
    system/vendor/lib/libchromatix_s5k3m2_hfr_120fps.so
