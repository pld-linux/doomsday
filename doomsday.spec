# TODO
# - port to use system assimp (doomsday/external/assimp)?
Summary:	jDoom, jHeretic and jHexen for Linux
Summary(pl.UTF-8):	jDoom, jHeretic i jHexen dla Linuksa
Name:		doomsday
Version:	2.1.1
Release:	1
License:	GPL v2 / CC 3.0 (icons)
Group:		Applications/Games
Source0:	http://downloads.sourceforge.net/deng/%{name}-%{version}.tar.gz
# Source0-md5:	f8478e928621c7d708d54ea88a62e9b3
Source1:	http://www.iconarchive.com/icons/3xhumed/mega-games-pack-26/Doom-1-48x48.png
# Source1-md5:	b7b7a9389eba56679e5db65d95c06803
Source2:	http://www.iconarchive.com/icons/3xhumed/mega-games-pack-23/Hexen-1-48x48.png
# Source2-md5:	573845e6e747f68617ac67f3a87dc78e
Source3:	http://www.iconarchive.com/icons/3xhumed/mega-games-pack-28/Heretic-I-1-48x48.png
# Source3-md5:	c89e36c49eabe2846137f313a5250308
Source4:	%{name}-doom.desktop
Source5:	%{name}-heretic.desktop
Source6:	%{name}-hexen.desktop
Patch0:		link.patch
URL:		http://www.dengine.net/
BuildRequires:	Mesa-libEGL-devel
BuildRequires:	OpenGL-devel
BuildRequires:	Qt5Core-devel >= 5.5
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5OpenGL-devel
BuildRequires:	Qt5OpenGLExtensions-devel
BuildRequires:	Qt5X11Extras-devel
BuildRequires:	SDL2-devel
BuildRequires:	SDL2_mixer-devel
BuildRequires:	assimp-devel
BuildRequires:	cmake >= 3.1
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRequires:	python
BuildRequires:	python-modules
BuildRequires:	qt5-build
BuildRequires:	qt5-qmake
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.595
BuildRequires:	xorg-lib-libXrandr-devel
Requires(post):	/sbin/ldconfig
Requires:	TiMidity++
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Doomsday Engine allows you to play the classic first-person
shooters DOOM, Heretic, and Hexen using modern technology, with
hardware accelerated 3D graphics, surround sound and much more.

%description -l pl.UTF-8
jDoom, jHeretic i jHexen dla Linuksa.

%prep
%setup -q
%patch0 -p1

%build
install -d build
cd build
%cmake ../doomsday
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_mandir}/man6}
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# no -devel package. cleanup
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libdeng_*.so
%{__rm} -r $RPM_BUILD_ROOT%{_includedir}
%{__rm} -r $RPM_BUILD_ROOT%{_libdir}/cmake

install -d $RPM_BUILD_ROOT%{_pixmapsdir}
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}/doom.png
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/hexen.png
cp -p %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}/heretic.png

cp -p %{_sourcedir}/%{name}-doom.desktop $RPM_BUILD_ROOT%{_desktopdir}
cp -p %{_sourcedir}/%{name}-hexen.desktop $RPM_BUILD_ROOT%{_desktopdir}
cp -p %{_sourcedir}/%{name}-heretic.desktop $RPM_BUILD_ROOT%{_desktopdir}

cp -p doomsday/doc/output/*.6 $RPM_BUILD_ROOT%{_mandir}/man6

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%banner -o -e %{name} <<-EOF
To run doomsday you need some WAD file: either freedoom package
or some shareware or commercial WAD from Doom or Heretic:
Doom.wad, Doom1.wad, Doom2.wad, Tnt.wad, Plutonia.wad,
Heretic.wad or Heretic1.wad.
When you have them, run doomsday with:
doomsday -game [ jdoom | jheretic | jhexen ]
EOF

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/doomsday
%attr(755,root,root) %{_bindir}/doomsday-2.0.0
%attr(755,root,root) %{_bindir}/doomsdayscript
%attr(755,root,root) %{_bindir}/doomsdayscript-2.0.0
%attr(755,root,root) %{_bindir}/doomsday-server
%attr(755,root,root) %{_bindir}/doomsday-server-2.0.0
%attr(755,root,root) %{_bindir}/doomsday-shell
%attr(755,root,root) %{_bindir}/doomsday-shell-2.0.0
%attr(755,root,root) %{_bindir}/doomsday-shell-text
%attr(755,root,root) %{_bindir}/doomsday-shell-text-2.0.0
%attr(755,root,root) %{_bindir}/md2tool
%attr(755,root,root) %{_bindir}/savegametool
%attr(755,root,root) %{_bindir}/savegametool-2.0.0
%attr(755,root,root) %{_bindir}/texc
%attr(755,root,root) %{_bindir}/wadtool

%attr(755,root,root) %{_libdir}/libdeng_core.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdeng_core.so.2.0
%attr(755,root,root) %{_libdir}/libdeng_appfw.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdeng_appfw.so.2.0
%attr(755,root,root) %{_libdir}/libdeng_doomsday.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdeng_doomsday.so.2.0
%attr(755,root,root) %{_libdir}/libdeng_gamefw.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdeng_gamefw.so.2.0
%attr(755,root,root) %{_libdir}/libdeng_gui.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdeng_gui.so.2.0
%attr(755,root,root) %{_libdir}/libdeng_legacy.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdeng_legacy.so.2.0
%attr(755,root,root) %{_libdir}/libdeng_shell.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdeng_shell.so.2.0

%{_libdir}/doomsday
%{_datadir}/doomsday
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
%{_mandir}/man6/*
