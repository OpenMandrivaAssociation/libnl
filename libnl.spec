%define	major	1
%define	libname %mklibname nl %{major}
%define	libdev	%mklibname -d nl

Name:		libnl
Version:	1.1
Release:	8
Summary:	Library for applications dealing with netlink sockets
License:	GPL
Group:		System/X11
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

# Fix unreadable files
find . -perm 0640 -exec chmod 0644 '{}' \;

# a quick hack to make doxygen stripping builddir from html outputs.
sed -i.org -e "s,^STRIP_FROM_PATH.*,STRIP_FROM_PATH = `pwd`," doc/Doxyfile.in

%build
%configure2_5x
make
make gendoc

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libnl.so.%{major}
%{_libdir}/libnl.so.%{major}.*

%files -n %{libdev}
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


%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1-7mdv2011.0
+ Revision: 661505
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1-6mdv2011.0
+ Revision: 602583
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1-5mdv2010.1
+ Revision: 520890
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.1-4mdv2010.0
+ Revision: 425631
- rebuild

* Fri Mar 06 2009 Jérôme Soyer <saispo@mandriva.org> 1.1-3mdv2009.1
+ Revision: 349782
- Rebuild and add Fedora Patches

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri Apr 25 2008 Funda Wang <fwang@mandriva.org> 1.1-2mdv2009.0
+ Revision: 197474
- Obsoletes old devel name

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag

* Tue Feb 05 2008 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.1-1mdv2008.1
+ Revision: 162681
- New release: 1.3
- recompress with lzma rather than bzip2
- cosmetics
- drop fugliness

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Feb 16 2007 Olivier Thauvin <nanardon@mandriva.org> 1.0-0.pre5.3mdv2007.0
+ Revision: 121853
- fix installation (path0: owner during install setup, and libdir)

* Wed Jul 19 2006 Olivier Blin <oblin@mandriva.com> 1.0-0.pre5.2mdv2007.0
+ Revision: 41536
- bump release
- add pkgconfig file (required for NetworkManager)
- define fullversion to work easily with pre version

* Thu Jul 13 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.0-0.pre5.1mdv2007.0
+ Revision: 40979
- import libnl-1.0-0.pre5.1mdv2007.0

