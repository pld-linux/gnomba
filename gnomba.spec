%define ver 0.5.1
%define rel 1mdk

Summary: Gnome SMB Browser 
Summary(es): Explorador SMB para Gnome
Summary(fr): Explorateur SMB pour Gnome 
Summary(wa): Foyteuse SMB pol Gnome
Name: gnomba
Version: %{ver}
Release: %{rel}
Copyright: GPL
Group: X11/GNOME/Network
Icon: gnomba-logo.xpm
Source: http://gnomba.darkcorner.net/tars/gnomba-%{ver}.tar.bz2
URL: http://gnomba.darkcorner.net/
BuildRoot: /var/tmp/gnomba-root
Requires: samba >= 2.0.5

%description
gnomba is a GUI network browser using the smb protocol.  It allows users
to browse workgroups, machines, and shares in a "Network Neighborhood."

%description -l es
gnomba es un explorador gráfico para buscar máquinas Samba o Windows
en la red local; similar a como funciona con el susodicho.

%description -l fr
gnomba est un explorateur graphique pour trouver les machines Samba
ou Windows du réseau local. Il permets une utilisation semblable à celle
du "Voisinage réseau" de Windows.

%description -l wa
gnomba est ene foyteuse grafike po trover des éndjoles Samba ou Windows sol
rantoele locåle. Avou lî vos poloz åjheymint cweri et monter des pårteyes
d' éndjoles windows oudoben eployi leus scrireces. 

%changelog

* Tue Nov 09 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- 0.5.1

* Sun Oct 31 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- Defattr
- Enable SMP build/check
- Remove useless defines
- 0.5.0 :
	- Update .desktop location in file list

* Wed Aug 31 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- 0.4.2

* Tue Aug 05 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- 0.3

* Wed Jul 28 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- upgraded to 0.2

* Mon Jul 26 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- adapted to mandrake
- made i18n patch
- added spanish, french and walloon to *.desktop and a po/wa.po file

%prep
%setup

%build
./configure --prefix=/usr --sysconfdir=/etc
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"
     
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT

make install prefix=$RPM_BUILD_ROOT/usr sysconfdir=$RPM_BUILD_ROOT/etc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README COPYING ChangeLog
/usr/bin/gnomba
/usr/share/gnome/apps/Internet/gnomba.desktop 
/usr/share/locale/*/LC_MESSAGES/gnomba.mo
/usr/share/pixmaps/*
