Name:           lastpass-cli
Version:        1.0.0
Release:        0
Summary:        LastPass command line interface tool
License:        GPL-2.0
Group:          Productivity/Security
Url:            https://github.com/LastPass/lastpass-cli
Source:         https://github.com/lastpass/lastpass-cli/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc automake
BuildRequires:  openssl-devel libxml2-devel libcurl-devel asciidoc
BuildRequires:  pkgconfig(bash-completion)
Requires:       /usr/bin/pinentry
Requires:       openssl libcurl libxml2 xclip

# /usr/bin/xclip isn't available in EPEL
# %{?fedora:Requires: /usr/bin/xclip}


%description
LastPass is a freemium password management service which stores encrypted
passwords in the cloud. This package provided it's command line interface
tool.

%prep
%setup -q

%build
CFLAGS="${CFLAGS:-%optflags}" LDFLAGS="${LDFLAGS:-%__global_ldflags}" make %{?_smp_mflags}

%install
%make_install install-doc

# Setup bash completion
bashcompdir=$(pkg-config --variable=completionsdir bash-completion)
install -Dpm 644 contrib/lpass_bash_completion %{buildroot}$bashcompdir/lpass


%files
%{_bindir}/lpass
%{_mandir}/man1/lpass.1.*
%license COPYING
%license LICENSE.OpenSSL
%doc README.md
%doc CONTRIBUTING
%doc contrib/examples
%{_datadir}/bash-completion/

%changelog

