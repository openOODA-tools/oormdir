Name:           oormdir
Version:        0.1.0
Release:        1%{?dist}
Summary:        Safely unlinks empty directory hierarchies with path boundary verification.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oormdir
Source0:        oormdir-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oormdir is a sovereign, capability-bounded EMPTY DIR REMOVER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oormdir
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oormdir-uninstall

%files
/usr/bin/oormdir
/usr/bin/oormdir-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
