%define name	b43-fwcutter
%define version	012
%define release %mkrel 3b.1

Name:		%{name}
Summary:	Tool to extract firmware for Broadcom 43xx network chip
Version:	%{version}
Release:	%{release}
# This is beta release but we must include it as it significantly widens number
# of supported devices...
#Source:	http://bu3sch.de/b43/fwcutter/%{name}-%{version}b.tar.bz2
Source:		%{name}-%{version}b.tar.lzma
Patch0:		%{name}-012b-install_perms.patch
URL:		http://linuxwireless.org/en/users/Drivers/b43
#previous site http://bcm43xx.berlios.de/
License:	GPL
Group:		System/Configuration/Networking
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}
#Obsoletes:	bcm43xx-fwcutter

%description
Fwcutter allows you to extract the firmware required for Broadcom 43xx chips
out of the .o files available with the card or on the internet.

Not all versions of the firmwares are supported by this tool.
You can list supported firmwares with :
b43-fwcutter -l

Depending on your chip, you will need a version 3 or 4 firmware.

Useful reading and links to firmwares that can be extracted are available at 
http://linuxwireless.org/en/users/Drivers/b43

Extract (as root) with :
b43-fwcutter -w /lib/firmware wl_apsta_mimo.o OR
b43-fwcutter -w /lib/firmware wl_apsta.o (for LP-PHY cards like BCM4312 only!)

It will create files directly at the required place (in either b43legacy or 
b43 subfolder).

%prep
%setup -q -n fwcutter
%patch0 -p0
perl -pi -e 's|man/man1|share/man/man1|g' Makefile

%build
%make
										
%install
rm -rf $RPM_BUILD_ROOT
make install PREFIX=%buildroot/%_prefix

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%{_bindir}/*
%{_mandir}/man1/*

