Summary:	GNUstep Backend package
Name:		gnustep-back
Version:	0.27.0
Release:	2
License:	LGPLv2+
Group:		Development/Other
Url:		https://www.gnustep.org/
Source0:	ftp://ftp.gnustep.org/pub/gnustep/core/%{name}-%{version}.tar.gz

BuildRequires:	gcc-objc
BuildRequires:	gnustep-make
BuildRequires:	freetype-devel
BuildRequires:	fontconfig-devel
BuildRequires:	gnustep-base-devel
BuildRequires:	gnustep-gui-devel
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xmu)
Requires:	gnustep-gui

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

%build
export CC=`gnustep-config --variable=CC`
export CXX=`gnustep-config --variable=CXX`
#define __cputoolize /bin/true
%configure LDFLAGS='-lfontconfig -z muldefs'
%make 

%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

%files
%doc ANNOUNCE COPYING.LIB INSTALL NEWS README 
%{_bindir}/*
%{_libdir}/GNUstep/Bundles/*
%{_libdir}/GNUstep/Fonts
%{_mandir}/man1/*

