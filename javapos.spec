
# build loop, jcl depends on javapos and javapos depends on jcl...
%define jcl_ver 2.0.1

Summary:	Java POS
Summary(pl):	Java POS
Name:		javapos
Version:	1.6
Release:	1
Group:		Development/Languages/Java
Group(de):	Entwicklung/Sprachen/Java
Group(pl):	Programowanie/Jêzyki/Java
License:	distributable
Url:		http://www.javapos.com
Source0:	http://www.javapos.com/downloads/JavaPOS-%{version}-Source-20010529.zip
Source1:	ftp://www-126.ibm.com/pub/jposloader/jcl%{jcl_ver}.zip
Source2:	http://www.javapos.com/downloads/JPOS_Version_1_6.pdf
BuildRequires:	jdk
BuildRequires:	xerces-j
Requires:	jre
Requires:	xerces-j
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javaclassdir	%{_libdir}/java

%description
JavaPOS.

%description -l pl
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
gzip -9nf jcl/readme.html jcl/changes.txt
rm jcl/README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.pdf jcl
%{_javaclassdir}/javapos.jar
