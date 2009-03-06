%define	major	1
%define	libname %mklibname nl %{major}
%define	libdev	%mklibname -d nl

Name:		libnl
Version:	1.1
Release:	%mkrel 3
Summary:	Library for applications dealing with netlink sockets
License:	GPL
Group:		System/X11
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://people.suug.ch/~tgr/libnl/
Source0:	http://people.suug.ch/~tgr/libnl/files/%{name}-%{version}.tar.lzma
BuildRequires: doxygen
Patch1: libnl-1.0-pre5-static.patch
Patch2: libnl-1.0-pre5-debuginfo.patch
Patch3: libnl-1.0-pre8-use-vasprintf-retval.patch
Patch4: libnl-1.0-pre8-more-build-output.patch
Patch5: libnl-1.1-include-limits-h.patch
Patch6: libnl-1.1-doc-inlinesrc.patch

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
Obsoletes:	%mklibname nl 1 -d

%description -n	%{libdev}
libnl is a library for applications dealing with netlink sockets.
The library provides an interface for raw netlink messaging and
various netlink family specific interfaces.

%prep
%setup -q
%setup -q -n %{name}-%{version}
%patch1 -p1 -b .build-static
%patch2 -p1 -b .debuginfo
%patch3 -p1 -b .use-vasprintf-retval
%patch4 -p1 -b .more-build-output
%patch5 -p1 -b .limits
%patch6 -p1 -b .doc-inlinesrc

# a quick hack to make doxygen stripping builddir from html outputs.
sed -i.org -e "s,^STRIP_FROM_PATH.*,STRIP_FROM_PATH = `pwd`," doc/Doxyfile.in

%build
%configure2_5x
make
make gendoc

%install
rm -rf %{buildroot}
%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

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
%{_libdir}/%{name}.a
