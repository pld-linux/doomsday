Summary:	jDoom, jHeretic and jHexen for Linux
Summary(pl):	jDoom, jHeretic i jHexen dla Linuksa
Name:		doomsday
Version:	1.8.5
Release:	0.1
License:	GPL v2
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/deng/deng-%{version}.tar.gz
# Source0-md5:	0e1f34ebddae77315765ce089e88a9f3
Patch0:		%{name}-ncurses.patch
URL:		http://www.doomsdayhq.com/
BuildRequires:	OpenAL-devel
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_net-devel
BuildRequires:	autoconf
BuildRequires:	automake
Requires(post):	/sbin/ldconfig
# it's FUBAR by storing pointers in int struct fields
ExcludeArch:	alpha amd64 ia64 ppc64 s390x sparc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
jDoom, jHeretic and jHexen for Linux.

%description -l pl
jDoom, jHeretic i jHexen dla Linuksa.

%prep
%setup -q -n deng-%{version}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
if [ "$1" = "1" ]; then
	echo "To run doomsday you need some WAD file: either freedoom package"
	echo "or some shareware or commercial WAD from Doom or Heretic:"
	echo "Doom.wad, Doom1.wad, Doom2.wad, Tnt.wad, Plutonia.wad,"
	echo "Heretic.wad or Heretic1.wad."
	echo "When you have them, run doomsday with:"
	echo "doomsday -game [ jdoom | jheretic | jhexen ]"
fi

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc Doc/*
%attr(755,root,root) %{_bindir}/doomsday
%attr(755,root,root) %{_libdir}/*.so.*.*.*
%{_libdir}/*.la
%{_datadir}/deng
