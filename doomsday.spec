# TODO
# - sync pl
# - cleen up spec
%define		subver	stable
Summary:	jDoom, jHeretic and jHexen for Linux
Summary(pl.UTF-8):	jDoom, jHeretic i jHexen dla Linuksa
Name:		doomsday
Version:	1.15.4
Release:	0.1
License:	GPL v2 / CC 3.0 (icons)
Group:		Applications/Games
Source0:	http://downloads.sourceforge.net/deng/%{name}-%{subver}-%{version}.tar.gz
# Source0-md5:	8329eacdea73edca7aea4034ca8d78aa
Source1:	http://www.iconarchive.com/icons/3xhumed/mega-games-pack-26/Doom-1-48x48.png
# Source1-md5:	b7b7a9389eba56679e5db65d95c06803
Source2:	http://www.iconarchive.com/icons/3xhumed/mega-games-pack-23/Hexen-1-48x48.png
# Source2-md5:	573845e6e747f68617ac67f3a87dc78e
Source3:	http://www.iconarchive.com/icons/3xhumed/mega-games-pack-28/Heretic-I-1-48x48.png
# Source3-md5:	c89e36c49eabe2846137f313a5250308
Patch0:		%{name}-libpng15.patch
Patch1:		%{name}-format.patch
URL:		http://www.dengine.net/
BuildRequires:	OpenAL-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
BuildRequires:	SDL2-devel
BuildRequires:	SDL2_mixer-devel
BuildRequires:	qt4-qmake
BuildRequires:	assimp-devel
BuildRequires:	curl-devel
BuildRequires:	libpng-devel
BuildRequires:	ncurses-devel
BuildRequires:	python
BuildRequires:	python-modules
BuildRequires:	rpmbuild(macros) >= 1.595
Requires:	TiMidity++
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Doomsday Engine allows you to play the classic first-person
shooters DOOM, Heretic, and Hexen using modern technology, with
hardware accelerated 3D graphics, surround sound and much more.

%description -l pl.UTF-8
jDoom, jHeretic i jHexen dla Linuksa.

%prep
%setup -q -n doomsday-%{subver}-%{version}
#%patch0 -p1
#%patch1 -p1

%build
install -d build
cd build
LDFLAGS="-lm"
qmake-qt4 CONFIG+=deng_notools \
	-r ../doomsday/doomsday.pro
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}
%{__make} -C build install INSTALL_ROOT=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_pixmapsdir}
cp -a %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}/doom.png
cp -a %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/hexen.png
cp -a %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}/heretic.png

cat <<EOF > $RPM_BUILD_ROOT%{_desktopdir}/%{name}-doom.desktop
[Desktop Entry]
Name=Doom
Comment=Doom for linux
Exec=doomsday -game jdoom
Icon=doom.png
Terminal=false
Type=Application
Categories=Game;FirstPersonGame;
Encoding=UTF-8
EOF

cat <<EOF > $RPM_BUILD_ROOT%{_desktopdir}/%{name}-hexen.desktop
[Desktop Entry]
Name=Hexen
Comment=Hexen for linux
Exec=doomsday -game jhexen
Icon=hexen.png
Terminal=false
Type=Application
Categories=Game;FirstPersonGame;
Encoding=UTF-8
EOF

cat <<EOF > $RPM_BUILD_ROOT%{_desktopdir}/%{name}-heretic.desktop
[Desktop Entry]
Name=Heretic
Comment=Heretic for linux
Exec=doomsday -game jheretic
Icon=heretic.png
Terminal=false
Type=Application
Categories=Game;FirstPersonGame;
Encoding=UTF-8
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
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
#%doc doomsday/build/README
%attr(755,root,root) %{_bindir}/doomsday
%attr(755,root,root) %{_bindir}/doomsday-server
%attr(755,root,root) %{_bindir}/launch-doomsday

%attr(755,root,root) %{_libdir}/libdeng_core.so.2.0.0
%attr(755,root,root) %ghost %{_libdir}/libdeng_core.so.2
%attr(755,root,root) %{_libdir}/libdeng_appfw.so.1.15.4
%attr(755,root,root) %ghost %{_libdir}/libdeng_appfw.so.1
%attr(755,root,root) %{_libdir}/libdeng_doomsday.so.1.15.4
%attr(755,root,root) %ghost %{_libdir}/libdeng_doomsday.so.1
%attr(755,root,root) %{_libdir}/libdeng_gui.so.1.15.4
%attr(755,root,root) %ghost %{_libdir}/libdeng_gui.so.1
%attr(755,root,root) %{_libdir}/libdeng_legacy.so.1.15.4
%attr(755,root,root) %ghost %{_libdir}/libdeng_legacy.so.1
%attr(755,root,root) %{_libdir}/libdeng_shell.so.1.15.4
%attr(755,root,root) %ghost %{_libdir}/libdeng_shell.so.1

%{_libdir}/doomsday
%{_datadir}/doomsday
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
%{_mandir}/man6/*

