# Ghunt-Maltego
### Maltego Transform Partner to Ghunt 

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

Current Version: 1.0.0-beta 

Release Date: 2 June 2023

## 💎 About

Per their Github page, "[Ghunt (v2)](https://github.com/mxrch/GHunt) is an offensive Google framework, designed to evolve efficiently.
It's currently focused on OSINT, but any use related with Google is possible." Ghunt-Maltego utilizes the Ghunt python library to create Transforms in Maltego.

## 🎚️ Version
Ghunt-Maltego releases will be versioned using dotted triples, similar to [Semantic Version](http://semver.org/). For this specific document, we will refer to the respective components of this triple as <major>.<minor>.<patch>. The version number may have additional information, such as "-alpha.1", "-beta.2" to mark alpha and beta versions for earlier access. Such releases will be considered as "pre-releases".
   
| Version                          | Supported          |
|----------------------------------|--------------------| 
| Ghunt-Maltego 1.0.x              | :white_check_mark: |

## 🛠️ Setup

##  ⚙️ Features
The following is a list of supported Ghunt data types.
   
| Data Type       | Supported  |Entity             |
|-----------------|------------|-------------------| 
| Full Name       | ✅         | maltego.Person    |
| Profile Photos  | ✅         | maltego.Image     |
| Cover Photos    | ❌         |                   |
| User Type       | ❌         |                   |
| Gaia ID         | ❌         |                   |
| Enabled Apps    | ✅         |maltego.Service    |
| Review Company  | ✅         |maltego.Company    |
| Review Rating   | ✅         |maltego.Sentiment  |
| Review Type     | ✅         |maltego.Industry   |
| Review Tag      | ✅         |maltego.hashtag    |
| Review Location | ✅         |maltego.Location   |
| Review Photos   | ❌         |                   |
   
*If a Ghunt feature isn't listed here, then it's probably not currently supported by ghunt-maltego.*
   
### 💡 Demo

<img src="img/ghunt.gif">  

## 📜 License
![image](https://img.shields.io/badge/License-GNU%20GPL-blue)

[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.fr.html)
