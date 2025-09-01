Summary:	GNUstep Backend package
Name:		gnustep-back
Version:	0.32.0
Release:	1
License:	LGPLv2+
Group:		Development/Other
Url:		https://www.gnustep.org/
#source uses underscores in versioning
Source0:	https://github.com/gnustep/libs-back/archive/refs/tags/back-0_32_0.tar.gz

BuildRequires:	gnustep-make
BuildRequires:	lib64freetype6-devel
BuildRequires:	lib64fontconfig-devel
BuildRequires:  lib64objc-devel
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
%autosetup -p1 -n libs-back-back-0_32_0

%build
export CC=`gnustep-config --variable=CC`
export CXX=`gnustep-config --variable=CXX`
%make_build

%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

%files
%doc ANNOUNCE COPYING.LIB INSTALL NEWS README 
%{_bindir}/*
%{_libdir}/GNUstep/Bundles/*
%{_libdir}/GNUstep/Fonts
%{_mandir}/man1/*
