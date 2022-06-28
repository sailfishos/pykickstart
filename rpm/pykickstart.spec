Name:       pykickstart
Summary:    Python utilities for manipulating kickstart files
Version:    3.25
Release:    1
License:    GPLv2 and MIT
URL:        https://github.com/sailfishos/pykickstart
BuildArch:  noarch
Source0:    %{name}-%{version}.tar.bz2
BuildRequires: gettext
BuildRequires: python3-devel
BuildRequires: python3-setuptools
Requires:   python3-base
Requires:   python3-pykickstart = %{version}-%{release}

%description
Python utilities for manipulating kickstart files.

%package -n python3-pykickstart
Summary:    Python 3 library for manipulating kickstart files.
Requires:   python3-ordered-set
Requires:   python3-requests
Requires:   python3-six

%description -n python3-pykickstart
Python 3 library for manipulating kickstart files.  The binaries are found in
the pykickstart package.

%package -n python3-pykickstart-docs
Summary:    Documentation for Python 3 library for manipulating kickstart files

%description -n python3-pykickstart-docs
Documentation for Python 3 library for manipulating kickstart files.


%prep
%setup -q -n %{name}-%{version}/pykickstart

%build
%py3_build

%install
rm -rf %{buildroot}
%py3_install

%files
%defattr(-,root,root,-)
%license COPYING
%{_bindir}/ksvalidator
%{_bindir}/ksflatten
%{_bindir}/ksverdiff
%{_bindir}/ksshell

%files -n python3-pykickstart
%defattr(-,root,root,-)
%{python3_sitelib}/pykickstart
%{python3_sitelib}/pykickstart*.egg-info

%files -n python3-pykickstart-docs
%defattr(-,root,root,-)
%doc README.rst
%doc data/kickstart.vim
%doc docs/2to3
%{_mandir}/man1/ksflatten.1.gz
%{_mandir}/man1/ksshell.1.gz
%{_mandir}/man1/ksvalidator.1.gz
%{_mandir}/man1/ksverdiff.1.gz
