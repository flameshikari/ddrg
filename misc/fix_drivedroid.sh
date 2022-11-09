#!/data/data/com.termux/files/usr/bin/sh

if [ "$(whoami)" != "root" ]
  then echo "run as root"
  exit
else
  setprop sys.usb.config cdrom
  setprop sys.usb.configfs 1
  rm /config/usb_gadget/g1/configs/b.1/f* &> /dev/null
  mkdir -p /config/usb_gadget/g1/functions/mass_storage.0/lun.0/ \
           /config/usb_gadget/g1/configs/b.1/strings/0x409
  getprop sys.usb.config > /config/usb_gadget/g1/configs/b.1/strings/0x409/configuration
  touch /config/usb_gadget/g1/functions/mass_storage.0/lun.0/file
  echo $1 > /config/usb_gadget/g1/functions/mass_storage.0/lun.0/file
  ln -s /config/usb_gadget/g1/functions/mass_storage.0 /config/usb_gadget/g1/configs/b.1/f99
  getprop sys.usb.controller > /config/usb_gadget/g1/UDC
  setprop sys.usb.state cdrom
fi
