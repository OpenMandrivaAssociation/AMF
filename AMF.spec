Name:           AMF
Version:        1.4.24
Release:        1
Summary:        Advanced Media Framework (AMF) SDK
License:        MIT
URL:            https://gpuopen.com/advanced-media-framework/
Source:         https://github.com/GPUOpen-LibrariesAndSDKs/AMF/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

%description
A lightweight, portable multimedia framework that abstracts away most of the
platform and API-specific details. %{name} is supported on the closed-source
AMDGPU-Pro driver.

%package        devel
Summary:        Development files for %{name}
Suggests:       AMF-docs

%description    devel
A lightweight, portable multimedia framework that abstracts away most of the 
platform and API-specific details. %{name} is supported on the closed-source           
AMDGPU-Pro driver.

The %{name}-devel package contains header files for developing
applications that use %{name}.

%package docs
Summary:        Additional Documentation for the Advanced Media Framework (AMF) SDK
Group:          Documentation/Other

%description docs
This package contains additional documentation provided for the
Advanced Media Framework (AMF) SDK.

%prep
%autosetup -p4

%build

%install
install -dm755 %{buildroot}%{_includedir}/%{name}/components
install -dm755 %{buildroot}%{_includedir}/%{name}/core
install -Dm644 amf/public/include/components/*.h %{buildroot}%{_includedir}/%{name}/components
install -Dm644 amf/public/include/core/*.h %{buildroot}%{_includedir}/%{name}/core

%files devel
%license LICENSE.txt
%doc amf/doc/README.md amf/doc/Readme.txt
%{_includedir}/%{name}/

%files docs
%doc amf/doc/*
