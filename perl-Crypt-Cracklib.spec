%define upstream_name    Crypt-Cracklib
%define upstream_version 1.7

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	3

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
