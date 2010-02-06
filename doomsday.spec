# TODO
# - icons for desktop files

%define		subver	beta6.7
%define		rel		2
Summary:	jDoom, jHeretic and jHexen for Linux
Summary(pl.UTF-8):	jDoom, jHeretic i jHexen dla Linuksa
Name:		doomsday
Version:	1.9.0
Release:	0.%{subver}.%{rel}
License:	GPL v2 / CC 3.0 (icons)
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/project/deng/Doomsday%20Engine/%{version}-%{subver}/deng-%{version}-%{subver}.tar.gz
# Source0-md5:	9c706df9a3f078b9b62af842e09b088e
Source1:	http://www.iconarchive.com/icons/3xhumed/mega-games-pack-26/Doom-1-48x48.png
# Source1-md5:	b7b7a9389eba56679e5db65d95c06803
Source2:	http://www.iconarchive.com/icons/3xhumed/mega-games-pack-23/Hexen-1-48x48.png
# Source2-md5:	573845e6e747f68617ac67f3a87dc78e
Source3:	http://www.iconarchive.com/icons/3xhumed/mega-games-pack-28/Heretic-I-1-48x48.png
# Source3-md5:	c89e36c49eabe2846137f313a5250308
URL:		http://www.doomsdayhq.com/
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
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRequires:	zip
Requires:	TiMidity++
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
jDoom, jHeretic and jHexen for Linux.

%description -l pl.UTF-8
jDoom, jHeretic i jHexen dla Linuksa.

%prep
%setup -q -n deng-%{version}-%{subver}

%build
install -d build
cd build
%cmake \
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
# vi: encoding=utf-8
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
# vi: encoding=utf-8
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
# vi: encoding=utf-8
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ "$1" = "1" ]; then
	%banner -e %{name} <<-EOF
	To run doomsday you need some WAD file: either freedoom package
	or some shareware or commercial WAD from Doom or Heretic:
	Doom.wad, Doom1.wad, Doom2.wad, Tnt.wad, Plutonia.wad,
	Heretic.wad or Heretic1.wad.
	When you have them, run doomsday with:
	doomsday -game [ jdoom | jheretic | jhexen ]
EOF
fi

%files
%defattr(644,root,root,755)
%doc doomsday/build/README
%attr(755,root,root) %{_bindir}/doomsday
%attr(755,root,root) %{_libdir}/libdpdehread.so
%attr(755,root,root) %{_libdir}/libdpwadmapconverter.so
%attr(755,root,root) %{_libdir}/libjdoom.so
%attr(755,root,root) %{_libdir}/libjheretic.so
%attr(755,root,root) %{_libdir}/libjhexen.so
%{_datadir}/deng
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
