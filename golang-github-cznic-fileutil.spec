# https://github.com/cznic/fileutil
%global goipath github.com/cznic/fileutil
%global commit  6a051e75936f623600b67c2b1116b6b6c0ffb936

%gometa

Name:           golang-github-cznic-fileutil
Version:        0
Release:        0.11%{?dist}
Summary:        File utility functions for Go
License:        BSD

URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}


%package        devel
Summary:        %{summary}

BuildRequires:  golang(github.com/cznic/mathutil)

%description    devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgesetup


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE
%doc CONTRIBUTORS AUTHORS README


%changelog
* Thu Nov 15 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.11.20180108git6a051e7
- SPEC refresh

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.10.20180108git6a051e7
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Aug 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0-0.9.20180108git6a051e7
- Update to use spec 3.0.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.git6a051e7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.git6a051e7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0-0.6.git6a051e7
- Bump to commit 6a051e7.

* Fri Nov 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0-0.5.git2d566d8
- Bump to commit 2d566d8.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.git90cf820
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git90cf820
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0-0.2.git90cf820
- Bump to upstream 90cf820aafe8f7df39416fdbb932029ff99bd1ab, fixing tests.

* Sat Mar 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0-0.1.gite618435
- First package for Fedora

