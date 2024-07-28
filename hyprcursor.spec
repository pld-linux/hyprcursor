Summary:	The hyprland cursor format, library and utilities
Name:		hyprcursor
Version:	0.1.9
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/hyprwm/hyprcursor/releases
Source0:	https://github.com/hyprwm/hyprcursor/archive/v%{version}/%{name}-v%{version}.tar.gz
# Source0-md5:	cce0498650dac9d7590ff296e1a85ded
Patch0:		flags.patch
URL:		https://hyprland.org/
BuildRequires:	cairo-devel
BuildRequires:	cmake >= 3.19
BuildRequires:	hyprlang-devel >= 0.4.2
BuildRequires:	librsvg-devel >= 2
BuildRequires:	libstdc++-devel >= 6:11
BuildRequires:	libzip-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	tomlplusplus-devel
Requires:	hyprlang >= 0.4.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hyprutils is a small C++ library for utilities used across the Hypr*
ecosystem.

%package devel
Summary:	Header files for hyprcursor
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Header files for hyprcursor.

%prep
%setup -q
%patch0 -p1

%build
%cmake -B build

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_bindir}/hyprcursor-util
%attr(755,root,root) %{_libdir}/libhyprcursor.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libhyprcursor.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhyprcursor.so
%{_includedir}/hyprcursor
%{_includedir}/hyprcursor.hpp
%{_pkgconfigdir}/hyprcursor.pc
