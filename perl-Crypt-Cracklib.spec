%define realname   Crypt-Cracklib
%define version    1.4
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Perl interface to Alec Muffett's Cracklib.
Source:     http://www.cpan.org/modules/by-module/Crypt/%{realname}-%{version}.tar.gz
Patch0:     Crypt-Cracklib.fix_path.patch
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Pod::Coverage)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Pod::Coverage)
BuildRequires: libcrack-devel


%description
This is a simple interface to the cracklib library.

%prep
%setup -q -n %{realname}-%{version} 
%patch0 -p0 -b .path

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

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

