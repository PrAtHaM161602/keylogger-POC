# keylogger-POC



---

## Remote Keylogger in Python

This is a POC for a remote keylogger written in python. It demonstrates how easy it is to gain access to a computer and steel credntials, as a reuslt we shouls not trust softwares/programs from malicious sources.
Note: This is for educational purposes only. Test with permission.

### **Important Disclaimer**

**This code is strictly for educational purposes.** Do not use this code for illegal activities. Unauthorized use of a keylogger is illegal and unethical. Always ensure that you have explicit consent and are acting within the boundaries of the law.

---

## Table of Contents

1. [Overview](#overview)
2. [How it Works](#how-it-works)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Proof of Concept (POC)](#proof-of-concept-poc)
7. [Ethical Use](#ethical-use)
8. [License](#license)

---

## Overview

This keylogger script can record keystrokes on a target machine and send them to a remote server for monitoring. The script works by using the `pynput` library to capture all the keystrokes typed on the machine. It then forwards the captured data to a server in real-time.

### **WARNING**: Only use this script in a controlled environment where you have full authorization (e.g., penetration testing or personal security research).

---

## How it Works

1. **Keylogging**: The script uses the `pynput` library to listen to all keypress events on the system.
2. **Data Sending**: The logged keystrokes are sent to a remote server using the `requests` library via HTTP.
3. **Persistence**: The script can be set to run as a background service (daemon) to ensure it captures keypresses even if the user closes the program window.
4. **Monitoring**: The keylogger sends data to the remote server, where it can be stored and analyzed.

---

## Requirements

* Python 3.x
* `pynput` library (for keylogging)
* `requests` library (for sending captured data to a remote server)

Install the required libraries using pip:

```bash
pip install pynput
```

---

## Installation
## Proof of Concept (POC)


1. The script listens for all key presses using the `pynput` library.
2. Every keystroke is logged into a remote server
3. This demonstrates the vulnerability of not properly securing sensitive data on a system.


The captured data is also sent to a remote server.



## Ethical Use

Always follow ethical guidelines when testing software like this:

* **Penetration Testing**: Only use keyloggers with explicit consent from the system owner.
* **Education**: Use this code in a controlled, educational environment.
* **Security Research**: If you’re researching security vulnerabilities, ensure that you’re working in a lab environment where no personal or sensitive data is compromised.






### **Conclusion**

This script demonstrates the dangers of keyloggers and highlights how they can easily steal sensitive information from unsuspecting users. **Always be responsible** when using or sharing security-related tools. Ethical use, consent, and awareness of laws are paramount.

