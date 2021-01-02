# ALL Rust libraries are private, because they don't keep an ABI.
%global _privatelibs lib.*-[[:xdigit:]]*[.]so.*
%global __provides_exclude ^(%{_privatelibs})$
%global __requires_exclude ^(%{_privatelibs})$

# While we don't want to encourage dynamic linking to Rust shared libraries, as
# there's no stable ABI, we still need the unallocated metadata (.rustc) to
# support custom-derive plugins like #[proc_macro_derive(Foo)].  But eu-strip is
# very eager by default, so we have to limit it to -g, only debugging symbols.
%global _find_debuginfo_opts -g

Name     : rust-std32
Version  : 1.49.0
Release  : 19
URL      : https://www.rust-lang.org
Source0  : https://static.rust-lang.org/dist/rust-std-1.49.0-i586-unknown-linux-gnu.tar.xz
Summary  : The Rust Standard Library
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause ISC MIT

%description
Rust is a systems programming language that runs blazingly fast, prevents
segfaults, and guarantees thread safety.

%prep
%setup -q -n rust-std-%{version}-i586-unknown-linux-gnu

%install
mkdir -p %{buildroot}/usr/lib64/
cp -a rust-std-i586-unknown-linux-gnu/lib/rustlib %{buildroot}/usr/lib64/

# The shared libraries should be executable for debuginfo extraction.
find %{buildroot}/usr/lib64/rustlib/ -type f -name '*.so' -exec chmod -v +x '{}' '+'

%files
/usr/lib64/rustlib/i586-unknown-linux-gnu/lib/*.rlib
/usr/lib64/rustlib/i586-unknown-linux-gnu/lib/*.so
