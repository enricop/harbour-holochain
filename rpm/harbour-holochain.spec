Name:       holochain
Summary:    Holochain for SailfishOS build example
Version:    0.6.0
Release:    1
License:    CAL-1.0
URL:        https://www.holochain.org/
Source0:    %{name}-%{version}.tar.bz2

BuildRequires:  git
BuildRequires:  zlib zlib-devel zlib-static bzip2-devel
BuildRequires:  coreutils
BuildRequires:  openssl-libs openssl-devel openssl-static
BuildRequires:  ccache
BuildRequires:  make
BuildRequires:  cmake extra-cmake-modules
BuildRequires:  gcc gcc-c++
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  python3-base
BuildRequires:  libatomic
BuildRequires:  procps
BuildRequires:  clang-devel clang-libs clang-tools-extra clang-tools-extra-devel
BuildRequires:  perl-IPC-Cmd


%description
A minimal example to (cross-)compile an Holochain binary in Sailfish OS.

%define BUILD_DIR "$PWD"/builddir

%define BUILD_TARGET aarch64-unknown-linux-gnu

# - PREP -----------------------------------------------------------------------
%prep
%setup -q -n %{name}-%{version}

mkdir -p "%{BUILD_DIR}"

# - BUILD ----------------------------------------------------------------------
%build

export CARGO_HOME="%{BUILD_DIR}/cargohome"
export CARGO_TARGET_DIR="%{BUILD_DIR}/cargotargetdir"

curl -o rustup-init https://static.rust-lang.org/rustup/dist/aarch64-unknown-linux-gnu/rustup-init

chmod +x rustup-init

./rustup-init -v --default-host aarch64-unknown-linux-gnu -y

source $CARGO_HOME/env

rustc --version

cargo --version

export CARGO_BUILD_TARGET=%{BUILD_TARGET}
export RUST_HOST_TARGET=%{BUILD_TARGET}
export RUST_TARGET=%{BUILD_TARGET}
export TARGET=%{BUILD_TARGET}
export HOST=%{BUILD_TARGET}
export CROSS_COMPILE=%{BUILD_TARGET}

# Set meego cross compilers
export CARGO_TARGET_AARCH64_UNKNOWN_LINUX_GNU_LINKER=aarch64-meego-linux-gnu-gcc
export CC_aarch64_unknown_linux_gnu=aarch64-meego-linux-gnu-gcc
export CXX_aarch64_unknown_linux_gnu=aarch64-meego-linux-gnu-g++
export AR_aarch64_unknown_linux_gnu=aarch64-meego-linux-gnu-ar

cargo install \
          --target aarch64-unknown-linux-gnu \
          holochain@%{version}

# - INSTALL --------------------------------------------------------------------
%install

# - FILES ----------------------------------------------------------------------
%files

%{_bindir}
