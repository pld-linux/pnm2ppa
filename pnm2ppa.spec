Name:		pnm2ppa
Summary:	Drivers for printing to HP PPA printers
Obsoletes:	ppa
Obsoletes:	pbm2ppa
Version:	1.04
Release:	1
Group:		Applications/Publishing
Group(de):	Applikationen/Publizieren
Group(pl):	Aplikacje/Publikowanie
URL:		http://sourceforge.net/projects/pnm2ppa 
Source0:	http://download.sourceforge.net/pnm2ppa/%{name}-%{version}.tar.gz
Source1:	http://www.httptech.com/ppa/files/ppa-0.8.6.tar.gz
Source2:	%{name}-filters.tar.gz
Patch0:		pbm2ppa-20000205.diff
Patch1:		%{name}-pld.patch
License:	GPL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	mpage ghostscript

%define topdir %{name}-%{version}
%define _prefix /usr

%description
pnm2ppa is a color driver for HP PPA host-based printers such as the
HP710C, 712C, 720C, 722C, 820Cse, 820Cxi, 1000Cse, and 1000Cxi. It
accepts ghostscript output in PNM formats, and sends it to the printer
in PPA format. The older (black only) driver pbm2ppa is also included.

Install pnm2ppa if you have a PPA printer and need to print.

For further information, see the pnm2ppa project homepage at
http://sourceforge.net/projects/pnm2ppa .

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q -n %{topdir}
%setup -q -T -D -a 1 -n %{topdir}
%setup -q -T -D -a 2 -n %{topdir}
%patch0 -p0
%patch1 -p1

%build
%{__make} 
cd pbm2ppa-0.8.6
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_sysconfdir}
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install -d $RPM_BUILD_ROOT%{_libdir}/lpfilters
%{__make} INSTALLDIR=$RPM_BUILD_ROOT%{_bindir} CONFDIR=$RPM_BUILD_ROOT%{_sysconfdir} \
    MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 install 
install -m 0755 utils/Linux/detect_ppa $RPM_BUILD_ROOT%{_bindir}/
install -m 0755 utils/Linux/test_ppa $RPM_BUILD_ROOT%{_bindir}/
install -m 0755 pbm2ppa-0.8.6/pbm2ppa $RPM_BUILD_ROOT%{_bindir}/
install -m 0755 pbm2ppa-0.8.6/pbmtpg $RPM_BUILD_ROOT%{_bindir}/
install -m 0644 pbm2ppa-0.8.6/pbm2ppa.conf $RPM_BUILD_ROOT%{_sysconfdir}
install -m 0644 pbm2ppa-0.8.6/pbm2ppa.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 0755 pnm2ppa-filters/pnm2ppa-filter-bw $RPM_BUILD_ROOT%{_libdir}/lpfilters
install -m 0755 pnm2ppa-filters/pnm2ppa-filter-bw-eco $RPM_BUILD_ROOT%{_libdir}/lpfilters
install -m 0755 pnm2ppa-filters/pnm2ppa-filter-color $RPM_BUILD_ROOT%{_libdir}/lpfilters
install -m 0755 pnm2ppa-filters/pnm2ppa-filter-color-eco $RPM_BUILD_ROOT%{_libdir}/lpfilters

install -d pbm2ppa
for file in CALIBRATION CREDITS INSTALL INSTALL-MORE LICENSE README ; do
  install -m 0644 pbm2ppa-0.8.6/$file pbm2ppa/$file
done

%clean
rm -rf $RPM_BUILD_ROOT 

%files 
%defattr(644,root,root,755)
%doc docs/en/CREDITS docs/en/INSTALL docs/en/LICENSE docs/en/README
%doc docs/en/RELEASE-NOTES docs/en/TODO
%doc docs/en/COLOR.txt docs/en/CALIBRATION.txt
%doc docs/en/COLOR.html docs/en/CALIBRATION.html
%doc test.ps
%doc pbm2ppa
%attr(755,root,root) %{_bindir}/pnm2ppa
%attr(755,root,root) %{_bindir}/pbm2ppa
%attr(755,root,root) %{_bindir}/pbmtpg
%attr(755,root,root) %{_bindir}/calibrate_ppa
%attr(755,root,root) %{_bindir}/test_ppa
%attr(755,root,root) %{_bindir}/detect_ppa
%{_mandir}/man1/pnm2ppa.1*
%{_mandir}/man1/pbm2ppa.1*
%{_libdir}/lpfilters/pnm2ppa-filter-*
%config %{_sysconfdir}/pnm2ppa.conf
%config %{_sysconfdir}/pbm2ppa.conf
