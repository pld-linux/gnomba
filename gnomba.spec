Summary:	GNOME SMB Browser
Summary(es):	Explorador SMB para GNOME
Summary(fr):	Explorateur SMB pour GNOME
Summary(pl):	Przegl±darka zasobów SMB dla GNOME
Summary(wa):	Foyteuse SMB pol GNOME
Name:		gnomba
Version:	0.6.2
Release:	3
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://gnomba.sourceforge.net/src/%{name}-%{version}.tar.gz
# Source0-md5:	698c40d2755c5b0d467e4de2f2119c0c
Icon:		gnomba-logo.xpm
URL:		http://gnomba.sourceforge.net/
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel
BuildRequires:	automake
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	samba >= 2.0.5


%description
gnomba is a GUI network browser using the smb protocol. It allows
users to browse workgroups, machines, and shares in a "Network
Neighborhood."

%description -l es
gnomba es un explorador gráfico para buscar máquinas Samba o Windows
en la red local; similar a como funciona con el susodicho.

%description -l fr
gnomba est un explorateur graphique pour trouver les machines Samba ou
Windows du réseau local. Il permets une utilisation semblable à celle
du "Voisinage réseau" de Windows.

%description -l pl
Gnomba jest przegl±dark± zasobów sieciowych wykorzystujac± protokó³
smb. Pozwala na przegl±danie grup, komputerów i zasobów w "Otoczeniu
sieciowym"

%description -l wa
gnomba est ene foyteuse grafike po trover des éndjoles Samba ou
Windows sol rantoele locåle. Avou lî vos poloz åjheymint cweri et
monter des pårteyes d' éndjoles windows oudoben eployi leus scrireces.

%prep
%setup -q

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
	sysdir=%{_applnkdir}/Network/Misc

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog TODO NEWS BUGS AUTHORS
%attr(755,root,root) %{_bindir}/gnomba
%{_applnkdir}/Network/Misc/gnomba.desktop
%{_pixmapsdir}/*
%{_mandir}/man1/*
