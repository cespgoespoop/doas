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
BuildRoot: ~/rpmbuild/
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
#sed -e "s@PREFIX?=.*@PREFIX?='$RPM_BUILD_ROOT'\/usr\/bin@g" -i Makefile
#sed -e "s@SYSCONFDIR?=.*@SYSCONFDIR?=\/etc@g" -i Makefile
echo "BUILDROOT = $RPM_BUILD_ROOT"

%define debug_package %{nil}

%build
#make %{?_smp_mflags}
make prefix=/usr/bin sysconfdir=/etc


%install
#install -d %{buildroot}%{_bindir}
install -d  %{buildroot}%{_bindir}
install -d  %{buildroot}%{_sysconfdir}
install -d  %{buildroot}%{_mandir}/man{1,5,8}
pwd
ls -lhart
cp -av doas.1 $RPM_BUILD_ROOT%{_mandir}/man1/doas.1
ls -lh $RPM_BUILD_ROOT%{_mandir}/man1/doas.1
cp -av doas.conf.5.final $RPM_BUILD_ROOT%{_mandir}/man5/doas.conf.5
ls -lh $RPM_BUILD_ROOT%{_mandir}/man5/doas.conf.5
cp -av vidoas.8.final $RPM_BUILD_ROOT%{_mandir}/man8/vidoas.8
ls -lh $RPM_BUILD_ROOT%{_mandir}/man8/vidoas.8
cp -av doas $RPM_BUILD_ROOT%{_bindir}/doas
cp -av vidoas.final $RPM_BUILD_ROOT%{_bindir}/vidoas



%files
%defattr(-,root,root,-)
%attr(0744, root, root) /usr/bin/vidoas
%attr(4755, root, root) /usr/bin/doas
%doc %attr(0444,root,root) /usr/share/man/*

