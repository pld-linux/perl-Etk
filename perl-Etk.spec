#
# Conditional build:
%bcond_with	tests	# perform "make test" (fails for now)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Etk

%define		_pkgname	etk-perl
Summary:	Perl extention to Etk
Summary(pl.UTF-8):   Rozszerzenie Perla dla Etk
Name:		perl-Etk
Version:	0.01
%define		_snap	20060706
Release:	0.%{_snap}.1
# not specified, should be same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://sparky.homelinux.org/snaps/enli/e17/proto/%{_pkgname}-%{_snap}.tar.bz2
# Source0-md5:	91b0ea2d43c5827184c45a8d8e4db170
URL:		http://enlightenment.org/
BuildRequires:	etk-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl extention to Etk.

%description -l pl.UTF-8
Rozszerzenie Perla dla Etk.

%prep
%setup -q -n %{_pkgname}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a etk_test/* test.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Etk.pm
%{perl_vendorarch}/Etk
%dir %{perl_vendorarch}/auto/Etk
%{perl_vendorarch}/auto/Etk/Etk.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Etk/Etk.so
%{perl_vendorarch}/auto/Etk/autosplit.ix
%{_mandir}/man3/Etk*
%{_examplesdir}/%{name}-%{version}
