#%define		_pre	pre3
Summary:	Drivers for printing to HP PPA printers
Summary(pl):	Sterowniki do drukarek HP PPA
Name:		pnm2ppa
Version:	1.12
Release:	1
License:	GPL
Group:		Applications/Publishing
Source0:	http://belnet.dl.sourceforge.net/pnm2ppa/%{name}-%{version}.tar.gz
Source1:	ppa-0.8.6.tar.gz
Source2:	%{name}-filters.tar.gz
Patch0:		pbm2ppa-20000205.diff
Patch1:		%{name}-pld.patch
Patch2:		%{name}-destdir.patch
URL:		http://pnm2ppa.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	mpage ghostscript
Obsoletes:	ppa
Obsoletes:	pbm2ppa

%description
pnm2ppa is a color driver for HP PPA host-based printers such as the
HP710C, 712C, 720C, 722C, 820Cse, 820Cxi, 1000Cse, and 1000Cxi. It
accepts ghostscript output in PNM formats, and sends it to the printer
in PPA format. The older (black only) driver pbm2ppa is also included.

Install pnm2ppa if you have a PPA printer and need to print.

For further information, see the pnm2ppa project homepage at
http://pnm2ppa.sourceforge.net/ .

%description -l pl
pnm2ppa to obs³uguj±cy kolor sterownik do drukarek HP PPA, takich jak
HP710C, 712C, 720C, 722C, 820Cse, 820Cxi, 1000Cse, 1000Cxi. Przyjmuje
wyj¶cie ghostscripta w formacie PNM, wysy³a je na drukarkê w formacie
PPA. Za³±czona jest te¿ starsza (obs³uguj±ca tylko czerñ) wersja
sterownika o nazwie pbm2ppa.

Wiêcej informacji znajduje siê na stronie projektu.

%prep
%setup -q -n %{name}-%{version} -a1 -a2
%patch0 -p0
%patch1 -p1
%patch2 -p1

%build
%{__make}
cd pbm2ppa-0.8.6
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir},%{_mandir}/man1,%{_libdir}/lpfilters}

%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	CONFDIR=$RPM_BUILD_ROOT%{_sysconfdir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1

install utils/Linux/detect_ppa $RPM_BUILD_ROOT%{_bindir}
install utils/Linux/test_ppa $RPM_BUILD_ROOT%{_bindir}
install pbm2ppa-0.8.6/pbm2ppa $RPM_BUILD_ROOT%{_bindir}
install pbm2ppa-0.8.6/pbmtpg $RPM_BUILD_ROOT%{_bindir}
install pbm2ppa-0.8.6/pbm2ppa.conf $RPM_BUILD_ROOT%{_sysconfdir}
install pbm2ppa-0.8.6/pbm2ppa.1 $RPM_BUILD_ROOT%{_mandir}/man1
install pnm2ppa-filters/pnm2ppa-filter-bw $RPM_BUILD_ROOT%{_libdir}/lpfilters
install pnm2ppa-filters/pnm2ppa-filter-bw-eco $RPM_BUILD_ROOT%{_libdir}/lpfilters
install pnm2ppa-filters/pnm2ppa-filter-color $RPM_BUILD_ROOT%{_libdir}/lpfilters
install pnm2ppa-filters/pnm2ppa-filter-color-eco $RPM_BUILD_ROOT%{_libdir}/lpfilters

install -d pbm2ppa
for file in CALIBRATION CREDITS README ; do
	install -m 0644 pbm2ppa-0.8.6/$file pbm2ppa/$file
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/en/{CREDITS,INSTALL,LICENSE,README,RELEASE-NOTES,TODO,COLOR.txt,CALIBRATION.txt}
%doc test.ps pbm2ppa
%attr(755,root,root) %{_bindir}/pnm2ppa
%attr(755,root,root) %{_bindir}/pbm2ppa
%attr(755,root,root) %{_bindir}/pbmtpg
%attr(755,root,root) %{_bindir}/calibrate_ppa
%attr(755,root,root) %{_bindir}/test_ppa
%attr(755,root,root) %{_bindir}/detect_ppa
%{_mandir}/man1/*.1*
%attr(755,root,root) %{_libdir}/lpfilters/pnm2ppa-filter-*
%config %{_sysconfdir}/pnm2ppa.conf
%config %{_sysconfdir}/pbm2ppa.conf
