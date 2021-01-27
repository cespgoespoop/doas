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
sed -e "s/PREFIX?=.*/PREFIX?='$RPM_BUILD_ROOT'\/\/usr\/bin/g" -i Makefile
sed -e "s/SYSCONFDIR?=.*/='$RPM_BUILD_ROOT'\/etc/g" -i Makefile

%define debug_package %{nil}

%build
#make %{?_smp_mflags}
make


%install
#install -d %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_bindir}
cp -a doas %{buildroot}%{_bindir}/doas
cp -a vidoas.final %{buildroot}%{_bindir}/vidoas

mkdir -p %{buildroot}%{_sysconfdir}

cat << EOF > %{buildroot}%{_sysconfdir}/doas.conf
# Please see doas.conf manual page for information on setting
# up a doas.conf file.

# Permit members of the wheel group to perform actions as root.
permit :wheel
EOF


%files
%defattr(-,root,root,-)
/usr/bin/doas
/usr/bin/vidoas
/etc/doas.conf
