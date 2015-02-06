Summary:	Easy to use object-oriented thread pool framework
Name:		python-threadpool
Version:	1.2.7
Release:	2
License:	MIT
Group:		Development/Python
URL:		http://chrisarndt.de/projects/threadpool
Source0:	http://chrisarndt.de/projects/threadpool/download/threadpool-%{version}.tar.bz2
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A thread pool is an object that maintains a pool of worker threads to perform
time consuming operations in parallel. It assigns jobs to the threads by
putting them in a work request queue, where they are picked up by the next
available thread. This then performs the requested operation in the background
and puts the results in another queue.

The thread pool object can then collect the results from all threads from this
queue as soon as they become available or after all threads have finished their
work. It's then possible to define callbacks to handle each result as it comes
in.

%prep

%setup -q -n threadpool-%{version}

%build
PYTHONDONTWRITEBYTECODE= %{__python} setup.py build

%install
rm -rf %{buildroot}

PYTHONDONTWRITEBYTECODE= %{__python} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGELOG.txt README.txt TODO.txt doc/*
%{py_puresitedir}/*



%changelog
* Wed Mar 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.7-1mdv2011.0
+ Revision: 645589
- import python-threadpool


* Wed Mar 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.7-1mdv2010.2
- initial Mandriva package (for zarafa-msr)
