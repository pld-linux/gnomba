Summary:	Gnome SMB Browser 
Summary(es):	Explorador SMB para Gnome
Summary(fr):	Explorateur SMB pour Gnome 
Summary(wa):	Foyteuse SMB pol Gnome
Name:		gnomba
Version:	0.6.2
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Group(pl):	X11/Aplikacje/Sieciowe
Icon:		gnomba-logo.xpm
Source0:	http://gnomba.darkcorner.net/tars/%{name}-%{version}.tar.bz2
Source1:	gnomba.desktop
URL:		http://gnomba.darkcorner.net/
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

%description -l wa
gnomba est ene foyteuse grafike po trover des éndjoles Samba ou
Windows sol rantoele locåle. Avou lî vos poloz åjheymint cweri et
monter des pårteyes d' éndjoles windows oudoben eployi leus scrireces.

%prep
%setup -q

%build
./configure --prefix=/usr --sysconfdir=%{_sysconfdir} \
  --datadir=%{_datadir}
%{__make} RPM_OPT_FLAGS="$RPM_OPT_FLAGS"
     
%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
  prefix=$RPM_BUILD_ROOT%{_prefix} \
  sysconfdir=$RPM_BUILD_ROOT%{_sysconfdir} \
  datadir=$RPM_BUILD_ROOT%{_datadir}

install -d %{_applnkdir}/Network/Misc
install %{SOURCE1} %{_applnkdir}/Network/Misc

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README COPYING ChangeLog
%attr(755,root,root) %{_bindir}/gnomba
%{_applnkdir}/Network/Misc/gnomba.desktop
%{_datadir}/pixmaps/*
