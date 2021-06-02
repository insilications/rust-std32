#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : rust-std32
Version  : 1
Release  : 90
URL      : https://static.rust-lang.org/dist/rust-nightly-i686-unknown-linux-gnu.tar.gz
Source0  : https://static.rust-lang.org/dist/rust-nightly-i686-unknown-linux-gnu.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 GPL-2.0
Requires: rustc-bin
Requires: rustc-data
Requires: rustc-dev
Requires: rustc-doc
Requires: rustc-libexec
Requires: rustc-man
Requires: rustc-staticdev
BuildRequires : gcc
BuildRequires : gcc-abi
BuildRequires : gcc-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-doc
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libs-math
BuildRequires : gcc-libstdc++32
BuildRequires : gcc-libubsan
BuildRequires : gcc-locale
BuildRequires : libgcc1
BuildRequires : libstdc++
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
# Ignore missing build ids
%undefine _missing_build_ids_terminate_build
# Disable automatic requeriments processing
AutoReq: no

%description
# The Rust Programming Language
This is the main source code repository for [Rust]. It contains the compiler,
standard library, and documentation.

%package dev
Summary: dev components for the rust-std32 package.
Group: Development
Provides: rust-std32-devel = %{version}-%{release}
Requires: rust-std32 = %{version}-%{release}
# Disable automatic requeriments processing
AutoReq: no

%description dev
dev components for the rust-std32 package.


%prep
%setup -q -n rust-nightly-i686-unknown-linux-gnu
cd %{_builddir}/rust-nightly-i686-unknown-linux-gnu
pushd ..
cp -a rust-nightly-i686-unknown-linux-gnu build32
popd

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1622621543
pushd ../build32/
## altflags1_32 content
unset LD_LIBRARY_PATH
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -pipe -fPIC -m32 -mstackrealign -march=native -mtune=native"
export CXXFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -fvisibility-inlines-hidden -pipe -fPIC -m32 -mstackrealign -march=native -mtune=native"
export LDFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -pipe -fPIC -m32 -mstackrealign -march=native -mtune=native"
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
unset LD_LIBRARY_PATH
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
#
#global _privatelibs lib.*-[[:xdigit:]]*[.]so.*
#global __provides_exclude ^(%{_privatelibs})$
#global __requires_exclude ^(%{_privatelibs})$
%global _privatelibs lib(.*-[[:xdigit:]]{16}*|rustc.*)[.]so.*
%global __provides_exclude ^(%{_privatelibs})$
%global __requires_exclude ^(%{_privatelibs})$
%global __provides_exclude_from ^(%{_docdir}|%{rustlibdir}/src)/.*$
%global __requires_exclude_from ^(%{_docdir}|%{rustlibdir}/src)/.*$
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
## altflags1_32 end
## make_macro_32 content
echo "Installing..."
## make_macro_32 end
popd

%install
export SOURCE_DATE_EPOCH=1622621543
rm -rf %{buildroot}
## install_macro_32 start
./install.sh --prefix=%{?buildroot:%{buildroot}}/usr/ --disable-ldconfig --components=rust-std-i686-unknown-linux-gnu --without=rust-docs --verbose
# shell completion for bash
# install -dm 0755 %{buildroot}/usr/share/bash-completion/completions
# install -m0644  %{buildroot}/usr/etc/bash_completion.d/cargo %{buildroot}/usr/share/bash-completion/completions/cargo
rm -rf %{buildroot}/usr/etc/bash_completion.d/cargo
#
find %{?buildroot:%{buildroot}} -name "install.log" -exec rm {} \;
find %{?buildroot:%{buildroot}} -type f -name '*manifest-*' -exec sed -i 's/\/builddir\/build\/BUILDROOT\/rust-std32-[0-9]-[0-9]*\.x86_64//g' {} \;
#pushd %{?buildroot:%{buildroot}}
#rg -e "/builddir/build/BUILDROOT/"
#popd
#rust-std32-1-90.x86_64
find %{buildroot}/usr/lib/rustlib/ -maxdepth 1 -type f -exec rm -v '{}' '+'
#-not -name '*.gcno'
## install_macro_32 end

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/lib/rustlib/i686-unknown-linux-gnu/lib/libaddr2line-5cc8de3d1e5a67da.rlib
/usr/lib/rustlib/i686-unknown-linux-gnu/lib/libadler-3ed84e1367c7b39b.rlib
/usr/lib/rustlib/i686-unknown-linux-gnu/lib/liballoc-ded3289de004e67d.rlib
/usr/lib/rustlib/i686-unknown-linux-gnu/lib/libcfg_if-0b66c2fe555d1bdb.rlib
/usr/lib/rustlib/i686-unknown-linux-gnu/lib/libcompiler_builtins-4d19e0927608426e.rlib
/usr/lib/rustlib/i686-unknown-linux-gnu/lib/libcore-8c6a774ee523cd4e.rlib
/usr/lib/rustlib/i686-unknown-linux-gnu/lib/libgetopts-9d872f581b715b2d.rlib
/usr/lib/rustlib/i686-unknown-linux-gnu/lib/libgimli-50544410d3a2d476.rlib
/usr/lib/rustlib/i686-unknown-linux-gnu/lib/libhashbrown-e4c229dd77992e13.rlib
/usr/lib/rustlib/i686-unknown-linux-gnu/lib/liblibc-5f77a339aa632103.rlib
/usr/lib/rustlib/i686-unknown-linux-gnu/lib/libminiz_oxide-66f4f1be094c0687.rlib
/usr/lib/rustlib/i686-unknown-linux-gnu/lib/libobject-1aeb8739acbebdd5.rlib
/usr/lib/rustlib/i686-unknown-linux-gnu/lib/libpanic_abort-39d98581ddfe3453.rlib
/usr/lib/rustlib/i686-unknown-linux-gnu/lib/libpanic_unwind-88ec6adf9a66f315.rlib
/usr/lib/rustlib/i686-unknown-linux-gnu/lib/libproc_macro-c2f44186178e55ee.rlib
/usr/lib/rustlib/i686-unknown-linux-gnu/lib/libprofiler_builtins-fdb27ca74b0e4d1b.rlib
/usr/lib/rustlib/i686-unknown-linux-gnu/lib/librustc_demangle-7b506c520454c747.rlib
/usr/lib/rustlib/i686-unknown-linux-gnu/lib/librustc_std_workspace_alloc-55520f10cabaa786.rlib
/usr/lib/rustlib/i686-unknown-linux-gnu/lib/librustc_std_workspace_core-78ea910a649d75d8.rlib
/usr/lib/rustlib/i686-unknown-linux-gnu/lib/librustc_std_workspace_std-6f2f03d614a9cf5d.rlib
/usr/lib/rustlib/i686-unknown-linux-gnu/lib/libstd-e9090c354dbf5176.rlib
/usr/lib/rustlib/i686-unknown-linux-gnu/lib/libstd-e9090c354dbf5176.so
/usr/lib/rustlib/i686-unknown-linux-gnu/lib/libstd_detect-5658c3ae82fb86bc.rlib
/usr/lib/rustlib/i686-unknown-linux-gnu/lib/libterm-22ff74ce84293ee2.rlib
/usr/lib/rustlib/i686-unknown-linux-gnu/lib/libtest-39dc0ef4df9601a7.rlib
/usr/lib/rustlib/i686-unknown-linux-gnu/lib/libtest-39dc0ef4df9601a7.so
/usr/lib/rustlib/i686-unknown-linux-gnu/lib/libunicode_width-ee4f0a21d4a29d52.rlib
/usr/lib/rustlib/i686-unknown-linux-gnu/lib/libunwind-afe762e7f6fc3081.rlib
