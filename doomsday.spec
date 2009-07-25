# TODO
# - icons for desktop files
# - (CVE-2006-1618) http://security.gentoo.org/glsa/glsa-200604-05.xml

%define		subver	beta6.4
%define		rel		0.1
Summary:	jDoom, jHeretic and jHexen for Linux
Summary(pl.UTF-8):	jDoom, jHeretic i jHexen dla Linuksa
Name:		doomsday
Version:	1.9.0
Release:	0.%{subver}.%{rel}
License:	GPL v2
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/deng/deng-%{version}-%{subver}.tar.gz
# Source0-md5:	63fdbc11f0473535f7206f62952a1e2e
URL:		http://www.doomsdayhq.com/
BuildRequires:	OpenAL-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_net-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cmake >= 2.4
BuildRequires:	curl-devel
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

cat <<EOF > $RPM_BUILD_ROOT%{_desktopdir}/%{name}-doom.desktop
[Desktop Entry]
Name=Doom
Comment=Doom for linux
Exec=doomsday -game jdoom
#Icon=hexen.png
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
#Icon=heretic.png
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
#Icon=heretic.png
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
