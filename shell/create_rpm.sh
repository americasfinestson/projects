#!/bin/bash

# This script creates an RPM out of the contents of the directory it is executed from, as well as all sub directories.

# Read user input
while getopts n: flag
do
  case "${flag}" in
    n) rpmname=${OPTARG}
  esac
done

# Create RPM build directories
rpm_build_dirs=("./BUILD" "./BUILDROOT" "./RPMS" "./SOURCES" "./SPECS" "./SRPMS")
for d in ${rpm_build_dirs[@]}
do
  if [ ! -d ${d} ] > /dev/null 2>&1;
  then
    mkdir -pm 0700 ${d}
  fi
done

# Create rpmbuild directory in user's home directory
if [ -n "$(ls -la ~ | grep rpmbuild | grep -e ^l -e ^- )" ]
then
  rm -f ~/rpmbuild
elif [ -n "$(ls -la ~ | grep rpmbuild | grep ^d)" ]
then
  rm -rf ~/rpmbuild
fi

# Symlink current working directory to ~/rpmbuild
ln -s $(pwd) ~/rpmbuild

# rsync everything into RPM build directory
rsync -avh --progress --exclude '.git' ./* ./BUILD/

# Create RPM spec file
cat > ./SPECS/specfile.spec <<'EOF'
Name:
Version:
Release:
Summary: Awesome RPM created from americasfinestson/create_rpm!
License: N/A
Requires:


%description
Incredibly awesome RPM created from Josh's public Github


%prep


%build


%install
mkdir -p %{buildroot}/scripts
rsync -ap * %{buildroot}/scripts
exit 0


%post
echo "What an awesome RPM installation!"

%files


EOF

# Create variables for dates
current_date=$(date --rfc-3339=seconds | tr -d -)
current_date_YYYY=$(date --rfc-3339=seconds | cut -d" " -f1 | cut -d"-" -f1)
current_date_MMMM=$(date --rfc-3339=seconds | cut -d" " -f1 | cut -d"-" -f2,3 | tr -d "-")

# Update Version and Release 
sed -i "s/\(Version:\)/\1${current_date_YYYY/g" ./SPECS/specfile.spec
sed -i "s/\(Release:\)/\1${current_date_MMMM/g" ./SPECS/specfile.spec

# Add files to file list
for f in "$(find ./BUILD/ | sed 's/\(\.\/BUILD\/\)\(\)/\/root\/scripts\/\2/g')";
do
  echo "${f}" >> ./SPECS/specfile.spec
done

# Build RPM
rpmbuild -ba ./SPECS/specfile.spec

# Move RPM to current working directory
rsync -avp ./RPMS/x86_64/*.rpm *

# Clean up
for d in ${rpm_build_dirs[@]}
do
  rm -rf ${d}
done

