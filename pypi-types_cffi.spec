#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
# autospec version: v21
# autospec commit: 5424026
#
Name     : pypi-types_cffi
Version  : 1.16.0.20241221
Release  : 4
URL      : https://files.pythonhosted.org/packages/5e/00/ecd613293b6c41081b4e5c33bc42ba22a839c493bf8b6ee9480ce3b7a4e8/types_cffi-1.16.0.20241221.tar.gz
Source0  : https://files.pythonhosted.org/packages/5e/00/ecd613293b6c41081b4e5c33bc42ba22a839c493bf8b6ee9480ce3b7a4e8/types_cffi-1.16.0.20241221.tar.gz
Summary  : Typing stubs for cffi
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-types_cffi-license = %{version}-%{release}
Requires: pypi-types_cffi-python = %{version}-%{release}
Requires: pypi-types_cffi-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(types_setuptools)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
## Typing stubs for cffi
This is a [PEP 561](https://peps.python.org/pep-0561/)
type stub package for the [`cffi`](https://foss.heptapod.net/pypy/cffi) package.
It can be used by type-checking tools like
[mypy](https://github.com/python/mypy/),
[pyright](https://github.com/microsoft/pyright),
[pytype](https://github.com/google/pytype/),
[Pyre](https://pyre-check.org/),
PyCharm, etc. to check code that uses `cffi`. This version of
`types-cffi` aims to provide accurate annotations for
`cffi==1.16.*`.

%package license
Summary: license components for the pypi-types_cffi package.
Group: Default

%description license
license components for the pypi-types_cffi package.


%package python
Summary: python components for the pypi-types_cffi package.
Group: Default
Requires: pypi-types_cffi-python3 = %{version}-%{release}

%description python
python components for the pypi-types_cffi package.


%package python3
Summary: python3 components for the pypi-types_cffi package.
Group: Default
Requires: python3-core
Provides: pypi(types_cffi)
Requires: pypi(types_setuptools)

%description python3
python3 components for the pypi-types_cffi package.


%prep
%setup -q -n types_cffi-1.16.0.20241221
cd %{_builddir}/types_cffi-1.16.0.20241221

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1735099972
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-types_cffi
cp %{_builddir}/types_cffi-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-types_cffi/dff786a9b9a95ffbea8a758f43143c45bc64cd66 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-types_cffi/dff786a9b9a95ffbea8a758f43143c45bc64cd66

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
