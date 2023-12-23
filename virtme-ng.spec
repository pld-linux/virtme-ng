Summary:	Tool that allows to easily and quickly recompile and test a Linux kernel
Name:		virtme-ng
Version:	1.19
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	https://github.com/arighi/virtme-ng/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	195793a6562c0dfe31d1d004429636f6
URL:		https://github.com/arighi/virtme-ng
BuildRequires:	python3-argcomplete
BuildRequires:	python3-modules >= 1:3.8
BuildRequires:	python3-requests
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	busybox-static
Requires:	python3 >= 1:3.8
Requires:	python3-modules >= 1:3.8
Requires:	qemu
Requires:	qemu-img
Suggests:	qemu-system-x86
Suggests:	virtiofsd >= 1.7.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
virtme-ng is a tool that allows to easily and quickly recompile and
test a Linux kernel, starting from the source code.

It allows to recompile the kernel in few minutes (rather than hours),
then the kernel is automatically started in a virtualized environment
that is an exact copy-on-write copy of your live system, which means
that any changes made to the virtualized environment do not affect the
host system.

%prep
%setup -q

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc DCO-1.1.txt README.md
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/virtme-ng.conf
%attr(755,root,root) %{_bindir}/virtme-*
%attr(755,root,root) %{_bindir}/vng
%{py3_sitescriptdir}/virtme
%{py3_sitescriptdir}/virtme_ng
%{py3_sitescriptdir}/virtme_ng-%{version}-py*.egg-info
%{bash_compdir}/virtme-ng-prompt
%{bash_compdir}/vng-prompt
