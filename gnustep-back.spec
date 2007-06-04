%define name		gnustep-back
%define version		0.12.0
%define release		%mkrel 2

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}-%{version}.tar.bz2
License: 	GPL
Group:		Development/Other
Summary: 	GNUstep Backend package
URL:		http://www.gnustep.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
Requires:	gnustep-base
BuildRequires:	gcc-objc
BuildRequires:	gnustep-make gnustep-base gnustep-gui
BuildRequires:	cups-devel
BuildRequires:	X11-devel
Requires:	gnustep-base gnustep-gui

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
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{_prefix}
make

%install
%makeinstall_std
bzme $RPM_BUILD_ROOT%prefix/System/Library/Documentation/man/man1/*.gz

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, root)
%doc ANNOUNCE COPYING.LIB INSTALL NEWS README 
%_prefix/GNUstep/System/Library/Bundles
%_prefix/GNUstep/System/Library/Documentation/man/man1/*
%_prefix/GNUstep/System/Library/Fonts
%_prefix/GNUstep/System/Tools/*
