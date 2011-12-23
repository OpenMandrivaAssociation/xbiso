Name:		xbiso
Version:	0.6.1
Release:	1
Summary:	ISO extraction utility for xdvdfs images
Group:		Archiving/Cd burning
License:	GPLv2+
URL:		http://sourceforge.net/projects/xbiso/
Source0:	http://downloads.sourceforge.net/xbiso/%{name}-%{version}.tar.gz
Patch0:		xbiso-0.6.1-destdir.patch
#BuildRequires:	ftplib-devel

%description
xbiso is an ISO extraction utility for xdvdfs images.

%prep
%setup -q
%patch0 -p1

%build
%configure
make %{?_smp_mflags}

%install
#mkdir $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_bindir}
#make DESTDIR=$RPM_BUILD_ROOT install
%makeinstall_std

%files
%doc CHANGELOG LICENSE README
%{_bindir}/xbiso
