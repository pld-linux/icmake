Summary:	Icmake - an Intelligent C-like Maker
Summary(pl.UTF-8):	Icmake - inteligentny C-podobny "maker"
Name:		icmake
Version:	7.16.00
Release:	1
License:	GPL v3
Group:		Development/Building
Source0:	http://downloads.sourceforge.net/icmake/%{name}_%{version}.orig.tar.gz
# Source0-md5:	174cf585d9133a42797d49e280345f03
URL:		http://icmake.sourceforge.net/
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
%{__sed} -i -e 's#gcc#%{__cc}#g' icm_bootstrap
%{__sed} -i -e 's#/lib/#/%{_lib}/#g' INSTALL.im

%build
CFLAGS="%{rpmcflags} %{rpmcppflags}" \
LDFLAGS="%{rpmldflags}" \
./icm_bootstrap /

%install
rm -rf $RPM_BUILD_ROOT

./icm_install progs $RPM_BUILD_ROOT
./icm_install scripts $RPM_BUILD_ROOT
./icm_install skel $RPM_BUILD_ROOT
./icm_install man $RPM_BUILD_ROOT
./icm_install doc $RPM_BUILD_ROOT
./icm_install etc $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc changelog doc/icmake.ps doc/icmake.doc
%dir %{_sysconfdir}/icmake
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/icmake/icmstart.rc
%attr(755,root,root) %{_bindir}/icmake
%attr(755,root,root) %{_bindir}/icmbuild
%attr(755,root,root) %{_bindir}/icmstart
%attr(755,root,root) %{_bindir}/icmun
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/icm-comp
%attr(755,root,root) %{_libdir}/%{name}/icm-exec
%attr(755,root,root) %{_libdir}/%{name}/icm-pp
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/parser
%{_datadir}/%{name}/parser/grammar
%dir %{_datadir}/%{name}/parser/gramspec
%attr(755,root,root) %{_datadir}/%{name}/parser/gramspec/grambuild
%{_datadir}/%{name}/parser/gramspec/*.gr0
%{_datadir}/%{name}/[!p]*
%{_mandir}/man1/icmake.1*
%{_mandir}/man1/icmbuild.1*
%{_mandir}/man1/icmstart.1*
%{_mandir}/man7/icmconf.7*
%{_mandir}/man7/icmstart.rc.7*
