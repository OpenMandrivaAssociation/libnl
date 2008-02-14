%define	major	1
%define	libname %mklibname nl %{major}
%define	libdev	%mklibname -d nl

Name:		libnl
Version:	1.1
Release:	%mkrel 1
Summary:	Library for applications dealing with netlink sockets
License:	GPL
Group:		System/X11
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://people.suug.ch/~tgr/libnl/
Source0:	http://people.suug.ch/~tgr/libnl/files/%{name}-%{version}.tar.lzma

%description
libnl is a library for applications dealing with netlink sockets.
The library provides an interface for raw netlink messaging and 
various netlink family specific interfaces.

%package -n	%{libname}
Group:		System/Libraries
Summary:	Library for applications dealing with netlink sockets

%description -n	%{libname}
libnl is a library for applications dealing with netlink sockets.
The library provides an interface for raw netlink messaging and
various netlink family specific interfaces.

%package -n	%{libdev}
Group:		Development/C
Summary:	Header files of libnl
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}

%description -n	%{libdev}
libnl is a library for applications dealing with netlink sockets.
The library provides an interface for raw netlink messaging and
various netlink family specific interfaces.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libnl.so.%{major}
%{_libdir}/libnl.so.%{major}.*

%files -n %{libdev}
%defattr(-,root,root)
%dir %{_includedir}/netlink
%{_includedir}/netlink/*.h
%dir %{_includedir}/netlink/fib_lookup
%{_includedir}/netlink/fib_lookup/*.h
%dir %{_includedir}/netlink/genl
%{_includedir}/netlink/genl/*.h
%dir %{_includedir}/netlink/route
%{_includedir}/netlink/route/*.h
%dir %{_includedir}/netlink/route/cls
%{_includedir}/netlink/route/cls/*.h
%dir %{_includedir}/netlink/route/sch
%{_includedir}/netlink/route/sch/*.h
%{_libdir}/libnl.so
%{_libdir}/pkgconfig/%{name}-%{major}.pc
