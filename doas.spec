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
BuildRoot: ~/rpmbuild/
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
echo "BUILDROOT = $RPM_BUILD_ROOT"
mkdir -p $RPM_BUILD_ROOT/usr/bin/
cd doas
sed -e "s/PREFIX?=.*/PREFIX?=\$RPM_BUILD_ROOT\/\/usr\/bin/g" -i Makefile
make
cp vidoas doas $RPM_BUILD_ROOT/usr/bin/
exit

%files
%attr(0744, root, root) /usr/bin/doas
%attr(0744, root, root) /usr/bin/vidoas

%pre

%post

%postun

%clean
rm -rf $RPM_BUILD_ROOT/usr/bin/doas
rm -rf $RPM_BUILD_ROOT/usr/bin/vidoas

%changelog
