<img src="img/ghunt-maltego.png">

### Maltego Transform Partner to Ghunt

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

Version: 1.2.0

## 💎 About

Per their Github page, "[Ghunt (v2)](https://github.com/mxrch/GHunt) is an offensive Google framework, designed to evolve efficiently. 
It's currently focused on OSINT, but any use related with Google is possible." Ghunt-Maltego utilizes the Ghunt python library to create Transforms in Maltego.

Ghunt is developed by [mxrch](https://github.com/mxrch). *Ghunt-Maltego is an independent third-party utilizing the Ghunt library and not officially associated with Ghunt.*

Please use this tool ethically by respecting people's privacy and only collecting intelligence where explicit permission has been granted or otherwise legally qualified to do so. We are not responsible for any illegal use.

## 🛠️ Setup

For more detailed instructions, read the [Wiki](https://github.com/kodamaChameleon/ghunt-maltego/wiki)

### Requirements
- Maltego 4.3.0
- [Python 3.11.2](./requirements.txt)
- A Gmail Account
- Ghunt Firefox/Google Companion (Optional)
   
### Installation

```
   cd ~/.local/bin
   git clone https://github.com/kodamaChameleon/ghunt-maltego.git
   cd ghunt-maltego
   python3 setup.py
```
   
## 🧙 Features

*If a Ghunt feature isn't listed here, then it's probably not currently supported by ghunt-maltego. If you would like to see it added, create a feature-enhancement request in GitHub explaining the feature desired and why it would be beneficial to the overall application.*

### Ghunt Email

<img src="img/demo.PNG">  
   
| Data Type                     | Supported  |Entity                |
|-------------------------------|------------|----------------------| 
| Full Name                     | ✅         | maltego.Person       |
| Profile Photos                | ✅         | maltego.Image        |
| Cover Photos                  | ✅         |                      |
| User Type                     | ❌         |                      |
| Gaia ID                       | ❌         |                      |
| Enabled Apps                  | ✅         | maltego.Service      |
| Review Company                | ✅         | maltego.Company      |
| Review Rating                 | ✅         | maltego.Sentiment    |
| Review Type                   | ✅         | maltego.Industry     |
| Review Tag                    | ✅         | maltego.hashtag      |
| Review Location               | ✅         | maltego.Location     |
| Review Photos                 | ❌         |                      |

### Ghunt Drive

<img src="img/demo2.PNG">

| Data Type                     | Supported  |Entity                |
|-------------------------------|------------|----------------------|
| Creation Date     | ✅         | maltego.DateTime     |
| Modification Date | ✅         | maltego.DateTime     |
| Owner             | ✅         | maltego.Person       |
| Organization      | ✅         | maltego.Organization |
| Domain            | ✅         | maltego.Domain       |
| Title             | ✅         | maltego.Phrase       |
| Hash              | ✅         | maltego.Hash         |
| Comments          | ✅         | maltego.Phrase       |

## 📜 License
![image](https://img.shields.io/badge/License-GNU%20GPL-blue)

[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.fr.html)
