Summary:	Layer two tunelling protocol daemon
Summary(pl.UTF-8):	Demon tunelujący protokoły warstwy drugiej
Name:		rp-l2tp
Version:	0.4
Release:	0.1
License:	GPL v2
Group:		Networking/Daemons
Source0:	http://dl.sourceforge.net/rp-l2tp/%{name}-%{version}.tar.gz
# Source0-md5:	0e45d11cb4fa6c56cce6b1d119733ed9
URL:		http://sourceforge.net/projects/rp-l2tp/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libtool
Requires:	ppp
Obsoletes:	l2tpd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Layer 2 Tunneling Protocol VPN daemon for Linux and other
POSIX-bases OSs.

%description -l pl.UTF-8
Demon VPN tunelujący protokoły warstwy drugiej dla Linuksa i innych
systemów opartych na POSIX.

%prep
%setup -q

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install l2tp.conf %{_sysconfdir}/l2tp.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
