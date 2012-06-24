Summary:	Icmake - an Intelligent C-like Maker
Summary(pl):	Icmake - inteligentny C-podobny "maker"
Name:		icmake
Version:	6.22
Release:	1
Group:		Developement/Building
Group(pl):	Programowanie/Budowanie
Copyright:	GPL
Source0:	ftp://ftp.icce.rug.nl/pub/unix/%{name}-%{version}.tgz
Source1:	ftp://ftp.icce.rug.nl/pub/unix/%{name}.doc
Patch0:		icmake-bootstrap.patch
Patch1:		icmake-warnings.patch
URL:		ftp://ftp.icce/rug.nl/pub/unix
BuildRoot:   	/tmp/%{name}-%{version}-root

%description
Icmake is yet another maker -- but this time, one that uses a C-like
syntaxis. The Icmake scripts should feel `natural' to all C programmers.
Icmake is furthermore a powerful shell script language: it can be used for
program maintenance as well as for system administrative tasks.

%description -l pl
Icmake jest kolejnym programem typu "make" -- ale takim, kt�ry u�ywa sk�adni
podobnej do C. Skrypty Icmake powinny by� do�� 'naturalne' dla programist�w
C. Icmake jest ponadto pot�znym narz�dziem skryptowym: mo�e by� u�wany
r�wnie dobrze do tworzenia program�w z r�wnym powodzeniem jak do wykonywania
zada� administracyjnych.

%prep
%setup -q -n icmake
%patch0 -p0
%patch1 -p0
install %{SOURCE1} .

%build
CFLAGS=$RPM_OPT_FLAGS /bin/sh bootstrap

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install bin/* $RPM_BUILD_ROOT%{_bindir}
install doc/icmake.1 $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/* \
	CHANGES icmake.doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.gz icmake.doc.gz doc/icmake.ps
%attr(755,root,root) %{_bindir}/icm*
%{_mandir}/man1/*
