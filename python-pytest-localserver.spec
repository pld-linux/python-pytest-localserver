#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	py.test plugin to test server connections locally
Summary(pl.UTF-8):	Wtyczka py.test do lokalnego testowania połączeń z serwerem
Name:		python-pytest-localserver
Version:	0.5.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-localserver/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-localserver/pytest-localserver-%{version}.tar.gz
# Source0-md5:	431d31cef0ac481f49b3755a3db1996b
URL:		https://pypi.org/project/pytest-localserver/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-pytest >= 2.0.0
BuildRequires:	python-requests
BuildRequires:	python-werkzeug >= 0.10
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest >= 2.0.0
BuildRequires:	python3-requests
BuildRequires:	python3-werkzeug >= 0.10
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pytest-localserver is a plugin for the pytest testing framework which
enables you to test server connections locally.

%description -l pl.UTF-8
pytest-localserver to wtyczka szkieletu testowego pytest, pozwalająca
na lokalne testowanie połączeń z serwerem.

%package -n python3-pytest-localserver
Summary:	py.test plugin to test server connections locally
Summary(pl.UTF-8):	Wtyczka py.test do lokalnego testowania połączeń z serwerem
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-pytest-localserver
pytest-localserver is a plugin for the pytest testing framework which
enables you to test server connections locally.

%description -n python3-pytest-localserver -l pl.UTF-8
pytest-localserver to wtyczka szkieletu testowego pytest, pozwalająca
na lokalne testowanie połączeń z serwerem.

%prep
%setup -q -n pytest-localserver-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README
%{py_sitescriptdir}/pytest_localserver
%{py_sitescriptdir}/pytest_localserver-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pytest-localserver
%defattr(644,root,root,755)
%doc LICENSE README
%{py3_sitescriptdir}/pytest_localserver
%{py3_sitescriptdir}/pytest_localserver-%{version}-py*.egg-info
%endif
