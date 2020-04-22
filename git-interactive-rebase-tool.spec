Summary:	Git Interactive Rebase Tool
Name:		git-interactive-rebase-tool
Version:	1.2.1
Release:	1
License:	GPL v2
Group:		Development/Tools
Source0:	https://github.com/MitMaro/git-interactive-rebase-tool/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	cf6ce6096646e68dad0a2dce4e5bc67e
Source1:	%{name}-%{version}-crates.tar.xz
# Source1-md5:	b15f96ff69b843591276cb2af195a28e
URL:		https://github.com/MitMaro/git-interactive-rebase-tool
BuildRequires:	cargo
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	git-core >= 1.7.8
ExclusiveArch:	%{x8664} %{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Terminal based sequence editor for git interactive rebase.

%prep
%setup -q -b1

%build
export CARGO_HOME="$(pwd)/.cargo"
cargo -v build --release --frozen

%install
rm -rf $RPM_BUILD_ROOT
export CARGO_HOME="$(pwd)/.cargo"

cargo -v install --frozen --root $RPM_BUILD_ROOT%{_prefix} --path .
%{__rm} $RPM_BUILD_ROOT%{_prefix}/.crates.toml
%{__rm} $RPM_BUILD_ROOT%{_prefix}/.crates2.json

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/interactive-rebase-tool
