# $Id: Owl/packages/pam_userpass/pam_userpass/pam_userpass.spec,v 1.3 2000/08/17 23:10:56 solar Exp $

Summary: Pluggable authentication module for USER/PASS-style protocols
Name: pam_userpass
Version: 0.3
Release: 1owl
Copyright: relaxed BSD and (L)GPL-compatible
Group: System Environment/Base
Source: pam_userpass-%{version}.tar.gz
Buildroot: /var/rpm-buildroot/%{name}-%{version}
BuildPreReq: pam >= 0.72-8owl

%description
pam_userpass is a PAM authentication module for use specifically by
services implementing non-interactive protocols and wishing to verify
a username/password pair.  The module doesn't do any actual
authentication, -- other modules, such as pam_pwdb, should be stacked
to provide the authentication.

%prep
%setup -q

%build
make CFLAGS="-c -Iinclude $RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install FAKEROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc LICENSE README
/lib/security/pam_userpass.so

%changelog
* Fri Aug 18 2000 Solar Designer <solar@owl.openwall.com>
- 0.3, added README.

* Sun Jul 09 2000 Solar Designer <solar@owl.openwall.com>
- Initial version.
