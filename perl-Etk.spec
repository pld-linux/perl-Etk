#
# Conditional build:
%bcond_with	tests	# perform "make test" (fails for now)
#
%define		pdir	Etk
Summary:	Perl bindings for the Enlightened ToolKit (Etk)
Summary(pl.UTF-8):	Wiązanie Perla do ETK - toolkitu Enlightenmenta
Name:		perl-Etk
Version:	0.07
Release:	1
# same as perl 5.8.7 or any later version of perl 5
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Etk/Etk-Perl-%{version}.tar.gz
# Source0-md5:	41aa38a002ea662f8a882191bae442e2
Patch0:		%{name}-api.patch
URL:		http://search.cpan.org/dist/Etk-Perl/
BuildRequires:	etk-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Etk module allows the use of Etk from within Perl. You can use them in
one of two ways, either by using the object oriented approach or
directly by calling the functions (although this is not recommended).

%description -l pl.UTF-8
Moduł Etk pozwala na używanie Etk z poziomu Perla. Można używać go na
dwa sposoby: zorientowany obiektowo albo bezpośrednio wywołując
funkcje (choć nie jest to zalecane).

%prep
%setup -q -n Etk-Perl-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a etk_test/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorarch}/Etk.pm
%{perl_vendorarch}/Etk
%dir %{perl_vendorarch}/auto/Etk
%attr(755,root,root) %{perl_vendorarch}/auto/Etk/Etk.so
%{_mandir}/man3/Etk*.3*
%{_examplesdir}/%{name}-%{version}
