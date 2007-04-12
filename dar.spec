%define name dar
%define ver 2.3.1
%define release %mkrel 2

%define major   3
%define libname %mklibname %name %major

summary: DAR - Disk ARchive
Name:           %{name}
Version:        %{ver}
Release:        %{release}
URL:            http://dar.linux.free.fr/
License:        GPL
Icon:           dar.gif
Group:          Archiving/Backup
Source:         http://dar.linux.free.fr/%name-%ver.tar.bz2

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:  zlib-devel >= 1.1.3, gcc-c++, bzip2-devel >= 1.0.2
BuildRequires:  libstdc++-static-devel 
BuildRequires:  libattr-devel libacl-devel
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
Summary:        Libraries from %Name
Provides:       lib%name = %version-%release

%description -n %libname
The libraries from %Name package

%package -n %libname-devel
Group:          Development/Other
Summary:        Libraries from %Name
Requires:       %libname = %version
Provides:       lib%name-devel = %version-%release
Provides:       %{name}-devel = %{version}-%{release}

%description -n %libname-devel
The libraries from %Name package

%package -n %libname-static-devel
Group:          Development/Other
Summary:        Static libraries from %Name
Requires:       %libname = %version
Provides:       lib%name-devel = %version-%release
Provides:       %{name}-devel = %{version}-%{release}

%description -n %libname-static-devel
The static libraries from %Name package

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
%{_libdir}/pkgconfig/libdar.pc

%files -n %libname
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %libname-devel
%defattr (-,root,root)
%{_includedir}/dar
%{_libdir}/*.la
%{_libdir}/*.so

%files -n %libname-static-devel
%defattr (-,root,root)
%{_libdir}/*.a

