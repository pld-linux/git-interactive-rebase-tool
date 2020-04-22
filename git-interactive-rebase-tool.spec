Summary:	Git Interactive Rebase Tool
Name:		git-interactive-rebase-tool
Version:	1.2.1
Release:	1
License:	GPL v2
Group:		Development/Tools
Source0:	https://github.com/MitMaro/git-interactive-rebase-tool/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	cf6ce6096646e68dad0a2dce4e5bc67e
URL:		https://github.com/MitMaro/git-interactive-rebase-tool
BuildRequires:	cargo
Requires:	git-core >= 1.7.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Terminal based sequence editor for git interactive rebase.

%prep
%setup -q

%build
cargo -v build --release

%install
rm -rf $RPM_BUILD_ROOT
cargo -v install --root $RPM_BUILD_ROOT%{_prefix} --path $PWD

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/interactive-rebase-tool
