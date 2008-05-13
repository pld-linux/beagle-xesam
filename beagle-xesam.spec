#
Summary:	Xesam adapter for Beagle
Name:		beagle-xesam
Version:	0.2
Release:	0.1
License:	MIT
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/beagle-xesam/0.2/%{name}-%{version}.tar.bz2
# Source0-md5:	76e032fb45f351b1c955dd509aaeebeb
URL:		http://beagle-project.org/
BuildRequires:	dotnet-ndesk-dbus-glib-sharp-devel
BuildRequires:	libbeagle-devel >= 0.3.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xesam adapter for Beagle.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/beagle-xesam-adaptor
%dir %{_libdir}/beagle-xesam
%attr(755,root,root) %{_libdir}/beagle-xesam/*.exe
%{_libdir}/beagle-xesam/*.mdb
