Name:    {{{ git_dir_name }}}
Version: {{{ git_dir_version }}}
Release: 1%{?dist}
Summary: Secure, private, untraceable cryptocurrency
License: BSD
URL:     https://getmonero.org/
VCS:     {{{ git_dir_vcs }}}
Source0: {{{ git_archive }}}

BuildRequires: gcc >= 4.7.3
BuildRequires: cmake >= 3.0.0
BuildRequires: pkgconf
BuildRequires: boost-devel
BuildRequires: openssl-devel
BuildRequires: cppzmq-devel
BuildRequires: lmdb-devel
BuildRequires: unbound-devel
BuildRequires: libsodium-devel
BuildRequires: miniupnpc-devel
BuildRequires: libunwind-devel
BuildRequires: xz-devel
BuildRequires: readline-devel
BuildRequires: ldns-devel
BuildRequires: expat-devel
BuildRequires: gtest-devel
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: git

%description
Monero is a private, secure, untraceable, decentralised digital currency.\
You are your bank, you control your funds, and nobody can trace your transfers\
unless you allow them to do so.

Privacy: Monero uses a cryptographically sound system to allow you to send and\
receive funds without your transactions being easily revealed on the blockchain\
(the ledger of transactions that everyone has). This ensures that your\
purchases, receipts, and all transfers remain absolutely private by default.

Security: Using the power of a distributed peer-to-peer consensus network,\
every transaction on the network is cryptographically secured.\
Individual wallets have a 25 word mnemonic seed that is only displayed once,\
and can be written down to backup the wallet. Wallet files are encrypted with a\
passphrase to ensure they are useless if stolen.

Untraceability: By taking advantage of ring signatures, a special property of a\
certain type of cryptography, Monero is able to ensure that transactions are\
not only untraceable, but have an optional measure of ambiguity that ensures\
that transactions cannot easily be tied back to an individual user or computer.

%package devel
Requires: %{name}%{?_isa} = %{version}-%{release}
Summary: Monery development files

%description devel
%{summary}.

%prep
{{{ git_dir_setup_macro }}}

%build
mkdir -p build
cd build
%cmake -D NO_AES=1 -D CMAKE_BUILD_TYPE=Release ..
make %{?_smp_mflags}

%install
cd build
make install DESTDIR=%{buildroot}

%files
%license LICENSE
%doc CONTRIBUTING.md
%doc README.md
%{_bindir}/monero-blockchain-blackball
%{_bindir}/monero-blockchain-export
%{_bindir}/monero-blockchain-import
%{_bindir}/monero-blockchain-usage
%{_bindir}/monero-gen-trusted-multisig
%{_bindir}/monero-wallet-cli
%{_bindir}/monero-wallet-rpc
%{_bindir}/monerod

%files devel
%license LICENSE
%doc CONTRIBUTING.md
%doc README.md
%{_includedir}/wallet/api/wallet2_api.h

%changelog
{{{ git_dir_changelog }}}
