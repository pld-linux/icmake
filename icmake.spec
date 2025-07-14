Summary:	Icmake - an Intelligent C-like Maker
Summary(pl.UTF-8):	Icmake - inteligentny C-podobny "maker"
Name:		icmake
Version:	9.03.01
Release:	1
License:	GPL v3
Group:		Development/Building
Source0:	https://gitlab.com/fbb-git/icmake/-/archive/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	aa906c6f3769ddd2684c7baab9adf160
Patch0:		verbose-build.patch
URL:		https://fbb-git.gitlab.io/icmake/
BuildRequires:	bash
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Icmake is yet another maker - but this time, one that uses a C-like
syntaxis. The Icmake scripts should feel `natural' to all C
programmers. Icmake is furthermore a powerful shell script language:
it can be used for program maintenance as well as for system
administrative tasks.

%description -l pl.UTF-8
Icmake jest kolejnym programem typu "make" - ale takim, który używa
składni podobnej do C. Skrypty Icmake powinny być dość 'naturalne' dla
programistów C. Icmake jest ponadto potężnym narzędziem skryptowym:
może być używany równie dobrze do tworzenia programów z równym
powodzeniem jak do wykonywania zadań administracyjnych.

%prep
%setup -q
%patch -P0 -p0
%{__sed} -i -e 's#/lib/#/%{_lib}/#g' icmake/INSTALL.im

%build
cd icmake
./icm_prepare /
CC="%{__cc}" \
CFLAGS="%{rpmcflags} %{rpmcppflags}" \
LDFLAGS="%{rpmldflags}" \
./icm_bootstrap /

%install
rm -rf $RPM_BUILD_ROOT

cd icmake
./icm_install all $RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/icmake{,-doc}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc icmake/changelog icmake/doc/icmake.ps icmake/doc/icmake.doc
%dir %{_sysconfdir}/icmake
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/icmake/icmstart.rc
%attr(755,root,root) %{_bindir}/icmake
%attr(755,root,root) %{_bindir}/icmbuild
%attr(755,root,root) %{_bindir}/icmstart
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/icm-comp
%attr(755,root,root) %{_libdir}/%{name}/icm-dep
%attr(755,root,root) %{_libdir}/%{name}/icm-exec
%attr(755,root,root) %{_libdir}/%{name}/icm-pp
%attr(755,root,root) %{_libdir}/%{name}/icmbuild
%attr(755,root,root) %{_libdir}/%{name}/icmun
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/parser
%{_datadir}/%{name}/parser/grammar
%{_datadir}/%{name}/[!p]*
%{_mandir}/man1/icmake.1*
%{_mandir}/man1/icmbuild.1*
%{_mandir}/man1/icmstart.1*
%{_mandir}/man7/icmconf.7*
%{_mandir}/man7/icmstart.rc.7*
