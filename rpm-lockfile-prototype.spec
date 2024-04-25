Name:           rpm-lockfile-prototype
Version:        v0.1.0.alpha.2
Release:        1.20240425133712523089.copr.packaging.3.gb82efbe%{?dist}
Summary:        A proof-of-concept tool that implements most of the requirements for KONFLUX-2110

License:        GPL-3.0-or-later
URL:            https://github.com/konflux-ci/rpm-lockfile-prototype
Source:         rpm-lockfile-prototype-v0.1.0.alpha.2.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
A proof-of-concept tool that implements most of the requirements for KONFLUX-2110.
...}

%description %_description

%prep
%autosetup -p1 -n rpm-lockfile-prototype-v0.1.0.alpha.2


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files rpm_lockfile


%check

%files -f %{pyproject_files}
%doc README.*
%{_bindir}/rpm-lockfile-prototype


%changelog
