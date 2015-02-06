%define upstream_name    Crypt-Cracklib
%define upstream_version 1.7

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	5

Summary:    Perl interface to Alec Muffett's Cracklib
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Crypt/%{upstream_name}-%{upstream_version}.tar.gz
Patch0:     Crypt-Cracklib-1.6-fix-path.patch
BuildRequires: libcrack-devel
BuildRequires: perl(Pod::Coverage)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Pod::Coverage)
BuildRequires: perl-devel

BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
This is a simple interface to the cracklib library.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p 1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.700.0-3
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.700.0-2
+ Revision: 680849
- mass rebuild

* Fri Dec 31 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.700.0-1mdv2011.0
+ Revision: 626819
- update to new version 1.7

* Mon Dec 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.600.0-1mdv2011.0
+ Revision: 625379
- new version

* Tue Jul 27 2010 Jérôme Quelin <jquelin@mandriva.org> 1.500.0-1mdv2011.0
+ Revision: 561544
- update to 1.5

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.4-3mdv2011.0
+ Revision: 555712
- rebuild

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.4-2mdv2010.0
+ Revision: 430348
- rebuild

* Thu Aug 07 2008 Olivier Thauvin <nanardon@mandriva.org> 1.4-1mdv2009.0
+ Revision: 265364
- import perl-Crypt-Cracklib


