Name:           python-ipython
Version:        9.6.0
Release:        %autorelease
Summary:        IPython: Productive Interactive Computing

License:        BSD-3-Clause
URL:            https://ipython.org
Source:         %{pypi_source ipython}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'ipython' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-ipython
Summary:        %{summary}

%description -n python3-ipython %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-ipython all,black,doc,matplotlib,test,test-extra


%prep
%autosetup -p1 -n ipython-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x all,black,doc,matplotlib,test,test-extra


%build
%pyproject_wheel


%install
%pyproject_install
# Add top-level Python module names here as arguments, you can use globs
%pyproject_save_files -l ...


%check
%pyproject_check_import


%files -n python3-ipython -f %{pyproject_files}


%changelog
%autochangelog