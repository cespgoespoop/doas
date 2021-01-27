###############################################################################
# Spec file for Utils
################################################################################
# Configured to be built by user student or other non-root user
################################################################################
#
Summary: A port of OpenBSD's doas which runs on FreeBSD, Linux, NetBSD, illumos and macOS.
Name: doas
Version: 6.3p4
Release: 1
License: BSD-2-Clause License
URL: https://github.com/cespgoespoop/doas/archive
Group: System
Packager: Jake Harris
#BuildRoot: ~/rpmbuild/
BuildRequires: gcc
BuildRequires: make
BuildRequires: byacc
BuildRequires: pam-devel
Source: https://github.com/cespgoespoop/doas/archive/%{version}.tar.gz
# Build with the following syntax:
# rpmbuild --target noarch -bb utils.spec

%description
A port of OpenBSD's doas which runs on FreeBSD, Linux, NetBSD, illumos and macOS.

%prep
################################################################################
# Create the build tree and copy the files from the development directories    #
# into the build tree.                                                         #
################################################################################


%setup -q
sed -e "s@PREFIX?=.*@PREFIX?='$RPM_BUILD_ROOT'\/usr\/bin@g" -i Makefile
sed -e "s@SYSCONFDIR?=.*@SYSCONFDIR?=\/etc@g" -i Makefile

%define debug_package %{nil}

%build
#make %{?_smp_mflags}
make


%install
#install -d %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_mandir}/man5
mkdir -p %{buildroot}%{_mandir}/man8

cp -av doas.1 %{buildroot}%{_mandir}/man1/doas.1
cp -av doas.conf.5.final %{buildroot}%{_mandir}/man5/doas.conf.5
cp -av vidoas.8.final %{buildroot}%{_mandir}/man8/vidoas.8
cp -av doas %{buildroot}%{_bindir}/doas
cp -av vidoas.final %{buildroot}%{_bindir}/vidoas



%files
%defattr(-,root,root,-)
/usr/bin/doas
/usr/bin/vidoas
/usr/share/man/man1/doas.1
/usr/share/man/man5/doas.conf.5
/usr/share/man/man8/vidoas.8

