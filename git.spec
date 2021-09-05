Name:           git
Version:        2.33.0
Release:        0%{?dist}
Summary:        Fast Version Control System

License:        GPLv2
URL:            http://git-scm.com/
Source0:        git.tar.gz

BuildRequires:  automake
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  zlib-devel
BuildRequires:  gettext
BuildRequires:  curl-devel

# Avoid "No build ID note found" error
%undefine _missing_build_ids_terminate_build

%description
Git is a fast, scalable, distributed revision control system with an
unusually rich command set that provides both high-level operations
and full access to internals.

The git rpm installs the core tools with minimal dependencies.  To
install all git packages, including tools for integrating with other
SCMs, install the git-all meta-package.

%prep
%setup -q -n git


%build
make configure
./configure --prefix=/opt
make %{?_smp_mflags}


%install
%make_install


%files
/opt/share/*
/opt/bin/*
/opt/libexec/*

%changelog
