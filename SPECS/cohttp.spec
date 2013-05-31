Name:           ocaml-cohttp
Version:        0.9.8
Release:        0
Summary:        An HTTP library for OCaml
License:        LGPL
Group:          Development/Other
URL:            https://github.com/mirage/ocaml-cohttp/archive/ocaml-cohttp-0.9.8.tar.gz
Source0:        ocaml-cohttp-0.9.8.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib
# re uri cstruct lwt ounit
Requires:       ocaml ocaml-findlib

%description
An HTTP library for OCaml.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n ocaml-cohttp-ocaml-cohttp-%{version}

%build
ocaml setup.ml -configure --destdir %{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -install

%clean
rm -rf %{buildroot}

%files devel
%defattr(-,root,root)
%doc LICENSE README.md CHANGES
%{_libdir}/ocaml/cohttp/*

%changelog
* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package
