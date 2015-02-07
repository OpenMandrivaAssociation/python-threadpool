Summary:	Easy to use object-oriented thread pool framework
Name:		python-threadpool
Version:	1.2.7
Release:	2
License:	MIT
Group:		Development/Python
URL:		http://chrisarndt.de/projects/threadpool
Source0:	http://chrisarndt.de/projects/threadpool/download/threadpool-%{version}.tar.bz2
BuildRequires:	python2-devel
BuildRequires:	python2-setuptools
BuildArch:	noarch


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
%setup -qn threadpool-%{version}

%build
PYTHONDONTWRITEBYTECODE= %{__python2} setup.py build

%install
PYTHONDONTWRITEBYTECODE= %{__python2} setup.py install --prefix=%{_prefix} --root=%{buildroot}



%files
%doc CHANGELOG.txt README.txt TODO.txt doc/*
%{py2_puresitedir}/*



