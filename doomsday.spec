Summary:	jDoom, jHeretic and jHexen for Linux
Summary(pl.UTF-8):	jDoom, jHeretic i jHexen dla Linuksa
Name:		doomsday
Version:	2.3.1
Release:	2
License:	GPL v2 / CC 3.0 (icons)
Group:		Applications/Games
Source0:	http://downloads.sourceforge.net/deng/%{name}-%{version}.tar.gz
# Source0-md5:	9ae2a3e053a6f11f37dfb450bb5e53cb
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
BuildRequires:	OpenAL-devel
BuildRequires:	OpenGL-devel >= 3.3
BuildRequires:	Qt5Core-devel >= 5.5
BuildRequires:	Qt5Gui-devel >= 5.5
BuildRequires:	Qt5Network-devel >= 5.5
BuildRequires:	Qt5OpenGL-devel >= 5.5
BuildRequires:	Qt5OpenGLExtensions-devel >= 5.5
BuildRequires:	Qt5Widgets-devel >= 5.5
BuildRequires:	Qt5X11Extras-devel >= 5.5
BuildRequires:	SDL2-devel >= 2.0
BuildRequires:	SDL2_mixer-devel >= 2.0
BuildRequires:	assimp-devel
BuildRequires:	cmake >= 3.1
BuildRequires:	fluidsynth-devel
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	minizip-devel >= 1.2.11
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3.2
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	qt5-build >= 5.5
BuildRequires:	qt5-qmake >= 5.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRequires:	zlib-devel
Requires(post):	/sbin/ldconfig
Requires:	TiMidity++
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Doomsday Engine allows you to play the classic first-person
shooters DOOM, Heretic, and Hexen using modern technology, with
hardware accelerated 3D graphics, surround sound and much more.

%description -l pl.UTF-8
Silnik Doomsday pozwala grać w klasyczne strzelaniny FPP, takie
jak DOOM, Heretic i Hexen przy użyciu współczesnej technologii,
ze sprzętowo akcelerowaną grafiką 3D, dźwiękiem surround itp.

%prep
%setup -q
%patch -P0 -p1

%build
install -d build
cd build
%cmake ../doomsday \
	-DDENG_ASSIMP_EMBEDDED=OFF

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_mandir}/man6}

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/texc
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

cp -p doomsday/doc/*.6 $RPM_BUILD_ROOT%{_mandir}/man6

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
%attr(755,root,root) %{_bindir}/doomsday-%{version}
%attr(755,root,root) %{_bindir}/doomsdayscript
%attr(755,root,root) %{_bindir}/doomsdayscript-%{version}
%attr(755,root,root) %{_bindir}/doomsday-server
%attr(755,root,root) %{_bindir}/doomsday-server-%{version}
%attr(755,root,root) %{_bindir}/doomsday-shell
%attr(755,root,root) %{_bindir}/doomsday-shell-%{version}
%attr(755,root,root) %{_bindir}/doomsday-shell-text
%attr(755,root,root) %{_bindir}/doomsday-shell-text-%{version}
%attr(755,root,root) %{_bindir}/md2tool
%attr(755,root,root) %{_bindir}/savegametool
%attr(755,root,root) %{_bindir}/savegametool-%{version}
%attr(755,root,root) %{_bindir}/texc
%attr(755,root,root) %{_bindir}/wadtool

%attr(755,root,root) %{_libdir}/libdeng_core.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdeng_core.so.2.3
%attr(755,root,root) %{_libdir}/libdeng_appfw.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdeng_appfw.so.2.3
%attr(755,root,root) %{_libdir}/libdeng_doomsday.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdeng_doomsday.so.2.3
%attr(755,root,root) %{_libdir}/libdeng_gamefw.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdeng_gamefw.so.2.3
%attr(755,root,root) %{_libdir}/libdeng_gui.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdeng_gui.so.2.3
%attr(755,root,root) %{_libdir}/libdeng_legacy.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdeng_legacy.so.2.3
%attr(755,root,root) %{_libdir}/libdeng_shell.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdeng_shell.so.2.3

%{_libdir}/doomsday
%{_datadir}/doomsday
%{_datadir}/metainfo/net.dengine.Doomsday.appdata.xml
%{_desktopdir}/doomsday-doom.desktop
%{_desktopdir}/doomsday-heretic.desktop
%{_desktopdir}/doomsday-hexen.desktop
%{_desktopdir}/net.dengine.Doomsday.desktop
%{_desktopdir}/net.dengine.Shell.desktop
%{_iconsdir}/hicolor/256x256/apps/net.dengine.Doomsday.png
%{_pixmapsdir}/doom.png
%{_pixmapsdir}/heretic.png
%{_pixmapsdir}/hexen.png
%{_mandir}/man6/doomsday.6*
%{_mandir}/man6/doomsday-server.6*
%{_mandir}/man6/doomsday-shell-text.6*
