# nobara-update-before-shutdown
A little helper that updates the system before shutdown/reboot/halt.

Still WIP

# Installation
```bash
sudo cp src/bin/nobara-automatic-update.sh /usr/local/bin/nobara-automatic-update.sh
sudo cp src/systemd/update-before-shutdown.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable update-before-shutdown.service
```