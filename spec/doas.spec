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
sed -e "s/PREFIX?=.*/PREFIX?=\$RPM_BUILD_ROOT\/\/usr\/bin/g" -i Makefile

%build
make %{?_smp_mflags}


%install
#install -d %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_bindir}
cp -a doas %{buildroot}%{_bindir}/doas
cp -a vidoas %{buildroot}%{_bindir}/vidoas


