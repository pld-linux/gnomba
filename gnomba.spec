Summary:	Gnome SMB Browser 
Summary(es):	Explorador SMB para Gnome
Summary(fr):	Explorateur SMB pour Gnome 
Summary(pl):	Przegl±darka zasobów SMB
Summary(wa):	Foyteuse SMB pol Gnome
Name:		gnomba
Version:	0.6.2
Release:	2
License:	GPL
Group:		X11/Applications/Networking
Group(pl):	X11/Aplikacje/Sieciowe
Source0:	http://gnomba.darkcorner.net/tars/%{name}-%{version}.tar.gz
Icon:		gnomba-logo.xpm
URL:		http://gnomba.darkcorner.net/
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel
BuildRequires:	automake
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	samba >= 2.0.5

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

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
gettextize --copy --force
aclocal
autoconf
automake -a -c 
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

gzip -9nf README ChangeLog TODO NEWS BUGS AUTHORS

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/gnomba
%{_applnkdir}/Network/Misc/gnomba.desktop
%{_pixmapsdir}/*
%{_mandir}/man1/*
