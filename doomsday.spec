# TODO
# - sync pl
%define		subver	beta6.9
%define		rel		1
Summary:	jDoom, jHeretic and jHexen for Linux
Summary(pl.UTF-8):	jDoom, jHeretic i jHexen dla Linuksa
Name:		doomsday
Version:	1.9.0
Release:	0.%{subver}.%{rel}
License:	GPL v2 / CC 3.0 (icons)
Group:		Applications/Games
Source0:	http://downloads.sourceforge.net/deng/deng-%{version}-%{subver}.tar.gz
# Source0-md5:	907ef41b70e2dbf148ef7e4a0350c6bd
Source1:	http://www.iconarchive.com/icons/3xhumed/mega-games-pack-26/Doom-1-48x48.png
# Source1-md5:	24783c4c52c9fdf762a73f70b6406e63
Source2:	http://www.iconarchive.com/icons/3xhumed/mega-games-pack-23/Hexen-1-48x48.png
# Source2-md5:	24783c4c52c9fdf762a73f70b6406e63
Source3:	http://www.iconarchive.com/icons/3xhumed/mega-games-pack-28/Heretic-I-1-48x48.png
# Source3-md5:	24783c4c52c9fdf762a73f70b6406e63
URL:		http://www.dengine.net/
BuildRequires:	OpenAL-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_net-devel
BuildRequires:	cmake >= 2.4
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
%setup -q -n deng-%{version}-%{subver}

%build
install -d build
cd build
LDFLAGS="-lm"
%cmake \
	-DBUILDOPENAL=1 \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DCURSES_INCLUDE_PATH=/usr/include/ncurses \
	-Dlibdir=%{_libdir} \
	../doomsday
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

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

%post
%banner -o -e %{name} <<-EOF
To run doomsday you need some WAD file: either freedoom package
or some shareware or commercial WAD from Doom or Heretic:
Doom.wad, Doom1.wad, Doom2.wad, Tnt.wad, Plutonia.wad,
Heretic.wad or Heretic1.wad.
When you have them, run doomsday with:
doomsday -game [ jdoom | jheretic | jhexen ]
EOF

%files
%defattr(644,root,root,755)
%doc doomsday/build/README
%attr(755,root,root) %{_bindir}/doomsday
%attr(755,root,root) %{_libdir}/libdpdehread.so
%attr(755,root,root) %{_libdir}/libdpwadmapconverter.so
%attr(755,root,root) %{_libdir}/libjdoom.so
%attr(755,root,root) %{_libdir}/libjheretic.so
%attr(755,root,root) %{_libdir}/libjhexen.so
%attr(755,root,root) %{_libdir}/libdsopenal.so
%{_datadir}/deng
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
