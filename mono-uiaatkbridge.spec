%define oname uiaatkbridge

Name:     	mono-%{oname}
Version:	1.0
Release:	%mkrel 1
License:	MIT or X11
URL:		http://www.mono-project.com/Accessibility
Source0:	http://ftp.novell.com/pub/mono/sources/uiaatkbridge/%{oname}-%{version}.tar.bz2
BuildRequires:	mono-devel >= 2.4
BuildRequires:	mono-uia >= 1.0
BuildRequires:	atk-devel
BuildRequires:	gtk2-devel >= 2.12
BuildRequires:	glib-sharp2 >= 2.12.8
BuildRequires:	gtk-sharp2 >= 2.12.8
Requires:	libat-spi
Summary:	UIA to ATK Bridge
Group:		Development/Other
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
UiaAtkBridge is a project of the Mono Accessibility team. Its purpose
is to translate between providers implementing interfaces from Microsoft's
UI Automation (UIA) specification, and the native accessibility infrastructure
on the Linux desktop (ATK).

The bridge contains adapter Atk.Objects that wrap UIA providers.  Adapter
behavior is determined by provider ControlType and supported pattern interfaces.
The bridge implements interfaces from UIAutomationBridge which allow the UI
Automation core to send it automation events and provider information.

%prep
%setup -q -n %oname-%version

%build
%configure2_5x --disable-static
make

%install
rm -rf %buildroot
%makeinstall_std

rm -f %{buildroot}/%_libdir/uiaatkbridge/libbridge-glue.la

%clean
rm -rf %buildroot

%files
%defattr(-, root, root)
%_libdir/uiaatkbridge/UiaAtkBridge.dll*
%_prefix/lib/mono/gac/UiaAtkBridge
%_libdir/uiaatkbridge/*.so
