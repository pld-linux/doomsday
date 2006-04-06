# TODO
# - icons for desktop files
# - (CVE-2006-1618) http://security.gentoo.org/glsa/glsa-200604-05.xml
Summary:	jDoom, jHeretic and jHexen for Linux
Summary(pl):	jDoom, jHeretic i jHexen dla Linuksa
Name:		doomsday
Version:	1.9.0
Release:	0.beta3.1
License:	GPL v2
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/deng/deng-%{version}-beta3.tar.gz
# Source0-md5:	581fefd6165dd4104b25656a6b9f31b4
Patch0:		%{name}-ncurses.patch
Patch1:		%{name}-runtimedir.patch
URL:		http://www.doomsdayhq.com/
BuildRequires:	OpenAL-devel
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_net-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	rpmbuild(macros) >= 1.213
Requires(post):	/sbin/ldconfig
Requires:		TiMidity++
# it's FUBAR by storing pointers in int struct fields
ExcludeArch:	%{x8664} alpha ia64 ppc64 s390x sparc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
jDoom, jHeretic and jHexen for Linux.

%description -l pl
jDoom, jHeretic i jHexen dla Linuksa.

%prep
%setup -q -n deng-%{version}-beta3
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
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

rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.a

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
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

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc Doc/*
%attr(755,root,root) %{_bindir}/doomsday
%attr(755,root,root) %{_libdir}/*.so.*.*.*
%{_libdir}/*.la
%{_datadir}/deng
%{_desktopdir}/*.desktop
