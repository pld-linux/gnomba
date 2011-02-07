Summary:	GNOME SMB Browser
Summary(es.UTF-8):	Explorador SMB para GNOME
Summary(fr.UTF-8):	Explorateur SMB pour GNOME
Summary(pl.UTF-8):	Przeglądarka zasobów SMB dla GNOME
Summary(wa.UTF-8):	Foyteuse SMB pol GNOME
Name:		gnomba
Version:	0.6.2
Release:	8
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://gnomba.sourceforge.net/src/%{name}-%{version}.tar.gz
# Source0-md5:	698c40d2755c5b0d467e4de2f2119c0c
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-po.patch
URL:		http://gnomba.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel
BuildRequires:	rpmbuild(macros) >= 1.565
BuildRequires:	sed >= 4.0
Requires:	samba-client >= 2.0.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gnomba is a GUI network browser using the smb protocol. It allows
users to browse workgroups, machines, and shares in a "Network
Neighborhood."

%description -l es.UTF-8
gnomba es un explorador gráfico para buscar máquinas Samba o Windows
en la red local; similar a como funciona con el susodicho.

%description -l fr.UTF-8
gnomba est un explorateur graphique pour trouver les machines Samba ou
Windows du réseau local. Il permets une utilisation semblable à celle
du "Voisinage réseau" de Windows.

%description -l pl.UTF-8
Gnomba jest przeglądarką zasobów sieciowych wykorzystującą protokół
smb. Pozwala na przeglądanie grup, komputerów i zasobów w "Otoczeniu
sieciowym"

%description -l wa.UTF-8
gnomba est ene foyteuse grafike po trover des éndjoles Samba ou
Windows sol rantoele locåle. Avou lî vos poloz åjheymint cweri et
monter des pårteyes d' éndjoles windows oudoben eployi leus scrireces.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%undos gnomba.desktop

%build
rm -rf missing
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make} \
	CODEPAGEDIR="/etc/samba/codepages" \
	LMHOSTSFILE="/etc/samba/lmhosts" \
	DRIVERFILE="/etc/samba/printers.def"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	sysdir=%{_desktopdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog TODO NEWS BUGS AUTHORS
%attr(755,root,root) %{_bindir}/gnomba
%{_desktopdir}/gnomba.desktop
%{_pixmapsdir}/*
%{_mandir}/man1/*
