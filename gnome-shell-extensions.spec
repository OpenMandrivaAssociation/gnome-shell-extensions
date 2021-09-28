%define url_ver %(echo %{version} | cut -d "." -f -2)

Summary:	Modify and extend GNOME Shell functionality and behavior
Name:		gnome-shell-extensions
Version:	41.0
Release:	1
Group:		Graphical desktop/GNOME
License:	GPLv2+
Url:		http://live.gnome.org/GnomeShell/Extensions
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-shell-extensions/%{url_ver}/%{name}-%{version}.tar.xz
BuildArch:	noarch

BuildRequires:	gnome-common
BuildRequires:	intltool
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnome-desktop-3.0)
BuildRequires:	pkgconfig(libgtop-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	gnome-shell
BuildRequires:	meson
BuildRequires:	sassc

Requires:	gnome-shell
Requires:	gnome-session

Recommends:	%{name}-apps-menu
Recommends:	%{name}-auto-move-windows
Recommends:	%{name}-drive-menu
Recommends:	%{name}-gajim
Recommends:	%{name}-launch-new-instance
Recommends:	%{name}-native-window-placement
Recommends:	%{name}-places-menu
Recommends:	%{name}-systemMonitor
Recommends:	%{name}-user-theme
Recommends:	%{name}-windowsNavigator
Recommends:	%{name}-workspace-indicator

Obsoletes:      gnome-shell-extensions-alternate-tab
Obsoletes:      %{name}-horizontal-workspaces

%description
GNOME Shell Extensions is a collection of extensions providing additional
and optional functionality to GNOME Shell.

Enabled extensions:

  * alternate-tab
  * apps-menu
  * auto-move-windows
  * drive-menu
  * launch-new-instance
  * native-window-placement
  * places-menu
  * screenshot-window-sizer
  * systemMonitor
  * user-theme
  * window-list
  * overrides
  * windowsNavigator
  * workspace-indicator

%package common
Summary:	Files common to GNOME Shell Extensions
Group:		Graphical desktop/GNOME
Requires:	gnome-shell >= 3.6.0

%description common
GNOME Shell Extensions is a collection of extensions providing additional
and optional functionality to GNOME Shell. Common files and directories
needed by extensions are provided here.

%package -n gnome-classic-session
Summary:        GNOME "classic" mode session
Group:          Graphical desktop/GNOME
Requires:       %{name}-apps-menu = %{version}-%{release}
Requires:       %{name}-launch-new-instance = %{version}-%{release}
Requires:       %{name}-places-menu = %{version}-%{release}
Requires:       %{name}-window-list = %{version}-%{release}
Requires:       %{name}-overrides = %{version}-%{release}
# Obsolete fallback mode components
Obsoletes:      gnome-applets < 1:3.5.92-5
%global gnome_applet_sensors_obsolete_ver 3.0.0-6
Obsoletes:      gnome-applet-sensors < %{gnome_applet_sensors_obsolete_ver}
Obsoletes:      gnome-applet-sensors-devel < %{gnome_applet_sensors_obsolete_ver}
Obsoletes:      gnome-panel < 3.8

%description -n gnome-classic-session
This package contains the required components for the GNOME Shell "classic"
mode, which aims to provide a GNOME 2-like user interface.

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

%package window-list
Summary:        Display a window list at the bottom of the screen in GNOME Shell
Group:          Graphical desktop/GNOME
Requires:       %{name}-common = %{version}-%{release}

%description window-list
This GNOME Shell extension displays a window list at the bottom of the screen.

%package overrides
Summary:        Classic-mode schema overides in GNOME Shell
Group:          Graphical desktop/GNOME
Requires:       %{name}-common = %{version}-%{release}
Obsoletes:	%{name}-static-workspaces
Obsoletes:	%{name}-default-min-max

%description overrides
This GNOME Shell extension disables overrides workspace management.


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

%package launch-new-instance
Summary:        Always launch a new application instance for GNOME Shell
Group:          Graphical desktop/GNOME
Requires:       %{name}-common = %{version}-%{release}

%description  launch-new-instance
This GNOME Shell extension modifies the behavior of clicking
the dash and app-launcher to always launch a new application instance.

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

%package screenshot-window-sizer
Summary: Screenshot window sizer for GNOME Shell
Group: Graphical desktop/GNOME
License: GPLv2+
Requires: %{name}-common = %{version}-%{release}

%description screenshot-window-sizer
This GNOME Shell extension allows to easily resize windows for GNOME Software
screenshots.

%package apps-menu
Summary:	Gnome 2.x style menu on the panel
Group:		Graphical desktop/GNOME
Requires:	%{name}-common = %{version}-%{release}

%description apps-menu
Lets you reach an application using gnome 2.x style menu on the panel.

%package workspace-indicator
Summary:	A menu for changing workspace
Group:		Graphical desktop/GNOME
Requires:	%{name}-common = %{version}-%{release}

%description workspace-indicator
A menu for changing workspace.

%prep
%setup -q

%build
%meson -Dextension_set="all" -Dclassic_mode=true
%meson_build

%install
%meson_install


# helper script
mkdir -p %buildroot%{_bindir}
cat << EOF >%{buildroot}%{_bindir}/startgnome_classic
#!/bin/sh
GNOME_SHELL_SESSION_MODE=classic
export GNOME_SHELL_SESSION_MODE
exec gnome-session --session gnome-classic
EOF
chmod 755 %{buildroot}%{_bindir}/startgnome_classic

# kill upstream xsession file.
# If we leave this it overrides our one, preventing the run of /etc/X11/Xsession
# and thus the processing of /etc/X11/xinit.d/ files.
# See: https://bugs.mageia.org/show_bug.cgi?id=11582
rm -rf %{buildroot}%{_datadir}/xsessions

# wmsession session file
mkdir -p %{buildroot}%{_sysconfdir}/X11/wmsession.d
cat << EOF > %{buildroot}%{_sysconfdir}/X11/wmsession.d/03GNOME_CLASSIC
NAME=GNOME Classic
ICON=gnome-logo-icon-transparent.png
DESC=GNOME 3 Classic Mode
EXEC=%{_bindir}/startgnome_classic
SCRIPT:
exec %{_bindir}/startgnome_classic
EOF

%find_lang %{name}

%files

%files common -f %{name}.lang
#doc README
%dir %{_datadir}/gnome-shell/extensions/
%dir %{_datadir}/glib-2.0/schemas
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.apps-menu.gschema.xml

%files -n gnome-classic-session
%config(noreplace) %{_sysconfdir}/X11/wmsession.d/*
%{_bindir}/startgnome_classic
#{_datadir}/gnome-session/sessions/gnome-classic.session
%{_datadir}/gnome-shell/modes/classic.json
%{_datadir}/gnome-shell/theme/*.svg
%{_datadir}/gnome-shell/theme/gnome-classic.css
%{_datadir}/gnome-shell/theme/gnome-classic-high-contrast.css

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

%files launch-new-instance
%{_datadir}/gnome-shell/extensions/launch-new-instance*

%files places-menu
%{_datadir}/gnome-shell/extensions/places-menu*

%files screenshot-window-sizer
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.screenshot-window-sizer.gschema.xml
%{_datadir}/gnome-shell/extensions/screenshot-window-sizer*/

%files native-window-placement
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.native-window-placement.gschema.xml
%{_datadir}/gnome-shell/extensions/native-window-placement*

%files apps-menu
%{_datadir}/gnome-shell/extensions/apps-menu*

%files workspace-indicator
%{_datadir}/gnome-shell/extensions/workspace-indicator*

%files window-list
%{_datadir}/gnome-shell/extensions/window-list*
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.window-list.gschema.xml

%files overrides
#{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.classic-overrides.gschema.xml
%{_datadir}/glib-2.0/schemas/00_org.gnome.shell.extensions.classic.gschema.override
