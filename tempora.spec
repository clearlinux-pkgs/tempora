#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tempora
Version  : 4.1.2
Release  : 41
URL      : https://files.pythonhosted.org/packages/86/4e/9af10e9b896c70ac6e817ac317107f96efbe0b435c4918edd5bf6fcaa330/tempora-4.1.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/86/4e/9af10e9b896c70ac6e817ac317107f96efbe0b435c4918edd5bf6fcaa330/tempora-4.1.2.tar.gz
Summary  : Objects and routines pertaining to date and time (tempora)
Group    : Development/Tools
License  : MIT
Requires: tempora-bin = %{version}-%{release}
Requires: tempora-license = %{version}-%{release}
Requires: tempora-python = %{version}-%{release}
Requires: tempora-python3 = %{version}-%{release}
Requires: jaraco.functools
Requires: pytz
BuildRequires : buildreq-distutils3
BuildRequires : jaraco.functools
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : pytz
BuildRequires : setuptools_scm
BuildRequires : tox
BuildRequires : virtualenv

%description
.. image:: https://img.shields.io/pypi/v/tempora.svg
:target: `PyPI link`_
.. image:: https://img.shields.io/pypi/pyversions/tempora.svg
:target: `PyPI link`_

%package bin
Summary: bin components for the tempora package.
Group: Binaries
Requires: tempora-license = %{version}-%{release}

%description bin
bin components for the tempora package.


%package license
Summary: license components for the tempora package.
Group: Default

%description license
license components for the tempora package.


%package python
Summary: python components for the tempora package.
Group: Default
Requires: tempora-python3 = %{version}-%{release}

%description python
python components for the tempora package.


%package python3
Summary: python3 components for the tempora package.
Group: Default
Requires: python3-core
Provides: pypi(tempora)
Requires: pypi(jaraco.functools)
Requires: pypi(pytz)

%description python3
python3 components for the tempora package.


%prep
%setup -q -n tempora-4.1.2
cd %{_builddir}/tempora-4.1.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1633723627
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/tempora
cp %{_builddir}/tempora-4.1.2/LICENSE %{buildroot}/usr/share/package-licenses/tempora/8e6689d37f82d5617b7f7f7232c94024d41066d1
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/calc-prorate

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/tempora/8e6689d37f82d5617b7f7f7232c94024d41066d1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
