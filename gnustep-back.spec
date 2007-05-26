%define version		0.9.6
%define name		gnustep-back
%define prefix 		/usr/GNUstep/System

Name: 		%{name}
Version: 	%{version}
Release: 	1mdk
Source: 	%{name}-%{version}.tar.bz2
License: 	GPL
Group:		Development/Other
Summary: 	GNUstep Backend package
URL:		http://www.gnustep.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
Requires:	gnustep-base
BuildRequires:	gnustep-make libgnustep-base-devel cups-devel

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
%setup -q -n %{name}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{prefix}
make

%install
make INSTALL_ROOT_DIR=$RPM_BUILD_ROOT GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{prefix} filelist=yes install

gzip -d $RPM_BUILD_ROOT%prefix/Library/Documentation/man/man1/*.gz
bzip2 $RPM_BUILD_ROOT%prefix/Library/Documentation/man/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, root)
%doc ANNOUNCE COPYING.LIB
%doc INSTALL NEWS README 
%prefix/Library/Bundles/libgnustep-back.bundle
%prefix/Library/Documentation/man/man1/
%prefix/Library/Fonts/Helvetica.nfont/
%prefix/Tools/*
