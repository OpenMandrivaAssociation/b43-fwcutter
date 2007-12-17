%define name	b43-fwcutter
%define version	008
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	Tool to extract firmware for Broadcom 43xx network chip
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
Patch0:		%{name}-008-install_perms.patch
URL:		http://bcm43xx.berlios.de/
License:	GPL
Group:		System/Configuration/Networking
#Obsoletes:	bcm43xx-fwcutter

%description
Fwcutter allows you to extract the firmware required for Broadcom 43xx chips
out of the .sys files commonly available with the card or on the internet.

It can extract v3 or v4 firmwares onto b43legacy or b43 folder, or at the 
location of your choice.

Once extracted, place the files in this folder into /lib/firmware.

%prep
%setup -q
%patch -p0
perl -pi -e 's|man/man1|share/man/man1|g' Makefile

%build
%make
										
%install
rm -rf $RPM_BUILD_ROOT
make install PREFIX=%buildroot/%_prefix
cat > README.urpmi <<EOF
You need to extract the firmware your the .sys file provided by your vendor.
i.e b43-fwcutter -w /lib/firmware/ bcmwl5.sys
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README README.urpmi
%{_bindir}/*
%{_mandir}/man1/*


