%define name		gnustep-back
%define version		0.18.0
%define release		%mkrel 1

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	ftp://ftp.gnustep.org/pub/gnustep/core/%{name}-%{version}.tar.gz
Patch0:		gnustep-back-0.16.0-fix-str-fmt.patch
License: 	LGPLv2+
Group:		Development/Other
Summary: 	GNUstep Backend package
URL:		http://www.gnustep.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
Requires:	gnustep-gui
BuildRequires:	gcc-objc
BuildRequires:	gnustep-base
BuildRequires:	gnustep-base-devel
BuildRequires:	gnustep-gui-devel
BuildRequires:	libx11-devel
BuildRequires:	GL-devel
BuildRequires:	libxext-devel
BuildRequires:	libxmu-devel
BuildRequires:	freetype2-devel

%description
It is a library of graphical user interface classes written
completely in the Objective-C language; the classes are based
upon the OpenStep specification as released by NeXT Software, Inc.
The library does not completely conform to the specification 
and has been enhanced in a number of ways to take advantage
of the GNU system. These classes include graphical objects
such as buttons, text fields, popup lists, browser lists,
and windows; there are also many associated classes
for handling events, colors, fonts, pasteboards and images.

%prep
%setup -q
%patch0 -p0

%build
%define __cputoolize /bin/true
%configure2_5x
make

%install
rm -fr %buildroot
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, root)
%doc ANNOUNCE COPYING.LIB INSTALL NEWS README 
%_prefix/lib/GNUstep/Bundles/*
%_mandir/man1/*
%_prefix/lib/GNUstep/Fonts
%_bindir/*
