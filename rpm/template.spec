Name:           ros-indigo-cob-gazebo-worlds
Version:        0.6.0
Release:        0%{?dist}
Summary:        ROS cob_gazebo_worlds package

Group:          Development/Libraries
License:        LGPL
URL:            http://ros.org/wiki/cob_gazebo_worlds
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-gazebo-msgs
Requires:       ros-indigo-gazebo-ros
Requires:       ros-indigo-joint-state-publisher
Requires:       ros-indigo-kdl-parser
Requires:       ros-indigo-robot-state-publisher
Requires:       ros-indigo-rospy
Requires:       ros-indigo-tf
Requires:       ros-indigo-xacro
BuildRequires:  ros-indigo-catkin

%description
This package provides some worlds for gazebo simulation.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu Sep 18 2014 Nadia Hammoudeh Garcia <nhg@ipa.fhg.de> - 0.6.0-0
- Autogenerated by Bloom

* Thu Aug 28 2014 Nadia Hammoudeh Garcia <nhg@ipa.fhg.de> - 0.5.3-0
- Autogenerated by Bloom

