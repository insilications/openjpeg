#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : openjpeg
Version  : 2.3.1
Release  : 10
URL      : file:///insilications/build/clearlinux/packages/openjpeg/openjpeg-v2.3.1.zip
Source0  : file:///insilications/build/clearlinux/packages/openjpeg/openjpeg-v2.3.1.zip
Source1  : file:///insilications/build/clearlinux/packages/openjpeg/openjpeg-data-20.05.19.zip
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: openjpeg-bin = %{version}-%{release}
Requires: openjpeg-lib = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : curl-dev
BuildRequires : doxygen
BuildRequires : findutils
BuildRequires : glibc-dev
BuildRequires : glibc-staticdev
BuildRequires : kakadu
BuildRequires : kakadu-dev
BuildRequires : lcms2
BuildRequires : lcms2-dev
BuildRequires : lcms2-staticdev
BuildRequires : libpng-dev
BuildRequires : libpng-staticdev
BuildRequires : openjdk11
BuildRequires : openjdk11-dev
BuildRequires : openjdk13
BuildRequires : openjdk13-dev
BuildRequires : pkgconfig(lcms2)
BuildRequires : pkgconfig(zlib)
BuildRequires : tiff-dev
BuildRequires : zlib-dev
BuildRequires : zlib-staticdev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
========================================================================
OpenJPIP software 2.1 ReadMe

%package bin
Summary: bin components for the openjpeg package.
Group: Binaries

%description bin
bin components for the openjpeg package.


%package dev
Summary: dev components for the openjpeg package.
Group: Development
Requires: openjpeg-lib = %{version}-%{release}
Requires: openjpeg-bin = %{version}-%{release}
Provides: openjpeg-devel = %{version}-%{release}
Requires: openjpeg = %{version}-%{release}

%description dev
dev components for the openjpeg package.


%package lib
Summary: lib components for the openjpeg package.
Group: Libraries

%description lib
lib components for the openjpeg package.


%package staticdev
Summary: staticdev components for the openjpeg package.
Group: Default
Requires: openjpeg-dev = %{version}-%{release}

%description staticdev
staticdev components for the openjpeg package.


%prep
%setup -q -n openjpeg-v2.3.1
cd %{_builddir}
unzip -q %{_sourcedir}/openjpeg-data-20.05.19.zip
cd %{_builddir}/openjpeg-v2.3.1
mkdir -p data
cp -r %{_builddir}/openjpeg-data-20.05.19/* %{_builddir}/openjpeg-v2.3.1/data

%build
unset http_proxy
unset https_proxy
unset no_proxy
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1597531162
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags1 content
export CFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe"
# -ffat-lto-objects -fno-PIE -fno-PIE -m64 -no-pie -fpic -fvisibility=hidden -flto-partition=none
# gcc: -feliminate-unused-debug-types -fipa-pta -flto=16 -Wno-error -Wp,-D_REENTRANT -fno-common
export CXXFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe"
#
export FCFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe"
export FFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe"
export CFFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe"
#
export LDFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe"
#
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
#export CCACHE_DISABLE=1
## altflags1 end
%cmake .. -DOPENJPEG_INSTALL_LIB_DIR=lib64 -DBUILD_TESTING=1 -DBUILD_CODEC=1 -DBUILD_UNIT_TESTS=1 -DBUILD_SHARED_LIBS=1 -DBUILD_STATIC_LIBS=1 -DCMAKE_BUILD_TYPE=Release -DBUILD_DOC=0
make  %{?_smp_mflags}  V=1 VERBOSE=1
popd

%check
export LANG=C.UTF-8
unset http_proxy
unset https_proxy
unset no_proxy
V=1 VERBOSE=1 ctest -V

%install
export SOURCE_DATE_EPOCH=1597531162
rm -rf %{buildroot}
pushd clr-build
%make_install
popd
## install_append content
#mkdir -p %{buildroot}/usr/lib64/
#mv %{buildroot}/usr/lib/libopenjp2.so* %{buildroot}/usr/lib64/
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib64/openjpeg-2.3/OpenJPEGConfig.cmake
/usr/lib64/openjpeg-2.3/OpenJPEGTargets-release.cmake
/usr/lib64/openjpeg-2.3/OpenJPEGTargets.cmake

%files bin
%defattr(-,root,root,-)
/usr/bin/opj_compress
/usr/bin/opj_decompress
/usr/bin/opj_dump

%files dev
%defattr(-,root,root,-)
/usr/include/openjpeg-2.3/openjpeg.h
/usr/include/openjpeg-2.3/opj_config.h
/usr/include/openjpeg-2.3/opj_stdint.h
/usr/lib64/libopenjp2.so
/usr/lib64/pkgconfig/libopenjp2.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libopenjp2.so.2.3.1
/usr/lib64/libopenjp2.so.7

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libopenjp2.a
