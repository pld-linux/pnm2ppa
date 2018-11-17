Summary:	Drivers for printing to HP PPA printers
Summary(pl.UTF-8):	Sterowniki do drukarek HP PPA
Name:		pnm2ppa
Version:	1.13
Release:	1
License:	GPL v2+
Group:		Applications/Publishing
Source0:	http://downloads.sourceforge.net/pnm2ppa/%{name}-%{version}.tar.gz
# Source0-md5:	5354e54ade6de7a35370e5b47030274c
Source1:	ppa-0.8.6.tar.gz
# Source1-md5:	fb40576435d5979db64fbea305ec224b
Source2:	%{name}-filters.tar.gz
# Source2-md5:	c73c6d86ef7e143f8464ba40c4dfa9bb
Patch0:		pbm2ppa-20000205.diff
Patch1:		%{name}-pld.patch
URL:		http://pnm2ppa.sourceforge.net/
Requires:	ghostscript
Requires:	mpage
Obsoletes:	ppa
Obsoletes:	pbm2ppa
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		lpfiltersdir	%{_libdir}/lpfilters

%description
pnm2ppa is a color driver for HP PPA host-based printers such as the
HP710C, 712C, 720C, 722C, 820Cse, 820Cxi, 1000Cse, and 1000Cxi. It
accepts ghostscript output in PNM formats, and sends it to the printer
in PPA format. The older (black only) driver pbm2ppa is also included.

%description -l pl.UTF-8
pnm2ppa to obsługujący kolor sterownik do drukarek HP PPA, takich jak
HP710C, 712C, 720C, 722C, 820Cse, 820Cxi, 1000Cse, 1000Cxi. Przyjmuje
wyjście ghostscripta w formacie PNM, wysyła je na drukarkę w formacie
PPA. Załączona jest też starsza (obsługująca tylko czerń) wersja
sterownika o nazwie pbm2ppa.

%prep
%setup -q -a1 -a2
%patch0 -p0
%patch1 -p1

%build
%configure

%{__make}

%{__make} -C pbm2ppa-0.8.6 \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{lpfiltersdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install utils/Linux/detect_ppa $RPM_BUILD_ROOT%{_bindir}
install utils/Linux/test_ppa $RPM_BUILD_ROOT%{_bindir}

install pbm2ppa-0.8.6/pbm2ppa $RPM_BUILD_ROOT%{_bindir}
install pbm2ppa-0.8.6/pbmtpg $RPM_BUILD_ROOT%{_bindir}
cp -p pbm2ppa-0.8.6/pbm2ppa.conf $RPM_BUILD_ROOT%{_sysconfdir}
cp -p pbm2ppa-0.8.6/pbm2ppa.1 $RPM_BUILD_ROOT%{_mandir}/man1

install pnm2ppa-filters/pnm2ppa-filter-bw $RPM_BUILD_ROOT%{lpfiltersdir}
install pnm2ppa-filters/pnm2ppa-filter-bw-eco $RPM_BUILD_ROOT%{lpfiltersdir}
install pnm2ppa-filters/pnm2ppa-filter-color $RPM_BUILD_ROOT%{lpfiltersdir}
install pnm2ppa-filters/pnm2ppa-filter-color-eco $RPM_BUILD_ROOT%{lpfiltersdir}

install -d pbm2ppa
for file in CALIBRATION CREDITS README ; do
	install -m 0644 pbm2ppa-0.8.6/$file pbm2ppa/$file
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/en/{CREDITS,INSTALL,README,RELEASE-NOTES,TODO,COLOR.txt,CALIBRATION.txt} test.ps pbm2ppa
%lang(pl) %doc docs/pl/{AUTORZY,CZYTAJ.TO,INSTALACJA,KALIBRACJA}
%attr(755,root,root) %{_bindir}/calibrate_ppa
%attr(755,root,root) %{_bindir}/detect_ppa
%attr(755,root,root) %{_bindir}/pbm2ppa
%attr(755,root,root) %{_bindir}/pbmtpg
%attr(755,root,root) %{_bindir}/pnm2ppa
%attr(755,root,root) %{_bindir}/test_ppa
%{_mandir}/man1/pbm2ppa.1*
%{_mandir}/man1/pnm2ppa.1*
%attr(755,root,root) %{lpfiltersdir}/pnm2ppa-filter-*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/pbm2ppa.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/pnm2ppa.conf
