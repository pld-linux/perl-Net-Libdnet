#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Net
%define	pnam	Libdnet
Summary:	Net::Libdnet - Perl interface to libdnet
Summary(pl.UTF-8):	Net::Libdnet - Perlowy interfejs do libdnet
Name:		perl-Net-Libdnet
Version:	0.99
Release:	1
License:	BSD
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c838677154b730f47f9a5c6b679fe296
URL:		http://search.cpan.org/dist/Net-Libdnet/
BuildRequires:	libdnet-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Class::Gomor)
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::Libdnet - Perl interface to libdnet.

%description -l pl.UTF-8
Net::Libdnet - Perlowy interfejs do libdnet

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%{__cp} -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Net/*.pm
%dir %{perl_vendorarch}/auto/Net/Libdnet
%attr(755,root,root) %{perl_vendorarch}/auto/Net/Libdnet/*.so
%{_bindir}/dnet.pl
%dir %{perl_vendorarch}/Net/Libdnet
%{perl_vendorarch}/Net/Libdnet/*.pm
%dir %{perl_vendorarch}/Net/Libdnet/Entry
%{perl_vendorarch}/Net/Libdnet/Entry/Intf.pm
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
