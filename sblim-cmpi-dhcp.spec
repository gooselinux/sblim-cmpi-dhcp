
%define provider_dir %{_libdir}/cmpi
%define tog_pegasus_version 2:2.6.1-1

Name:           sblim-cmpi-dhcp
Version:        1.0
Release:        1%{?dist}
Summary:        SBLIM WBEM-SMT DHCP

Group:          Applications/System
License:        EPL
URL:            http://sblim.wiki.sourceforge.net/
Source0:        http://downloads.sourceforge.net/sblim/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  tog-pegasus-devel >= %{tog_pegasus_version}
BuildRequires:  sblim-tools-libra-devel
BuildRequires:  sblim-cmpi-base-devel
BuildRequires:  bison
BuildRequires:  flex
Requires:       sblim-tools-libra
Requires:       dhcp
Provides:       cmpi-dhcp = %{version}-%{release}

%description
The cmpi-dhcp package provides access to the DHCP configuration data
via CIMOM technology/infrastructure.
It contains the DHCP CIM Model, CMPI Provider with the DHCP task specific
Resource Access.

%package        devel
Summary:        SBLIM WBEM-SMT DHCP - Header Development Files
Group:          Development/Libraries
Requires:       sblim-cmpi-dhcp = %{version}-%{release}

%description devel
SBLIM WBEM-SMT DHCP Development Package contains header files and
link libraries for dependent provider packages

%package        test
Summary:        SBLIM WBEM-SMT DHCP - Testcase Files
Group:          Applications/System
Requires:       sblim-cmpi-dhcp = %{version}-%{release}
Requires:       sblim-testsuite

%description test
SBLIM WBEM-SMT DHCP Provider Testcase Files for the SBLIM Testsuite

%prep
%setup -q


%build
%ifarch s390 s390x ppc ppc64
export CFLAGS="$RPM_OPT_FLAGS -fsigned-char"
%else
export CFLAGS="$RPM_OPT_FLAGS"
%endif
%configure \
        TESTSUITEDIR=%{_datadir}/sblim-testsuite \
        CIMSERVER=pegasus \
        PROVIDERDIR=%{_libdir}/cmpi/
make


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
# remove unused libtool files
rm -f $RPM_BUILD_ROOT/%{_libdir}/*a
rm -f $RPM_BUILD_ROOT/%{_libdir}/cmpi/*a
mv $RPM_BUILD_ROOT/%{_libdir}/libuniquekey.so $RPM_BUILD_ROOT/%{provider_dir}
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc %{_datadir}/doc/sblim-cmpi-dhcp-%{version}
%exclude %{_datadir}/doc/sblim-cmpi-dhcp-%{version}/*.test
%doc %{_mandir}/man5/smt_dhcp_ra_support.conf.5.gz
%config(noreplace) %{_sysconfdir}/smt_dhcp*.conf
%{_datadir}/sblim-cmpi-dhcp
%{_libdir}/cmpi/libuniquekey.so
%{_libdir}/libRaToolsDhcp.so.*
%{_libdir}/cmpi/libcmpiLinux_DHCP*.so

%files devel
%defattr(-,root,root,-)
%{_libdir}/libRaToolsDhcp.so

%files test
%defattr(-,root,root,-)
%{_datadir}/sblim-testsuite/test-cmpi-dhcp.sh
%doc %{_datadir}/doc/sblim-cmpi-dhcp-%{version}/*.test
%{_datadir}/sblim-testsuite/dhcpd.conf
%{_datadir}/sblim-testsuite/cim/Linux_DHCP*
%{_datadir}/sblim-testsuite/system/linux/Linux_DHCP*


# Conditional definition of schema and registration files
%define DHCP_SCHEMA %{_datadir}/sblim-cmpi-dhcp/Linux_DHCPEntity.mof %{_datadir}/sblim-cmpi-dhcp/Linux_DHCPService.mof %{_datadir}/sblim-cmpi-dhcp/Linux_DHCPGlobal.mof %{_datadir}/sblim-cmpi-dhcp/Linux_DHCPGlobalForService.mof %{_datadir}/sblim-cmpi-dhcp/Linux_DHCPGroup.mof %{_datadir}/sblim-cmpi-dhcp/Linux_DHCPGroupsForEntity.mof %{_datadir}/sblim-cmpi-dhcp/Linux_DHCPHost.mof %{_datadir}/sblim-cmpi-dhcp/Linux_DHCPHostsForEntity.mof %{_datadir}/sblim-cmpi-dhcp/Linux_DHCPOptions.mof %{_datadir}/sblim-cmpi-dhcp/Linux_DHCPOptionsForEntity.mof %{_datadir}/sblim-cmpi-dhcp/Linux_DHCPParams.mof %{_datadir}/sblim-cmpi-dhcp/Linux_DHCPParamsForEntity.mof %{_datadir}/sblim-cmpi-dhcp/Linux_DHCPPool.mof %{_datadir}/sblim-cmpi-dhcp/Linux_DHCPPoolsForEntity.mof %{_datadir}/sblim-cmpi-dhcp/Linux_DHCPRegisteredProfile.mof %{_datadir}/sblim-cmpi-dhcp/Linux_DHCPServiceConfiguration.mof %{_datadir}/sblim-cmpi-dhcp/Linux_DHCPServiceConfigurationForService.mof %{_datadir}/sblim-cmpi-dhcp/Linux_DHCPSharednet.mof %{_datadir}/sblim-cmpi-dhcp/Linux_DHCPSharednetsForEntity.mof %{_datadir}/sblim-cmpi-dhcp/Linux_DHCPSubnet.mof %{_datadir}/sblim-cmpi-dhcp/Linux_DHCPSubnetsForEntity.mof %{_datadir}/sblim-cmpi-dhcp/Linux_DHCPElementConformsToProfile.mof
%define DHCP_REGISTRATION %{_datadir}/sblim-cmpi-dhcp/Linux_DHCPGlobal.registration %{_datadir}/sblim-cmpi-dhcp/Linux_DHCPGlobalForService.registration %{_datadir}/sblim-cmpi-dhcp/Linux_DHCPGroup.registration %{_datadir}/sblim-cmpi-dhcp/Linux_DHCPGroupsForEntity.registration %{_datadir}/sblim-cmpi-dhcp/Linux_DHCPHost.registration %{_datadir}/sblim-cmpi-dhcp/Linux_DHCPHostsForEntity.registration %{_datadir}/sblim-cmpi-dhcp/Linux_DHCPOptions.registration %{_datadir}/sblim-cmpi-dhcp/Linux_DHCPOptionsForEntity.registration %{_datadir}/sblim-cmpi-dhcp/Linux_DHCPParams.registration %{_datadir}/sblim-cmpi-dhcp/Linux_DHCPParamsForEntity.registration %{_datadir}/sblim-cmpi-dhcp/Linux_DHCPPool.registration %{_datadir}/sblim-cmpi-dhcp/Linux_DHCPPoolsForEntity.registration %{_datadir}/sblim-cmpi-dhcp/Linux_DHCPRegisteredProfile.registration %{_datadir}/sblim-cmpi-dhcp/Linux_DHCPService.registration %{_datadir}/sblim-cmpi-dhcp/Linux_DHCPServiceConfiguration.registration %{_datadir}/sblim-cmpi-dhcp/Linux_DHCPServiceConfigurationForService.registration %{_datadir}/sblim-cmpi-dhcp/Linux_DHCPSharednet.registration %{_datadir}/sblim-cmpi-dhcp/Linux_DHCPSharednetsForEntity.registration %{_datadir}/sblim-cmpi-dhcp/Linux_DHCPSubnet.registration %{_datadir}/sblim-cmpi-dhcp/Linux_DHCPSubnetsForEntity.registration

%define DHCP_INTEROP_SCHEMAS %{_datadir}/sblim-cmpi-dhcp/Linux_DHCPService.mof %{_datadir}/sblim-cmpi-dhcp/Linux_DHCPRegisteredProfile.mof %{_datadir}/sblim-cmpi-dhcp/Linux_DHCPElementConformsToProfile.mof
%define DHCP_INTEROP_REGISTRATIONS %{_datadir}/sblim-cmpi-dhcp/Linux_DHCPRegisteredProfile.registration %{_datadir}/sblim-cmpi-dhcp/Linux_DHCPElementConformsToProfile.registration

%pre
# If upgrading, deregister old version
if [ $1 -gt 1 ]
then
  %{_datadir}/sblim-cmpi-dhcp/provider-register.sh -d -t pegasus \
        -r %{DHCP_REGISTRATION} -m %{DHCP_SCHEMA} > /dev/null 2>&1 || :;

  %{_datadir}/sblim-cmpi-dhcp/provider-register.sh -d -t pegasus \
        -n "root/PG_InterOp" -r %{DHCP_INTEROP_REGISTRATIONS} -m %{DHCP_INTEROP_SCHEMAS} > /dev/null 2>&1 || :;

fi

%post
# Register Schema and Provider - this is highly provider specific
%{_datadir}/sblim-cmpi-dhcp/provider-register.sh -t pegasus \
        -v -r %{DHCP_REGISTRATION} -m %{DHCP_SCHEMA} > /dev/null 2>&1 || :;

%{_datadir}/sblim-cmpi-dhcp/provider-register.sh -t pegasus \
         -v -n "root/PG_InterOp" -r %{DHCP_INTEROP_REGISTRATIONS} -m %{DHCP_INTEROP_SCHEMAS} > /dev/null 2>&1 || :;
/sbin/ldconfig

%preun
# Deregister only if not upgrading 
if [ $1 -eq 0 ]
then
  %{_datadir}/sblim-cmpi-dhcp/provider-register.sh -d \
        -t pegasus -r %{DHCP_REGISTRATION} -m %{DHCP_SCHEMA} > /dev/null 2>&1 || :;

  %{_datadir}/sblim-cmpi-dhcp/provider-register.sh -d -t pegasus \
        -n "root/PG_InterOp" -r %{DHCP_INTEROP_REGISTRATIONS} -m %{DHCP_INTEROP_SCHEMAS} > /dev/null 2>&1 || :;
fi

%postun
# Run ldconfig only if not upgrading
if [ $1 -eq 0 ]
then
  /sbin/ldconfig
fi


%changelog
* Wed Jun 30 2010 Vitezslav Crhonek <vcrhonek@redhat.com> - 1.0-1
- Update to sblim-cmpi-dhcp-1.0

* Tue Oct  6 2009 Vitezslav Crhonek <vcrhonek@redhat.com> - 0.5.5-1
- Initial support
