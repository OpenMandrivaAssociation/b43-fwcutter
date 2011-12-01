%define name	b43-fwcutter
%define version	015
%define release %mkrel 1

Name:		%{name}
Summary:	Tool to extract firmware for Broadcom 43xx network chip
Version:	%{version}
Release:	%{release}
Source:		http://bu3sch.de/b43/fwcutter/%{name}-%{version}.tar.bz2
Patch0:		%{name}-015-install.patch
URL:		http://linuxwireless.org/en/users/Drivers/b43
#previous site http://bcm43xx.berlios.de/
License:	BSD
Group:		System/Configuration/Networking
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}
#Obsoletes:	bcm43xx-fwcutter

%description
Fwcutter allows you to extract the firmware required for Broadcom 43xx chips
out of the .o files available with the card or on the Internet.

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
b43 subdirectory).

%prep
%setup -q
%patch0 -p1
#perl -pi -e 's|man/man1|share/man/man1|g' Makefile

%build
%make
										
%install
rm -rf %{buildroot}
make install PREFIX=%buildroot/%_prefix

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%doc COPYING
%{_bindir}/*
%{_mandir}/man1/*

