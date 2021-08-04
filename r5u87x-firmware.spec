%define snapshot a9b2171d762b

Name:           r5u87x-firmware
# This is a snapshot of 0.2.0 + some fixes
Version:        0.2.0
Release:        17.%{snapshot}%{?dist}
Summary:        R5U87x firmware and loader
Group:          System Environment/Kernel
# Source is GPL, firmware files are distributable
License:        GPLv2+ and Distributable
Url:            http://bitbucket.org/ahixon/r5u87x/wiki/Home
Source0:        http://bitbucket.org/ahixon/r5u87x/get/%{snapshot}.bz2
# Distro specific firmware path adjustments
Patch0:         r5u87x-firmware-path.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  glib2-devel libusb-devel gcc
# For /lib/udev/rules.d dir ownership
Requires:       udev

%description
This package contains firmware needed to make cameras based on Ricoh R5U87x
chipsets work with the uvcvideo driver. And a firmware load tool and udev
rules to load the firmware.


%prep
%setup -q -n r5u87x
%patch0 -p1 -z .firmware_path
chmod 644 README COPYING
chmod 644 docs/*.txt


%build
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS"
make %{?_smp_mflags} PREFIX=
make %{?_smp_mflags} PREFIX= rules


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT PREFIX=


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc docs/*.txt README COPYING
/sbin/r5u87x-loader
/lib/udev/rules.d/90-r5u87x-loader.rules
/lib/firmware/*.fw


%changelog
* Wed Aug 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.0-17.a9b2171d762b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.0-16.a9b2171d762b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.0-15.a9b2171d762b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.0-14.a9b2171d762b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 10 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.0-13.a9b2171d762b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.0-12.a9b2171d762b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.0-11.a9b2171d762b
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <sergio@serjux.com> - 0.2.0-10.a9b2171d762b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.2.0-9.a9b2171d762b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.2.0-8.a9b2171d762b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 26 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.2.0-7.a9b2171d762b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 0.2.0-6.a9b2171d762b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Mar 12 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.2.0-5.a9b2171d762b
- https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Feb 09 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.2.0-4.a9b2171d762b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 18 2010 Hans de Goede <j.w.r.degoede@hhs.nl> 0.2.0-3.a9b2171d762b
- Rebase to latest upstream
- This fixes the udev rules to work with recent udev releases

* Wed Jan 27 2010 Hans de Goede <j.w.r.degoede@hhs.nl> 0.2.0-2.32495328d1c6
- Rebase to latest upstream (includes vflip patch, drop)
- Rename to r5u87x-firmware (rf794)

* Mon Aug 31 2009 Hans de Goede <j.w.r.degoede@hhs.nl> 0.2.0-1.32a27008b8b9
- First version of the RPM Fusion package
