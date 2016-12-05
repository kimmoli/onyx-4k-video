Name:       onyx-4k-video

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}
Summary:    OnePlusX 4K video
Version:    0.0.1
Release:    1
Group:      Qt/Qt
License:    LICENSE
URL:        http://forum.xda-developers.com/oneplus-x/orig-development/mod-custom-camera-hal-4k-uhd-dci-30-fps-t3315382
Source0:    %{name}-%{version}.tar.bz2

AutoReqProv: no

%description
Sultanxda 4K video patch convenience rpm package

%prep
%setup -q -n %{name}-%{version}

%build

%qtc_qmake5 SPECVERSION=%{version}

%qtc_make %{?_smp_mflags}

%install
rm -rf %{buildroot}

%qmake5_install

%pre
/usr/bin/ssu mo | grep -q "onyx" || exit 1
/bin/mount -n -o remount,rw /system || exit 1
cp /system/etc/media_profiles.xml /system/etc/media_profiles.org || :
cp /system/lib/hw/camera.msm8974.so /system/lib/hw/camera.msm8974.org || :
cp /system/lib/libmmcamera_interface.so /system/lib/libmmcamera_interface.org || :
cp /system/lib/libmmjpeg_interface.so /system/lib/libmmjpeg_interface.org || :
cp /system/lib/libqomx_core.so /system/lib/libqomx_core.org || :
cp /system/vendor/lib/libmmjpeg.so /system/vendor/lib/libmmjpeg.org || :
cp /system/vendor/lib/libchromatix_s5k3m2_hfr_120fps.so /system/vendor/lib/libchromatix_s5k3m2_hfr_120fps.org || :
cp /system/vendor/lib/libchromatix_s5k3m2_hfr_60fps.so /system/vendor/lib/libchromatix_s5k3m2_hfr_60fps.org || :
cp /system/vendor/lib/libchromatix_s5k3m2_hfr_90fps.so /system/vendor/lib/libchromatix_s5k3m2_hfr_90fps.org || :

%preun
/bin/mount -n -o remount,rw /system || exit 1

%postun
cp /system/etc/media_profiles.org /system/etc/media_profiles.xml || :
cp /system/lib/hw/camera.msm8974.org /system/lib/hw/camera.msm8974.so || :
cp /system/lib/libmmcamera_interface.org /system/lib/libmmcamera_interface.so || :
cp /system/lib/libmmjpeg_interface.org /system/lib/libmmjpeg_interface.so || :
cp /system/lib/libqomx_core.org /system/lib/libqomx_core.so || :
cp /system/vendor/lib/libmmjpeg.org /system/vendor/lib/libmmjpeg.so || :
cp /system/vendor/lib/libchromatix_s5k3m2_hfr_120fps.org /system/vendor/lib/libchromatix_s5k3m2_hfr_120fps.so || :
cp /system/vendor/lib/libchromatix_s5k3m2_hfr_60fps.org /system/vendor/lib/libchromatix_s5k3m2_hfr_60fps.so || :
cp /system/vendor/lib/libchromatix_s5k3m2_hfr_90fps.org /system/vendor/lib/libchromatix_s5k3m2_hfr_90fps.so || :

%files
%defattr(644,root,root,755)
/etc/camera-settings
/etc/camera-settings/camera-resolutions.json
/system/etc/media_profiles.xml
/system/lib/hw/camera.msm8974.so
/system/lib/libmmcamera_interface.so
/system/lib/libmmjpeg_interface.so
/system/lib/libqomx_core.so
/system/vendor/lib/libmmjpeg.so
/system/vendor/lib/libchromatix_s5k3m2_hfr_120fps.so
/system/vendor/lib/libchromatix_s5k3m2_hfr_60fps.so
/system/vendor/lib/libchromatix_s5k3m2_hfr_90fps.so
