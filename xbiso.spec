Name:		xbiso
Version:	0.6.1
Release:	2
Summary:	ISO extraction utility for xdvdfs images
Group:		Archiving/Cd burning
License:	GPLv2+
URL:		https://sourceforge.net/projects/xbiso/
Source0:	http://downloads.sourceforge.net/xbiso/%{name}-%{version}.tar.gz
Patch0:		xbiso-0.6.1-destdir.patch
BuildRequires:	libftp-devel

%description
xbiso is an ISO extraction utility for xdvdfs images.

%prep
%setup -q
%patch0 -p1

%build
%configure
%make

%install
mkdir -p %{buildroot}%{_bindir}
%makeinstall_std

%files
%doc CHANGELOG LICENSE README
%{_bindir}/xbiso


%changelog
* Fri Dec 23 2011 Alexander Khrukin <akhrukin@mandriva.org> 0.6.1-1
+ Revision: 744798
- BR fix
- removed unneeded lines
- imported package xbiso

