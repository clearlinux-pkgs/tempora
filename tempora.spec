#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tempora
Version  : 1.11
Release  : 2
URL      : https://files.pythonhosted.org/packages/12/6b/dc2e9370bf3be766302dbd6cd9729e258e875d31a7a21c9f760aaa5b5b5e/tempora-1.11.tar.gz
Source0  : https://files.pythonhosted.org/packages/12/6b/dc2e9370bf3be766302dbd6cd9729e258e875d31a7a21c9f760aaa5b5b5e/tempora-1.11.tar.gz
Summary  : Objects and routines pertaining to date and time (tempora)
Group    : Development/Tools
License  : MIT
Requires: tempora-bin
Requires: tempora-python3
Requires: tempora-python
Requires: Sphinx
Requires: pytest
Requires: pytz
Requires: six
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : setuptools_scm
BuildRequires : setuptools_scm-python
BuildRequires : tox
BuildRequires : virtualenv

%description
.. image:: https://img.shields.io/pypi/v/tempora.svg
:target: https://pypi.org/project/tempora

%package bin
Summary: bin components for the tempora package.
Group: Binaries

%description bin
bin components for the tempora package.


%package python
Summary: python components for the tempora package.
Group: Default
Requires: tempora-python3

%description python
python components for the tempora package.


%package python3
Summary: python3 components for the tempora package.
Group: Default
Requires: python3-core

%description python3
python3 components for the tempora package.


%prep
%setup -q -n tempora-1.11

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1525905877
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/calc-prorate

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
