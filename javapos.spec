
# build loop, jcl depends on javapos and javapos depends on jcl...
%define jcl_ver 2.0.1

Summary:	Java POS
Summary(pl.UTF-8):	Java POS
Name:		javapos
Version:	1.6
Release:	1
Group:		Development/Languages/Java
License:	distributable
Source0:	http://www.javapos.com/downloads/JavaPOS-%{version}-Source-20010529.zip
# Source0-md5:	9015b7558013bc8bcb81cfc528d821aa
Source1:	ftp://www-126.ibm.com/pub/jposloader/jcl%{jcl_ver}.zip
# Source1-md5:	9e5065b8a80895dbc0702080af702d84
Source2:	http://www.javapos.com/downloads/JPOS_Version_1_6.pdf
# Source2-md5:	c967008bfb0428478cf925b01f7abec0
URL:		http://www.javapos.com/
BuildRequires:	jdk
BuildRequires:	unzip
BuildRequires:	xerces-j
Requires:	jre
Requires:	xerces-j
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javaclassdir	%{_libdir}/java

%description
JavaPOS.

%description -l pl.UTF-8
JavaPOS.

%prep
%setup -q -c JavaPOS-%{version}-Source-20010529.zip
unzip %{SOURCE1}
unzip jcl%{jcl_ver}/src/jcl_src.jar

%build
install -d dist
find jpos -name \*.java | xargs javac -O -d dist -classpath .:%{_javaclassdir}/xerces.jar

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_javaclassdir}

( cd dist
  jar cf ../javapos.jar jpos
)
install javapos.jar $RPM_BUILD_ROOT%{_javaclassdir}

# install docs
# javapos
install %{SOURCE2} .
# jcl
mv jcl%{jcl_ver}/docs jcl
mv jcl%{jcl_ver}/readme.html jcl
mv jcl%{jcl_ver}/changes.txt jcl
rm jcl/README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.pdf jcl
%{_javaclassdir}/javapos.jar
