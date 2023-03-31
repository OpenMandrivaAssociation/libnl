%define	major	1
%define	libname	%mklibname nl %{major}
%define	devname	%mklibname -d nl
%define _disable_lto 1

Summary:	Library for applications dealing with netlink sockets
Name:		libnl
Version:	1.1.4
Release:	2
License:	GPLv2
Group:		System/X11
Url:		http://people.suug.ch/~tgr/libnl/
Source0:	https://www.infradead.org/~tgr/libnl/files/libnl-%{version}.tar.gz
BuildRequires: doxygen

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

%package -n	%{devname}
Group:		Development/C
Summary:	Header files of libnl
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n	%{devname}
libnl is a library for applications dealing with netlink sockets.
The library provides an interface for raw netlink messaging and
various netlink family specific interfaces.

%prep
%setup -q
%autopatch -p1

# Fix unreadable files
find . -perm 0640 -exec chmod 0644 '{}' \;

# a quick hack to make doxygen stripping builddir from html outputs.
sed -i.org -e "s,^STRIP_FROM_PATH.*,STRIP_FROM_PATH = `pwd`," doc/Doxyfile.in

%build
%configure --disable-static
%make_build

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.a

%files -n %{libname}
%{_libdir}/libnl.so.%{major}*

%files -n %{devname}
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
