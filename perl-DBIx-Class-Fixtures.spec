%define upstream_name    DBIx-Class-Fixtures
%define upstream_version 1.001010

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Provides fixtures for DBIx-Class-based scripts.
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/DBIx/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class::Accessor::Grouped)
BuildRequires: perl(Config::Any)
BuildRequires: perl(DBIx::Class)
BuildRequires: perl(DBIx::Class::Schema::Loader)
BuildRequires: perl(Data::Dump::Streamer)
BuildRequires: perl(Data::Visitor)
BuildRequires: perl(DateTime)
BuildRequires: perl(DateTime::Format::MySQL)
BuildRequires: perl(DateTime::Format::Pg)
BuildRequires: perl(DateTime::Format::SQLite)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Copy::Recursive)
BuildRequires: perl(Hash::Merge)
BuildRequires: perl(JSON::Syck)
BuildRequires: perl(Path::Class)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Dump fixtures from source database to filesystem then import to another
database (with same schema) at any time. Use as a constant dataset for running
tests against or for populating development databases when impractical to use
production clones. Describe fixture set using relations and conditions based on
your DBIx::Class schema.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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


