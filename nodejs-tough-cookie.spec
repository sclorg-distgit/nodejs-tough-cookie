%{?scl:%scl_package nodejs-tough-cookie}
%{!?scl:%global pkg_name %{name}}
%global npm_name tough-cookie
%{?nodejs_find_provides_and_requires}

%{!?scl:%global enable_tests 0}

Name:		%{?scl_prefix}nodejs-tough-cookie
Version:        2.3.2
Release:        3%{?dist}
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

# remove punycode as dependency as it is povided differenly from nodejs package
%nodejs_fixdep punycode -r

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json lib/ %{buildroot}%{nodejs_sitelib}/%{npm_name}

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
* Thu Jan 26 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.3.2-3
- Remove punycode from dependencies (RHBZ#1416815)

* Thu Jan 05 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.3.2-2
- Fixdep punycode

* Thu Jan 05 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.3.2-1
- Updated with script

* Tue Sep 13 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.2.2-1
- Updated with script
- tar has some issues but should be okay

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.0-2
- rebuilt

* Thu Jul 16 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.0-1
- Initial build
