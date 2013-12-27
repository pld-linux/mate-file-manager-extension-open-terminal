Summary:	open-terminal extension for Caja (MATE file manager)
Summary(pl.UTF-8):	Rozszerzenie open-terminal dla zarządcy plików Caja ze środowiska MATE
Name:		mate-file-manager-extension-open-terminal
Version:	1.6.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://pub.mate-desktop.org/releases/1.6/mate-file-manager-open-terminal-%{version}.tar.xz
# Source0-md5:	630effed402ff64a270d7062212615d2
URL:		http://mate-desktop.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-devel >= 0.10.40
BuildRequires:	glib2-devel >= 1:2.14.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libtool >= 1:1.4.3
BuildRequires:	mate-file-manager-devel >= 1.1.0
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.14.0
Requires:	glib2 >= 1:2.14.0
Requires:	mate-file-manager >= 1.1.0
Requires:	mate-terminal
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a proof-of-concept Caja extension which allows you to open a
terminal in arbitrary local folders.

This is a fork of nautilus-open-terminal extension.

%description -l pl.UTF-8
Rozszerzenie zarządcy plików Caja, pozwalające na otwieranie terminala
w dowolnych folderach lokalnych.

Jest to odgałęzienie rozszerzenia nautilus-open-terminal.

%prep
%setup -q -n mate-file-manager-open-terminal-%{version}

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/caja/extensions-2.0/*.la

# mate < 1.5 did not exist in PLD, avoid dependency on mate-conf
%{__rm} $RPM_BUILD_ROOT%{_datadir}/MateConf/gsettings/caja-open-terminal.convert

%find_lang caja-open-terminal

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f caja-open-terminal.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/caja/extensions-2.0/libcaja-open-terminal.so
%{_datadir}/glib-2.0/schemas/org.mate.caja-open-terminal.gschema.xml
