# nobara-update-before-shutdown
A little helper that updates the system before shutdown/reboot/halt.

Still WIP

# Installation
```bash
sudo cp src/bin/nobara-automatic-update.sh /usr/local/bin/nobara-automatic-update.sh
sudo chmod +x /usr/local/bin/nobara-automatic-update.sh
sudo cp src/systemd/update-before-shutdown.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable update-before-shutdown.service
```

# Roadmap
* ~~Does the script needs to be +x?~~ Yes.
* Implement https://copr.fedorainfracloud.org/ - more information is here: https://github.com/Nobara-Project/rpm-sources
* Add manual flatpack update
* Add a message to the shutdown screen if updates are getting processed
* Validate if all 3 targets are needed in the systemd file