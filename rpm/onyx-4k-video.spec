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
/bin/mount -n -o remount,rw /system || :

%files
%defattr(644,root,root,755)
/system/etc/media_profiles.xml
/system/lib/hw/camera.msm8974.so
/system/lib/libmmcamera_interface.so
/system/lib/libmmjpeg_interface.so
/system/lib/libqomx_core.so
/system/vendor/lib/libmmjpeg.so
