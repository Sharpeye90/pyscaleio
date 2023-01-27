%global project_name pyscaleio
%global project_description %{expand:
Python library that provides convenient way to interact with ScaleIO/VxFlex REST API.}
%define buildid @BUILDID@
%if 0%{?el8} || 0%{?redos}
%global el_python3_pkgversion 3
%else
%global el_python3_pkgversion 36
%endif

Name:    python-scaleio
Version: 0.1.11
Release: 1.CROC3_REDOS1%{?buildid}%{?dist}
Summary: ScaleIO/VxFlex API client

Group:   Development/Tools
License: Apache Software License 2.0
URL:     https://github.com/gmmephisto/pyscaleio
Source:  https://pypi.python.org/packages/source/p/%project_name/%project_name-%version.tar.gz

BuildArch:     noarch

%description %{project_description}


%package -n python%{python3_pkgversion}-scaleio
Summary: ScaleIO API client
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-setuptools
BuildRequires: python%{el_python3_pkgversion}-six
BuildRequires: python%{el_python3_pkgversion}-pbr

Requires: python%{el_python3_pkgversion}-requests >= 2.3
Requires: python%{python3_pkgversion}-object-validator >= 0.1.4
Requires: python%{python3_pkgversion}-psys >= 0.3
Requires: python%{el_python3_pkgversion}-inflection
Requires: python%{el_python3_pkgversion}-six

%description -n python%{python3_pkgversion}-scaleio %{project_description}

%prep
%setup -q -n %project_name-%version


%build
export PBR_VERSION=%version
%py3_build


%install
[ "%buildroot" = "/" ] || rm -rf "%buildroot"
export PBR_VERSION=%version
%py3_install


%files -n python%{python3_pkgversion}-scaleio
%defattr(-,root,root,-)
%{python3_sitelib}/pyscaleio
%{python3_sitelib}/pyscaleio-%{version}-*.egg-info
%doc ChangeLog README.rst


%clean
[ "%buildroot" = "/" ] || rm -rf "%buildroot"


%changelog
* Fri Dec 30 2022 Andrey Kulaev <akulaev@croc.ru> - 0.1.11-2
- Add support for koji centos 8.4 

* Mon Feb 07 2022 Alexander Chernev  <achernev@croc.ru> - 0.1.11-1
- Add detailes messages to ScaleIOError message
- Update Vtree scheme
- Add volume overwrite method
- Add VTree migration method
- Add parent VTree getter to Volume model
- Add migration info to VTree model
- Add Storage Pool getter to Volume model

* Mon Jan 10 2022 Andrey Kulaev <akulaev@croc.ru> - 0.1.10-1
- Ignore unknown fields in ExportsInfo for SIO 3.6 compatibility

* Mon Nov 15 2021 Andrey Kulaev <akulaev@croc.ru> - 0.1.9-1
- Add storage pool's volumes getter
- Add instance's statistics getter
- Add build id generation to release name
- Add query selected statistics method to base resource

* Mon Sep 13 2021 Andrey Kulaev <akulaev@croc.ru> - 0.1.8-1
- Add methods for consistency group creation and remove
- Use create_snapshots() method in Volume model
- Add consistency group property to Volume model
- Add tests for System model
- Add required 'mediaType' parameter to storage pool

* Tue Feb 19 2019 Mikhail Ushanov <gm.mephisto@gmail.com> - 0.1.7-1
- New version
- Update license information
- Add VxFlex term to project description

* Fri Feb 15 2019 Mikhail Ushanov <gm.mephisto@gmail.com> - 0.1.6-2
- Add RPM package build for python3_other in EPEL

* Tue Jan 08 2019 Mikhail Ushanov <gm.mephisto@gmail.com> - 0.1.6-1
- New version.
- Python3.6 support.
- Build python3 package for epel7

* Tue Jun 20 2017 Mikhail Ushanov <gm.mephisto@gmail.com> - 0.1.5-1
- New version.
- Python3 compatibility fixes.

* Wed Mar 29 2017 Mikhail Ushanov <gm.mephisto@gmail.com> - 0.1.4-1
- New version.
- Update requires version.

* Wed Apr 20 2016 Mikhail Ushanov <gm.mephisto@gmail.com> - 0.1.2-1
- New version.
- Update requires version.

* Tue Apr 19 2016 Mikhail Ushanov <gm.mephisto@gmail.com> - 0.1.1-1
- New version.
- Update spec.

* Tue Apr 12 2016 Mikhail Ushanov <gm.mephisto@gmail.com> - 0.0.1-1
- Initial build.
