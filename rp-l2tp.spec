#
Summary:    Layer two tunelling protocol daemon
Summary(pl):    Demon tuneluj±cy protoko³y warstwy drugiej
Name:		rp-l2tp
Version:	0.4
Release:	0.1
License:	- (enter GPL/GPL v2/LGPL/BSD/BSD-like/other license name here)
#Vendor:		-
Group:      Networking/Daemons
Source0:	http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
URL:		-
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
#BuildRequires:	-
#PreReq:		-
#Requires(pre,post):	-
#Requires(preun):	-
#Requires(postun):	-
Requires:	ppp
#Provides:	-
Obsoletes:	l2tpd
#Conflicts:	-
#BuildArch:	noarch
#ExclusiveArch:  %{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

License:    GPL
Source0:    http://www.l2tpd.org/downloads/%{name}-%{version}.tar.gz

%description
A Layer 2 Tunneling Protocol VPN daemon for Linux and other
POSIX-bases OSs.

%description -l pl
Demon VPN tuneluj±cy protoko³y warstwy drugiej dla Linuksa i innych
systemów opartych na POSIX.

%prep
%setup -q

%build
# if ac/am/* rebuilding is necessary, do it in this order and add
# appropriate BuildRequires
#%%{__gettextize}
#%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
#cp -f /usr/share/automake/config.sub .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post
#%post	-p /sbin/ldconfig

%preun

%postun
#%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO

# if _sysconfdir != /etc:
#%%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*

%attr(755,root,root) %{_bindir}/*

%{_datadir}/%{name}

# initscript and its config
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}

%files subpackage
%defattr(644,root,root,755)
%doc extras/*.gz
%{_datadir}/%{name}-ext
