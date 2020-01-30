SCHTASKS /delete /TN kioskreboot /f
SCHTASKS /create /TN kioskreboot /TR "curl https://v2.washwapos.com/reboot" /ST 04:00 /SC DAILY
