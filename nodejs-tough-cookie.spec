%{?scl:%scl_package nodejs-tough-cookie}
%{!?scl:%global pkg_name %{name}}
%global npm_name tough-cookie
%{?nodejs_find_provides_and_requires}

%{!?scl:%global enable_tests 1}

Name:		%{?scl_prefix}nodejs-tough-cookie
Version:	2.3.3
Release:	2%{?dist}
Summary:	RFC6265 Cookies and Cookie Jar for node.js
Url:		https://github.com/SalesforceEng/tough-cookie
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	BSD

BuildArch:	noarch
ExclusiveArch:	%{ix86} x86_64 %{arm} noarch

BuildRequires:	%{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:	npm(async)
BuildRequires:	npm(vows)
%endif

%description
RFC6265 Cookies and Cookie Jar for node.js

%prep
%setup -q -n package

%nodejs_fixdep punycode

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json lib/ \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
vows test/*_test.js
%endif

%files
%{nodejs_sitelib}/tough-cookie

%doc README.md
%doc LICENSE

%changelog
* Mon Oct 02 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.3.3-2
- Resolves: RHBZ#1497695
- fixdep punycode

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.0-2
- rebuilt

* Thu Jul 16 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.0-1
- Initial build
