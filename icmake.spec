Summary:	Icmake - an Intelligent C-like Maker
Summary(pl):	Icmake - inteligentny C-podobny "maker"
Name:		icmake
Version:	6.22
Release:	3
Group:		Development/Building
License:	GPL
Source0:	ftp://ftp.rug.nl/contrib/frank/software/linux/icmake/%{name}-%{version}.tgz
Source1:	ftp://ftp.rug.nl/contrib/frank/software/linux/icmake/%{name}.doc
Patch0:		%{name}-bootstrap.patch
Patch1:		%{name}-warnings.patch
URL:		ftp://ftp.rug.nl/contrib/frank/software/linux/icmake/icmake.lsm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Icmake is yet another maker -- but this time, one that uses a C-like
syntaxis. The Icmake scripts should feel `natural' to all C
programmers. Icmake is furthermore a powerful shell script language:
it can be used for program maintenance as well as for system
administrative tasks.

%description -l pl
Icmake jest kolejnym programem typu "make" -- ale takim, który u¿ywa
sk³adni podobnej do C. Skrypty Icmake powinny byæ do¶æ 'naturalne' dla
programistów C. Icmake jest ponadto potêznym narzêdziem skryptowym:
mo¿e byæ u¿wany równie dobrze do tworzenia programów z równym
powodzeniem jak do wykonywania zadañ administracyjnych.

%prep
%setup -q -n icmake
%patch0 -p0
%patch1 -p0
install %{SOURCE1} .

%build
CFLAGS="%{rpmcflags}" /bin/sh bootstrap

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install bin/* $RPM_BUILD_ROOT%{_bindir}
install doc/icmake.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES icmake.doc doc/icmake.ps
%attr(755,root,root) %{_bindir}/icm*
%{_mandir}/man1/*
