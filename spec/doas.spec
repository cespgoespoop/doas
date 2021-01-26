###############################################################################
# Spec file for Utils
################################################################################
# Configured to be built by user student or other non-root user
################################################################################
#
Summary: A port of OpenBSD's doas which runs on FreeBSD, Linux, NetBSD, illumos and macOS.
Name: doas
Version: 6.4p4
Release: 1
License: BSD-2-Clause License
URL: https://github.com/slicer69/doas
Group: System
Packager: Jake Harris
#BuildRoot: ~/rpmbuild/
Requires: gcc
Requires: make
Requires: byacc
Requires: pam-devel

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
install -d %{buildroot}%{_bindir}
cp -a doas %{buildroot}%{_bindir}/doas
cp -a vidoas %{buildroot}%{_bindir}/vidoas


