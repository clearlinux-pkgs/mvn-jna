#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-jna
Version  : 3.4.0
Release  : 5
URL      : https://github.com/java-native-access/jna/archive/3.4.0.tar.gz
Source0  : https://github.com/java-native-access/jna/archive/3.4.0.tar.gz
Source1  : https://repo.maven.apache.org/maven2/net/java/dev/jna/jna-platform/4.1.0/jna-platform-4.1.0.jar
Source2  : https://repo.maven.apache.org/maven2/net/java/dev/jna/jna-platform/4.1.0/jna-platform-4.1.0.pom
Source3  : https://repo.maven.apache.org/maven2/net/java/dev/jna/jna/4.1.0/jna-4.1.0-sources.jar
Source4  : https://repo1.maven.org/maven2/net/java/dev/jna/jna/3.4.0/jna-3.4.0.pom
Source5  : https://repo1.maven.org/maven2/net/java/dev/jna/jna/3.5.2/jna-3.5.2.jar
Source6  : https://repo1.maven.org/maven2/net/java/dev/jna/jna/3.5.2/jna-3.5.2.pom
Source7  : https://repo1.maven.org/maven2/net/java/dev/jna/jna/4.1.0/jna-4.1.0.jar
Source8  : https://repo1.maven.org/maven2/net/java/dev/jna/jna/4.1.0/jna-4.1.0.pom
Source9  : https://repo1.maven.org/maven2/net/java/dev/jna/platform/3.4.0/platform-3.4.0.pom
Source10  : https://repo1.maven.org/maven2/net/java/dev/jna/platform/3.5.2/platform-3.5.2.jar
Source11  : https://repo1.maven.org/maven2/net/java/dev/jna/platform/3.5.2/platform-3.5.2.pom
Source12  : https://repo1.maven.org/maven2/org/elasticsearch/jna/4.4.0-1/jna-4.4.0-1.jar
Source13  : https://repo1.maven.org/maven2/org/elasticsearch/jna/4.4.0-1/jna-4.4.0-1.pom
Summary  : Library supporting Foreign Function Interfaces
Group    : Development/Tools
License  : LGPL-2.1 MIT
Requires: mvn-jna-data = %{version}-%{release}
Requires: mvn-jna-license = %{version}-%{release}
BuildRequires : apache-ant
BuildRequires : buildreq-mvn

%description
Status
======
libffi-3.0.10 was released on XXXXXXXXXX, 2011. Check the libffi web
page for updates: <URL:http://sourceware.org/libffi/>.

%package data
Summary: data components for the mvn-jna package.
Group: Data

%description data
data components for the mvn-jna package.


%package license
Summary: license components for the mvn-jna package.
Group: Default

%description license
license components for the mvn-jna package.


%prep
%setup -q -n jna-3.4.0

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-jna
cp LICENSE %{buildroot}/usr/share/package-licenses/mvn-jna/LICENSE
cp native/libffi/LICENSE %{buildroot}/usr/share/package-licenses/mvn-jna/native_libffi_LICENSE
mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/java/dev/jna/jna-platform/4.1.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/net/java/dev/jna/jna-platform/4.1.0/jna-platform-4.1.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/java/dev/jna/jna-platform/4.1.0
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/net/java/dev/jna/jna-platform/4.1.0/jna-platform-4.1.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/java/dev/jna/jna/4.1.0
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/net/java/dev/jna/jna/4.1.0/jna-4.1.0-sources.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/java/dev/jna/jna/3.4.0
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/net/java/dev/jna/jna/3.4.0/jna-3.4.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/java/dev/jna/jna/3.5.2
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/net/java/dev/jna/jna/3.5.2/jna-3.5.2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/java/dev/jna/jna/3.5.2
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/net/java/dev/jna/jna/3.5.2/jna-3.5.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/java/dev/jna/jna/4.1.0
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/net/java/dev/jna/jna/4.1.0/jna-4.1.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/java/dev/jna/jna/4.1.0
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/net/java/dev/jna/jna/4.1.0/jna-4.1.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/java/dev/jna/platform/3.4.0
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/net/java/dev/jna/platform/3.4.0/platform-3.4.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/java/dev/jna/platform/3.5.2
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/net/java/dev/jna/platform/3.5.2/platform-3.5.2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/java/dev/jna/platform/3.5.2
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/net/java/dev/jna/platform/3.5.2/platform-3.5.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/elasticsearch/jna/4.4.0-1
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/org/elasticsearch/jna/4.4.0-1/jna-4.4.0-1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/elasticsearch/jna/4.4.0-1
cp %{SOURCE13} %{buildroot}/usr/share/java/.m2/repository/org/elasticsearch/jna/4.4.0-1/jna-4.4.0-1.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/net/java/dev/jna/jna-platform/4.1.0/jna-platform-4.1.0.jar
/usr/share/java/.m2/repository/net/java/dev/jna/jna-platform/4.1.0/jna-platform-4.1.0.pom
/usr/share/java/.m2/repository/net/java/dev/jna/jna/3.4.0/jna-3.4.0.pom
/usr/share/java/.m2/repository/net/java/dev/jna/jna/3.5.2/jna-3.5.2.jar
/usr/share/java/.m2/repository/net/java/dev/jna/jna/3.5.2/jna-3.5.2.pom
/usr/share/java/.m2/repository/net/java/dev/jna/jna/4.1.0/jna-4.1.0-sources.jar
/usr/share/java/.m2/repository/net/java/dev/jna/jna/4.1.0/jna-4.1.0.jar
/usr/share/java/.m2/repository/net/java/dev/jna/jna/4.1.0/jna-4.1.0.pom
/usr/share/java/.m2/repository/net/java/dev/jna/platform/3.4.0/platform-3.4.0.pom
/usr/share/java/.m2/repository/net/java/dev/jna/platform/3.5.2/platform-3.5.2.jar
/usr/share/java/.m2/repository/net/java/dev/jna/platform/3.5.2/platform-3.5.2.pom
/usr/share/java/.m2/repository/org/elasticsearch/jna/4.4.0-1/jna-4.4.0-1.jar
/usr/share/java/.m2/repository/org/elasticsearch/jna/4.4.0-1/jna-4.4.0-1.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-jna/LICENSE
/usr/share/package-licenses/mvn-jna/native_libffi_LICENSE
