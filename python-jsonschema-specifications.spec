Summary:	The JSON Schema meta-schemas and vocabularies, exposed as a Registry
Name:		python-jsonschema-specifications
Version:	2023.12.1
Release:	1
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/jsonschema-specifications/
Source0:	https://pypi.org/packages/source/j/jsonschema-specifications/jsonschema_specifications-%{version}.tar.gz
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(hatch-vcs]
BuildRequires:	python%{pyver}dist(pip)

BuildArch:	noarch

%description
JSON support files from the JSON Schema Specifications (metaschemas,
vocabularies, etc.), packaged for runtime access from Python as a
referencing-based Schema Registry.

%files
%{py_sitedir}/jsonschema-specifications
%{py_sitedir}/jsonschema_specifications-*.*-info

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n jsonschema_specifications-%{version}

%build
%py_build

%install
%py_install

