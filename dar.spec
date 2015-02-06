%define major		5
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Summary:	Shell command to back up directory trees and files
Name:		dar
Version:	2.4.8
Release:	2
URL:		http://dar.linux.free.fr/
License:	GPLv2+
Group:		Archiving/Backup
Source0:	http://downloads.sourceforge.net/project/dar/%{name}/v%{version}/%{name}-%{version}.tar.gz
Patch0:		dar-2.4.3-mdv-shebang.patch
BuildRequires:	zlib-devel
BuildRequires:	gcc-c++
BuildRequires:	bzip2-devel
BuildRequires:	libstdc++-static-devel
BuildRequires:	libattr-devel
BuildRequires:	acl-devel
BuildRequires:	glibc-static-devel
BuildRequires:	openssl-static-devel
BuildRequires:	doxygen

%description
DAR is a command line tool to backup a directory tree and files. DAR is
able to make differential backups, split them over a set of disks or files
of a given size, use compression, filter files or subtrees to be saved or
not saved, directly access and restore given files. DAR is also able
to handle extended attributes, and can make remote backups through an
ssh session for example. Finally, DAR handles save and restore of hard
and symbolic links.

%package -n 	%{libname}
Group:		System/Libraries
Summary:	Shared library for %{name}

%description -n	%{libname}
DAR is a command line tool to backup a directory tree and files. DAR is
able to make differential backups, split them over a set of disks or files
of a given size, use compression, filter files or subtrees to be saved or
not saved, directly access and restore given files. DAR is also able
to handle extended attributes, and can make remote backups through an
ssh session for example. Finally, DAR handles save and restore of hard
and symbolic links.


%package -n	%{develname}
Group:		Development/Other
Summary:	Development headers for %{name}
Requires:	%libname = %{version}
Provides:	%{name}-devel = %{EVRD}

%description -n	%{develname}
DAR is a command line tool to backup a directory tree and files. DAR is
able to make differential backups, split them over a set of disks or files
of a given size, use compression, filter files or subtrees to be saved or
not saved, directly access and restore given files. DAR is also able
to handle extended attributes, and can make remote backups through an
ssh session for example. Finally, DAR handles save and restore of hard
and symbolic links.


%prep
%setup -q
%patch0 -p1

%build
%configure2_5x --disable-upx --disable-static
%make

%install
# fix-up docs
install -m 644 doc/samples/README README.samples

%makeinstall_std
find %{buildroot} -name '*.la' -delete

%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%doc README.samples doc/samples/cdbackup.sh doc/samples/darrc_sample doc/samples/sample1.txt
%doc doc/mini-howto/dar-differential-backup-mini-howto.*.html
%{_bindir}/*
#/sbin/*
%{_mandir}/man1/*
%{_datadir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}rc

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr (-,root,root)
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/pkgconfig/lib%{name}.pc


%changelog
* Thu Sep 20 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 2.4.8-1
+ Revision: 817171
- update to 2.4.8

* Tue Jul 10 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 2.4.7-1
+ Revision: 808730
- update to 2.4.7

* Fri Jun 29 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 2.4.6-1
+ Revision: 807509
- update to 2.4.6

* Wed Apr 18 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 2.4.5-1
+ Revision: 791726
- update to 2.4.5

* Thu Mar 29 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 2.4.4-1
+ Revision: 788212
- update to 2.4.4

* Thu Mar 01 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 2.4.3-1
+ Revision: 781616
- new version 2.4.3
- don't build static libs

* Sun Oct 16 2011 Andrey Bondrov <abondrov@mandriva.org> 2.4.2-1
+ Revision: 704847
- New version 2.4.2, new major 5

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 2.3.10-2mdv2011.0
+ Revision: 610190
- rebuild

* Thu Apr 15 2010 Sandro Cazzaniga <kharec@mandriva.org> 2.3.10-1mdv2010.1
+ Revision: 534942
- new release 2.3.10

* Sat May 23 2009 Frederik Himpe <fhimpe@mandriva.org> 2.3.9-1mdv2010.0
+ Revision: 379051
- update to new version 2.3.9

* Sat Jun 21 2008 Funda Wang <fwang@mandriva.org> 2.3.8-1mdv2009.0
+ Revision: 227663
- New version 2.3.8

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sat Mar 01 2008 Adam Williamson <awilliamson@mandriva.org> 2.3.7-1mdv2008.1
+ Revision: 177114
- protect major in file list
- minor spec cleanups
- new release 2.3.7

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag

* Thu Dec 06 2007 Adam Williamson <awilliamson@mandriva.org> 2.3.6-1mdv2008.1
+ Revision: 115797
- new release 2.3.6
- new license policy
- remove a workaround that was introduced for kdar, as kdar is basically dead

* Mon Aug 27 2007 Funda Wang <fwang@mandriva.org> 2.3.5-1mdv2008.0
+ Revision: 71738
- New version 2.3.5

* Thu Jul 12 2007 Adam Williamson <awilliamson@mandriva.org> 2.3.4-1mdv2008.0
+ Revision: 51677
- spec clean (from frederik himpe)
- new release 2.3.4 (from frederik himpe)

* Mon Jun 11 2007 Adam Williamson <awilliamson@mandriva.org> 2.3.3-2mdv2008.0
+ Revision: 38087
- include macro_tools.hpp in libdar-devel for kdar

* Sun Jun 10 2007 Adam Williamson <awilliamson@mandriva.org> 2.3.3-1mdv2008.0
+ Revision: 37738
- move .pc file to devel package
- clean and correct provides
- clean descriptions
- go with the new devel policy
- correct major (4)
- new release 2.3.3


* Mon Aug 14 2006 Nicolas Lécureuil <neoclust@mandriva.org> 2.3.1-2mdv2007.0
- Fix rpmlint warnings

* Sat Jul 01 2006 Emmanuel Andry <eandry@mandriva.org> 2.3.1-1mdv2007.0
- New release 2.3.1

* Sun May 07 2006 Jerome Soyer <saispo@mandriva.org> 2.3.0-1mdk
- New release 2.3.0
- Fix doc build

* Wed Dec 07 2005 Lenny Cartier <lenny@mandriva.com> 2.2.5-1mdk
- 2.2.5

* Mon Aug 22 2005 Frederic Crozat <fcrozat@mandriva.com> 2.2.2-3mdk 
- Rebuild with latest gcc

* Sun Jun 05 2005 Frederic Crozat <fcrozat@mandriva.com> 2.2.2-2mdk 
- Set executable bit on par scripts

* Sun Jun 05 2005 Frederic Crozat <fcrozat@mandriva.com> 2.2.2-1mdk
- Release 2.2.2

* Sun May 08 2005 Frederic Crozat <fcrozat@mandriva.com> 2.2.1-2mdk 
- Fix buildrequires

* Sun May 08 2005 Frederic Crozat <fcrozat@mandriva.com> 2.2.1-1mdk 
- Release 2.2.1
- clean specfile
- build with EA support now

* Tue Sep 28 2004 Svetoslav Slavtchev <svetljo@gmx.de> 2.1.5-2mdk
- fix group and post/pre scripts

* Tue Sep 28 2004 Svetoslav Slavtchev <svetljo@gmx.de> 2.1.5-1mdk
- initial contrib package

