Name:           neofetch
Version:        3.4.0
Release:        1%{?dist}
Summary:        CLI system information tool written in Bash

License:        MIT
URL:            https://github.com/dylanaraps/%{name}
Source0:        https://github.com/dylanaraps/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

#BuildArch:      noarch
Requires:       bash >= 3.0
# EPEL packages don't yet have support for weak-dependencies
# https://fedoraproject.org/wiki/Packaging:WeakDependencies#Weak_dependencies
%if 0%{?fedora} >= 23
Recommends:     bind-utils, coreutils, curl, gawk, grep, ImageMagick, lspci
Recommends:     w3m-img, xdotool, xorg-x11-server-utils, xorg-x11-utils
%endif

%description
Neofetch displays information about your system next to an image,
your OS logo, or any ASCII file of your choice. The main purpose of Neofetch
is to be used in screenshots to show other users what OS/distribution you're
running, what theme/icons you're using and more.

%prep
%autosetup
sed 's,/usr/bin/env bash,%{_bindir}/bash,g' -i neofetch

%build

%install
%make_install

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}
%license LICENSE.md
%doc README.md CHANGELOG.md
%{_mandir}/man1/%{name}.1*

%changelog
* Fri Apr 06 2018 Kees de Jong <keesdejong@fedoraproject.org> - 3.4.0-1
- New upstream release

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 13 2017 Kees de Jong <keesdejong@fedoraproject.org> - 3.3.0-1
- Initial package.
