Name:           nobara-update-before-shutdown
Version:        0.0.1
Release:        1%{?dist}
Summary:        Performs all updates if available during the shutdown sequence of Nobara
BuildArch:      noarch

License:        GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
URL:            https://github.com/snooops/nobara-update-before-shutdown
Source0:        %{name}-%{version}.tar.gz

Requires:       bash systemd

%description
A little helper that updates the system before shutdown/reboot/halt.

%prep
%setup -q

%install
# cleanup the build root
rm -rf $RPM_BUILD_ROOT

# installation of the update script
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
cp src/bin/nobara-automatic-update.sh $RPM_BUILD_ROOT/%{_bindir}

# installation of the system service
mkdir -p %{buildroot}/%{_unitdir}

cp src/systemd/update-before-shutdown.service %{buildroot}/%{_unitdir}

# activate the systemd service
systemctl enable update-before-shutdown.service

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/nobara-automatic-update.sh
%{_unitdir}/update-before-shutdown.service 

%changelog
* Tue Nov 26 2024 Snooops <snooops@dns-serve.de>
- First version being packaged
