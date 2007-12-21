%define	name libnl
%define version  1.0
%define pre pre5
%if %{pre}
%define release  %mkrel 0.%{pre}.3
%define fullversion %{version}-%{pre}
%else
%define release  %mkrel 1
%define fullversion %{version}
%endif
%define major 1
%define libname %mklibname nl %major

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Library for applications dealing with netlink sockets
License:	GPL
Group:		System/X11
URL:		http://people.suug.ch/~tgr/libnl/
Source0:	http://people.suug.ch/~tgr/libnl/files/libnl-%{fullversion}.tar.bz2
Patch0:     libnl-dont-install-as-root.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
libnl is a library for applications dealing with netlink sockets.
The library provides an interface for raw netlink messaging and 
various netlink family specific interfaces.

#--------------------------------------------------------------------

%package -n %libname
Group:		System/Libraries
Summary:	Library for applications dealing with netlink sockets
Provides:	%name = %version-%release

%description -n %libname
libnl is a library for applications dealing with netlink sockets.
The library provides an interface for raw netlink messaging and
various netlink family specific interfaces.

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%files -n %libname
%defattr(-,root,root)
%{_libdir}/libnl.so.1
%{_libdir}/libnl.so.1.0-pre5


#--------------------------------------------------------------------
%package -n %libname-devel
Group:    Development/C
Summary:  Header files of libnl
Requires: %name = %version
Provides: %name-devel = %version-%release

%description -n %libname-devel
libnl is a library for applications dealing with netlink sockets.
The library provides an interface for raw netlink messaging and
various netlink family specific interfaces.

%files -n %libname-devel
%defattr(-,root,root)
%{_includedir}/netlink/*.h
%{_includedir}/netlink/route/*.h
%{_includedir}/netlink/route/cls/*.h
%{_includedir}/netlink/route/sch/*.h
%{_libdir}/libnl.so
%{_libdir}/pkgconfig/%{name}-%{major}.pc
#---------------------------------------------------------------------

%prep

%setup -q -n %{name}-%{fullversion}
%patch -p0 -b .install-root

%build

%configure2_5x
%make

%install
rm -rf %buildroot

%{makeinstall_std} LIBDIR=%_libdir

install -d %{buildroot}%{_libdir}/pkgconfig/
cat << EOF > %{buildroot}%{_libdir}/pkgconfig/%{name}-%{major}.pc
prefix=%{_prefix}
exec_prefix=\${prefix}
libdir=%{_libdir}
includedir=%{_includedir}

Name: libnl
Description: Convenience library for netlink sockets
Version: %{fullversion}
Libs: -L\${libdir} -lnl
Cflags:
EOF

%clean
rm -rf %buildroot



