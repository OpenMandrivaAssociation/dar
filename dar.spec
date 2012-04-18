%define major		5
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Summary:	Shell command to back up directory trees and files
Name:		dar
Version:	2.4.5
Release:	1
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
