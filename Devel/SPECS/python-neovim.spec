%global sum Python client to Neovim
%global desc Implements support for python plugins in Nvim. Also works as a library for\
connecting to and scripting Nvim processes through its msgpack-rpc API.
%if 0%{?fedora} > 21 || 0%{?rhel} > 7
%global with_python3 1
%endif

Name:           python-neovim
Version:        0.2.0
Release:        1%{?dist}

License:        ASL 2.0
Summary:        %{sum}
URL:            https://github.com/neovim/python-client
Source0:        https://github.com/neovim/python-client/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
%if 0%{?with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%endif

%description
%{desc}


%package -n python2-neovim
Summary:        %{sum}
%{?python_provide:%python_provide python2-neovim}
%if 0%{?fedora} <= 23 || 0%{?rhel} <= 7
Requires:       neovim
Requires:       python-greenlet
%else
Requires:       python2-greenlet
%endif
Requires:       python2-msgpack
Requires:       python-trollius

%description -n python2-neovim
%{desc}


%if 0%{?with_python3}
%package -n python3-neovim
Summary:        %{sum}
%{?python_provide:%python_provide python3-neovim}
Requires:       neovim
Requires:       python3-greenlet
Requires:       python3-msgpack

%description -n python3-neovim
%{desc}
%endif


%prep
%autosetup -n python-client-%{version}


%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif


%install
%py2_install
%if 0%{?with_python3}
%py3_install
%endif


%check


%files -n python2-neovim
%defattr(-,root,root,-)
%license LICENSE
%doc README.md
%{python2_sitelib}/*

%if 0%{?with_python3}
%files -n python3-neovim
%defattr(-,root,root,-)
%license LICENSE
%doc README.md
%{python3_sitelib}/*
%endif


%changelog
* Sun Dec 10 2017 David Personette <dperson@gmail.com> - 0.2.0-1
- Upgrade to current version

* Sun Jan 08 2017 David Personette <dperson@gmail.com> - 0.1.12-1
- Changes from fedora upstream
- Upgrade to current version

* Sun Nov 27 2016 David Personette <dperson@gmail.com> - 0.1.11-1
- Upgrade to current version

* Mon Oct 24 2016 David Personette <dperson@gmail.com> - 0.1.10-1
- Upgrade to current version

* Sun Jul 17 2016 David Personette <dperson@gmail.com> - 0.1.9-3
- Fix module deps for python2 / python3 packages

* Mon Jul 04 2016 David Personette <dperson@gmail.com> - 0.1.9-2
- Fix module names on older versions

* Sun Jul 03 2016 David Personette <dperson@gmail.com> - 0.1.9-1
- Initial version