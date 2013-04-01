%define name		gnustep-back

Name: 		%{name}
Version: 	0.23.0
Release: 	1
Source: 	ftp://ftp.gnustep.org:21/pub/gnustep/core/%{name}-%{version}.tar.gz
Patch0:		gnustep-back-0.16.0-fix-str-fmt.patch
License: 	LGPLv2+
Group:		Development/Other
Summary: 	GNUstep Backend package
URL:		http://www.gnustep.org/
Requires:	gnustep-gui
BuildRequires:	gcc-objc
BuildRequires:	gnustep-base
BuildRequires:	gnustep-base-devel
BuildRequires:	gnustep-gui-devel
BuildRequires:	libx11-devel
BuildRequires:	GL-devel
BuildRequires:	libxext-devel
BuildRequires:	libxmu-devel
BuildRequires:	freetype-devel

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
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

%files
%defattr (-, root, root)
%doc ANNOUNCE COPYING.LIB INSTALL NEWS README 
%_libdir/GNUstep/Bundles/*
%_mandir/man1/*
%_libdir/GNUstep/Fonts
%_bindir/*


%changelog
* Tue Aug 03 2010 Funda Wang <fwang@mandriva.org> 0.18.0-1mdv2011.0
+ Revision: 565362
- New version 0.18.0

* Thu Jan 08 2009 Funda Wang <fwang@mandriva.org> 0.16.0-1mdv2009.1
+ Revision: 327016
- fix str fmt
- New version 0.16.0

* Wed Aug 20 2008 Funda Wang <fwang@mandriva.org> 0.14.0-3mdv2009.0
+ Revision: 274290
- rebuild for new gnustep-base
- spec cleanup

* Fri Jun 20 2008 Franck Villaume <fvill@mandriva.com> 0.14.0-1mdv2009.0
+ Revision: 227537
- new stable version 0.14.0

* Tue Jun 03 2008 Franck Villaume <fvill@mandriva.com> 0.13.2-1mdv2009.0
+ Revision: 214514
- new version 0.13.2

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.12.0-3mdv2008.1
+ Revision: 136456
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Jul 25 2007 Austin Acton <austin@mandriva.org> 0.12.0-3mdv2008.0
+ Revision: 55131
- buildrequires gnustep-base
- update for new layout
- drop redundant requires

* Mon Jun 04 2007 Austin Acton <austin@mandriva.org> 0.12.0-2mdv2008.0
+ Revision: 34990
- increment release
- fix buildrequires
- redo it all

  + Adam Williamson <awilliamson@mandriva.org>
    - Import gnustep-back




* Tue May 10 2005 Lenny Cartier <lenny@mandriva.com> 0.9.6-1mdk
- new

