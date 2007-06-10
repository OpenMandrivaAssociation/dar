%define name dar
%define version 2.3.3
%define release %mkrel 1

%define major   4
%define libname %mklibname %name %major
%define develname %mklibname %name -d
%define staticname %mklibname %name -d -s

summary: DAR - Disk ARchive
Name:           %{name}
Version:        %{version}
Release:        %{release}
URL:            http://dar.linux.free.fr/
License:        GPL
Group:          Archiving/Backup
Source:         http://dar.linux.free.fr/%name-%version.tar.bz2

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:  zlib-devel 
BuildRequires:	gcc-c++ 
BuildRequires:	bzip2-devel
BuildRequires:  libstdc++-static-devel 
BuildRequires:  libattr-devel 
BuildRequires:	libacl-devel
BuildRequires:  glibc-static-devel
BuildRequires:  openssl-static-devel
BuildRequires:  doxygen

%description
DAR is a command line tool to backup a directory tree and files. DAR is
able to make differential backups, split them over a set of disks or files
of a given size, use compression, filter files or subtrees to be saved or
not saved, directly access and restore given files. DAR is also able
to handle extented attributes, and can make remote backups through an
ssh session for example. Finally, DAR handles save and restore of hard
and symbolic links.

%package -n %libname
Group:          System/Libraries
Summary:        Shared library for %{name}
Provides:       lib%name = %version-%release

%description -n %libname
DAR is a command line tool to backup a directory tree and files. DAR is
able to make differential backups, split them over a set of disks or files
of a given size, use compression, filter files or subtrees to be saved or
not saved, directly access and restore given files. DAR is also able
to handle extented attributes, and can make remote backups through an
ssh session for example. Finally, DAR handles save and restore of hard
and symbolic links.


%package -n %develname
Group:          Development/Other
Summary:        Development headers for %{name}
Requires:       %libname = %version
Provides:       %{name}-devel = %{version}-%{release}

%description -n %develname
DAR is a command line tool to backup a directory tree and files. DAR is
able to make differential backups, split them over a set of disks or files
of a given size, use compression, filter files or subtrees to be saved or
not saved, directly access and restore given files. DAR is also able
to handle extented attributes, and can make remote backups through an
ssh session for example. Finally, DAR handles save and restore of hard
and symbolic links.


%package -n %staticname
Group:          Development/Other
Summary:        Static development headers for %{name}
Requires:       %libname = %version
Provides:       %{name}-static-devel = %{version}-%{release}

%description -n %staticname
DAR is a command line tool to backup a directory tree and files. DAR is
able to make differential backups, split them over a set of disks or files
of a given size, use compression, filter files or subtrees to be saved or
not saved, directly access and restore given files. DAR is also able
to handle extented attributes, and can make remote backups through an
ssh session for example. Finally, DAR handles save and restore of hard
and symbolic links.

%prep
%setup -q 

%build
%configure2_5x --disable-upx 

#parallel build is broken
make

%install
rm -rf %{buildroot}

# fix-up docs
install -m 644 doc/samples/README README.samples

%makeinstall_std

%find_lang %{name}

#chmod a+x $RPM_BUILD_ROOT%{_datadir}/dar/*.duc

# mv dar_static to /sbin , just in case :-) 
install -d %buildroot/sbin
install %buildroot/%_bindir/dar_static  %buildroot/sbin/
rm -f %buildroot/%_bindir/dar_static 

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%post -n %libname -p /sbin/ldconfig

%postun  -n %libname -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README THANKS TODO
%doc README.samples doc/samples/cdbackup.sh doc/samples/darrc_sample doc/samples/sample1.txt
%doc doc/mini-howto/dar-differential-backup-mini-howto.*.html
%{_bindir}/*
/sbin/*
%{_mandir}/man1/*
%{_datadir}/%name

%files -n %libname
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %develname
%defattr (-,root,root)
%{_includedir}/dar
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/lib%{name}.pc

%files -n %staticname
%defattr (-,root,root)
%{_libdir}/*.a

