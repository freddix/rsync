Summary:	Program for efficient remote updates of files
Name:		rsync
Version:	3.1.0
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://rsync.samba.org/ftp/rsync/%{name}-%{version}.tar.gz
# Source0-md5:	3be148772a33224771a8d4d2a028b132
URL:		http://rsync.samba.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	openssl-devel
BuildRequires:	popt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/rsyncd

%description
rsync is a replacement for rcp that has many more features.

rsync uses the "rsync algorithm" which provides a very fast method for
bringing remote files into sync. It does this by sending just the
differences in the files across the link, without requiring that both
sets of files are present at one of the ends of the link beforehand.

A technical report describing the rsync algorithm is included with
this package.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
%{__autoheader}
%{__autoconf}
%configure \
	--enable-ipv6 \
	--disable-debug \
	--with-rsyncd-conf=%{_sysconfdir}/rsyncd.conf
%{__make} proto
%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	bindir=$RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS OLDNEWS TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*

