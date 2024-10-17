%define upstream_name    DBIx-Class-Fixtures
%define upstream_version 1.001010

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	Provides fixtures for DBIx-Class-based scripts
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/DBIx/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Accessor::Grouped)
BuildRequires:	perl(Config::Any)
BuildRequires:	perl(DBIx::Class)
BuildRequires:	perl(DBIx::Class::Schema::Loader)
BuildRequires:	perl(Data::Dump::Streamer)
BuildRequires:	perl(Data::Visitor)
BuildRequires:	perl(DateTime)
BuildRequires:	perl(DateTime::Format::MySQL)
BuildRequires:	perl(DateTime::Format::Pg)
BuildRequires:	perl(DateTime::Format::SQLite)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Copy::Recursive)
BuildRequires:	perl(Hash::Merge)
BuildRequires:	perl(JSON::Syck)
BuildRequires:	perl(Path::Class)
BuildRequires:	perl(SQL::Abstract)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
Dump fixtures from source database to filesystem then import to another
database (with same schema) at any time. Use as a constant dataset for running
tests against or for populating development databases when impractical to use
production clones. Describe fixture set using relations and conditions based on
your DBIx::Class schema.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 1.1.10-4mdv2011.0
+ Revision: 654284
- rebuild for updated spec-helper

* Sat Dec 25 2010 Shlomi Fish <shlomif@mandriva.org> 1.1.10-3mdv2011.0
+ Revision: 624956
- Add SQL::Abstract as an explicit dependency
- Removed trailing dot in the summary
- import perl-DBIx-Class-Fixtures

