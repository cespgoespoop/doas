###############################################################################
# Spec file for Utils
################################################################################
# Configured to be built by user student or other non-root user
################################################################################
#
Summary: A port of OpenBSD's doas which runs on FreeBSD, Linux, NetBSD, illumos and macOS.
Name: doas
Version: 6.3p5
Release: 4
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
head -30 Makefile
make prefix=/usr/bin SYSCONFDIR=/etc 

cat << EOF > doas.conf
# Basic doas configuration
permit :wheel
EOF

cat << EOF >> doas.pam
#%PAM-1.0
auth       include      system-auth
account    include      system-auth
password   include      system-auth
session    optional     pam_keyinit.so revoke
session    include      system-auth
EOF


%install
install -d  %{buildroot}%{_bindir}
install -d  %{buildroot}%{_sysconfdir}
install -d  %{buildroot}%{_mandir}/man{1,5,8}

install -Dm 0444 doas.1 $RPM_BUILD_ROOT%{_mandir}/man1/doas.1
install -Dm 0444 doas.conf.5.final $RPM_BUILD_ROOT%{_mandir}/man5/doas.conf.5
install -Dm 0444 vidoas.8.final $RPM_BUILD_ROOT%{_mandir}/man8/vidoas.8
install -Dm 4744 doas $RPM_BUILD_ROOT%{_bindir}/doas
install -Dm 0755 vidoas.final $RPM_BUILD_ROOT%{_bindir}/vidoas
install -Dm 0644 doas.conf $RPM_BUILD_ROOT%{_sysconfdir}/doas.conf
install -Dm 0644 doas.pam $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/doas



%files 
%attr(4755,root,root) /usr/bin/doas
%attr(0755,root,root) /usr/bin/vidoas
/usr/share/man/*
/etc/doas.conf
/etc/pam.d/doas

#%post
#chmod -v 4111 /usr/bin/doas
