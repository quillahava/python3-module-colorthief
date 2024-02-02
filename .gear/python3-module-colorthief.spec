%define pypi_name colorthief

Name:           python3-module-%pypi_name
Version:        0.2.1
Release:        alt1
Summary:        Python library for extracting colors from images
Group:          Development/Python3

License:        BSD
URL:            https://github.com/fengsp/color-thief-py
Source0:        %{name}-%{version}.tar

BuildRequires(pre): rpm-build-python3
BuildRequires:  python3-dev
BuildRequires:  python3(setuptools)
BuildRequires:  python3(wheel)
Requires: python3-module-Pillow
%py3_provides %pypi_name

BuildArch:      noarch

%description
Python3-colorthief is a library that helps you extract colors from images.

%prep
%setup -v

%build
%pyproject_build

%install
%pyproject_install
install -Dm644 LICENSE %{buildroot}%{_licensedir}/%{name}/LICENSE


%files
%doc README.rst CHANGES
%_licensedir/%name/LICENSE
%python3_sitelibdir/*

%changelog
* Fri Feb 2 2024 Aleksandr A. Voyt <vojtaa@basealt.ru> 0.2.1-alt1
- First package version

