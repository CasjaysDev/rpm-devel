%global debug_package %{nil}

%global pypi_name colorama

#%if 0%{?rhel} && 0%{?rhel} <= 7
%bcond_with python3
#%else
#%bcond_without python3
#%endif

Name:           python-%{pypi_name}
Version:        0.3.2
Release:        3%{?dist}
Summary:        Cross-platform colored terminal text

License:        BSD
URL:            http://pypi.python.org/pypi/colorama/
Source0:        http://pypi.python.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python2-setuptools
BuildRequires:  python2-devel
%if %{with python3}
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
%endif # with python3

%description
The aim of the colorama module is to simplify the usage of coloramas for
the average programmer, and to popularize coloramas usage giving examples
of useful coloramas, such as memoize, tracing, redirecting_stdout, locked,
etc.  The core of this module is a colorama factory called colorama.

%package -n python2-colorama
Summary:        Module to simplify usage of coloramas in python2
%{?python_provide:%python_provide python2-colorama}

%description -n python2-colorama
The aim of the colorama module is to simplify the usage of coloramas for
the average programmer, and to popularize coloramas usage giving examples
of useful coloramas, such as memoize, tracing, redirecting_stdout, locked,
etc.  The core of this module is a colorama factory called colorama.

%if %{with python3}
%package -n python3-colorama
Summary:        Module to simplify usage of coloramas in python3
%{?python_provide:%python_provide python3-colorama}

%description -n python3-colorama
The aim of the colorama module is to simplify the usage of coloramas for
the average programmer, and to popularize coloramas usage giving examples
of useful coloramas, such as memoize, tracing, redirecting_stdout, locked,
etc.  The core of this module is a colorama factory called colorama.
%endif # with python3

%prep
%autosetup -n %{pypi_name}-%{version}
find -type f -executable -exec sed -i '1s=^#!/usr/bin/\(python\|env python\)[23]\?=#!%{__python2}=' {} +


%build
%py2_build
%if %{with python3}
%py3_build
%endif # with python3

%install
%py2_install
%if %{with python3}
%py3_install
%endif # with python3
find %{buildroot} -name SOURCES.txt~ -exec rm -f {} \;

%check
%{__python2} setup.py test
%if %{with python3}
%{__python3} setup.py test
%endif # with python3

%files -n python2-%{pypi_name}
%doc README*
%license LICENSE.txt
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%if %{with python3}
%files -n python3-%{pypi_name}
%doc README*
%license LICENSE.txt
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif # with python3

%changelog
* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python2.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Sep 05 2014 Matthias Runge <mrunge@redhat.com> - 0.3.2-1
- update to 0.3.2 (rhbz#1090014)

* Fri Jul 25 2014 Lubomir Rintel <lkundrak@v3.sk> - 0.2.7-5
- Skip the python2 %%files section if we don't build the python2 package

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Wed Mar 12 2014 Matthias Runge <mrunge@redhat.com> - 0.2.7-2
- introduce python2 package (rhbz#1075410)

* Mon Sep 30 2013 Matthias Rugne <mrunge@redhat.com> - 0.2.7-1
- uddate to 0.2.7 (rhbz#1010924)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 22 2013 Matthias Runge <mrunge@redhat.com> - 0.2.5-1
- update to 0.2.5 (rhbz#913431)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Sep 11 2012 Matthias Runge <mrunge@redhat.com> - 0.2.4-1
- Initial package.

