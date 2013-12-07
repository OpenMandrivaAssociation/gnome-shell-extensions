%define url_ver %(echo %{version} | cut -d "." -f -2)

Summary:	Modify and extend GNOME Shell functionality and behavior
Name:		gnome-shell-extensions
Version:	3.6.1
Release:	5
Group:		Graphical desktop/GNOME 
License:	GPLv2+ 
Url:		http://live.gnome.org/GnomeShell/Extensions
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gnome-shell-extensions/%{url_ver}/%{name}-%{version}.tar.xz
BuildArch:	noarch

BuildRequires:	gnome-common
BuildRequires:	intltool
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnome-desktop-3.0)
BuildRequires:	pkgconfig(libgtop-2.0)

Suggests:	%{name}-alternate-tab
Suggests:	%{name}-alternative-status-menu
Suggests:	%{name}-dock 
Suggests:	%{name}-windowsnavigator 
Suggests:	%{name}-user-theme 
Suggests:	%{name}-auto-move-windows 
Suggests:	%{name}-drive-menu  
Suggests:	%{name}-places-menu 
Suggests:	%{name}-native-window-placement
Suggests:	%{name}-xrandr-indicator
Suggests:	%{name}-systemmonitor
Suggests:	%{name}-gajim
Suggests:	%{name}-apps-menu
Suggests:	%{name}-workspace-indicator

%description
GNOME Shell Extensions is a collection of extensions providing additional 
and optional functionality to GNOME Shell.

Enabled extensions:

* alternate-tab
* alternative-status-menu
* dock
* windowsNavigator
* user-theme
* auto-move-windows
* drive-menu
* places-menu
* native-window-placement
* xrandr-indicator
* systemMonitor
* apps-menu
* gajim
* workspace-indicator
* example (simple example for writing extensions)

%package common
Summary:	Files common to GNOME Shell Extensions
Group:		Graphical desktop/GNOME 
Requires:	gnome-shell >= 3.6.0

%description common
GNOME Shell Extensions is a collection of extensions providing additional 
and optional functionality to GNOME Shell. Common files and directories 
needed by extensions are provided here.

%package alternate-tab
Summary:	Classic Alt+Tab behavior. Window based instead of app based
Group:		Graphical desktop/GNOME 
Requires:	%{name}-common = %{version}-%{release}

%description alternate-tab
Lets you use classic Alt+Tab (window-based instead of app-based) in
GNOME Shell.

GNOME Shell groups multiple instances of the same application together.
This extension disables grouping.  

%package alternative-status-menu
Summary:	For those who want a power off item visible at all the time
Group:		Graphical desktop/GNOME 
Requires:	%{name}-common = %{version}-%{release}

%description alternative-status-menu
For those who want a power off item visible at all the time, replaces 
GNOME Shell status menu with one featuring separate Suspend and Power Off. 
Adds the ability to hibernate as well.

%package dock
Summary:	Shows a dock-style task switcher permanently
Group:		Graphical desktop/GNOME 
Requires:	%{name}-common = %{version}-%{release}

%description dock
Shows a dock-style task switcher on the right side of the screen permanently.

%package windowsnavigator
Summary:	Keyboard selection of windows and work-spaces in overlay mode
Group:		Graphical desktop/GNOME 
Requires:	%{name}-common = %{version}-%{release}

%description windowsnavigator
Allow keyboard selection of windows and work-spaces in overlay mode in 
GNOME Shell.

Switch to overview mode (press the windows or alt+f1 key) and 
press the alt key to show numbers over windows.  Press any number to switch
to the corresponding window.

%package user-theme
Summary:	Lets the user select a custom theme for the shell
Group:		Graphical desktop/GNOME 
Requires:	%{name}-common = %{version}-%{release}

%description user-theme
Lets the user select a custom theme for the Gnome shell. It will allow you to 
apply a style from /.themes/[themeName]/gnome-shell/gnome-shell.css

%package auto-move-windows
Summary:	Assign specific workspaces to applications
Group:		Graphical desktop/GNOME 
Requires:	%{name}-common = %{version}-%{release}

%description auto-move-windows
Lets you manage your workspaces more easily, assigning a specific workspace
to each application as soon as it creates a window, in a manner configurable
with a GSettings key.

%package drive-menu
Summary:	Disk device manager in the system status area
Group:		Graphical desktop/GNOME 
Requires:	%{name}-common = %{version}-%{release}

%description drive-menu
Adds a menu in the system status area that tracks removable disk devices
attached and offers to browse them and eject/unmount them.

%package places-menu
Summary:	Places menu indicator in the system status area
Group:		Graphical desktop/GNOME 
Requires:	%{name}-common = %{version}-%{release}

%description places-menu
Adds a menu in the system status area that resembles the Places menu from
GNOME 2.x

%package native-window-placement
Summary:	Arrange windows in overview in a more native way
Group:		Graphical desktop/GNOME 
Requires:	%{name}-common = %{version}-%{release}

%description native-window-placement
This extension employs an algorithm (taken from KDE) for layouting the
thumbnails in the overview that more closely reflects the positions and 
relative sizes of the actual windows, instead of using a fixed grid.

%package systemmonitor
Summary:	Monitor your system status
Group:		Graphical desktop/GNOME 
Requires:	%{name}-common = %{version}-%{release}

%description systemmonitor
Monitor your system status.

%package xrandr-indicator
Summary:	Replace the GTK+ based indicator
Group:		Graphical desktop/GNOME
Requires:	%{name}-common = %{version}-%{release}

%description xrandr-indicator
Replace the GTK+ based indicator from gnome-settings-daemon with
a native one. Lets the user rotate the laptop monitor and open
display preferences quickly.

%package apps-menu
Summary:	Gnome 2.x style menu on the panel
Group:		Graphical desktop/GNOME
Requires:	%{name}-common = %{version}-%{release}

%description apps-menu
Lets you reach an application using gnome 2.x style menu on the panel.

%package gajim
Summary:	Integration with Gajim, a Jabber/XMPP instant messaging client
Group:		Graphical desktop/GNOME
Requires:	%{name}-common = %{version}-%{release}

%description gajim
Integration with Gajim, a Jabber/XMPP instant messaging client..

%package example
Summary:	A minimal example illustrating how to write extensions
Group:		Graphical desktop/GNOME
Requires:	%{name}-common = %{version}-%{release}

%description example
A minimal example illustrating how to write extensions.

%package workspace-indicator
Summary:	A menu for changing workspace
Group:		Graphical desktop/GNOME
Requires:	%{name}-common = %{version}-%{release}

%description workspace-indicator
A menu for changing workspace.

%prep
%setup -q

# Main.panel._userMenu renamed to Main.panel._statusmenu in GS 3.0.1; fix sent
# to the alternative-status-menu extension author
sed -i "s|Main\.panel\._userMenu|Main.panel._statusmenu|g" extensions/alternative-status-menu/extension.js

%build
NOCONFIGURE=1 gnome-autogen.sh
%configure2_5x  \
	--disable-schemas-compile \
	--enable-extensions="all"

%make

%install
%makeinstall_std

%find_lang %{name}

%files

%files common -f %{name}.lang
%doc README
%dir %{_datadir}/gnome-shell/extensions/
%dir %{_datadir}/glib-2.0/schemas

%files alternate-tab
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.alternate-tab.gschema.xml
%{_datadir}/gnome-shell/extensions/alternate-tab*

%files alternative-status-menu
%{_datadir}/gnome-shell/extensions/alternative-status-menu*
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.alternative-status-menu.gschema.xml

%files dock
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.dock.gschema.xml
%{_datadir}/gnome-shell/extensions/dock*

%files windowsnavigator
%{_datadir}/gnome-shell/extensions/windowsNavigator*

%files user-theme
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.user-theme.gschema.xml
%{_datadir}/gnome-shell/extensions/user-theme*

%files auto-move-windows
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.auto-move-windows.gschema.xml
%{_datadir}/gnome-shell/extensions/auto-move-windows*

%files drive-menu
%{_datadir}/gnome-shell/extensions/drive-menu*

%files places-menu
%{_datadir}/gnome-shell/extensions/places-menu*

%files native-window-placement
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.native-window-placement.gschema.xml
%{_datadir}/gnome-shell/extensions/native-window-placement*

%files systemmonitor
%{_datadir}/gnome-shell/extensions/systemMonitor*

%files xrandr-indicator
%{_datadir}/gnome-shell/extensions/xrandr-indicator*

%files apps-menu
%{_datadir}/gnome-shell/extensions/apps-menu*

%files gajim
%{_datadir}/gnome-shell/extensions/gajim*

%files workspace-indicator
%{_datadir}/gnome-shell/extensions/workspace-indicator*

%files example
%{_datadir}/gnome-shell/extensions/example*
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.example.gschema.xml

