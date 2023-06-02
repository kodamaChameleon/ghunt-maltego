# Ghunt-Maltego
### Maltego Transform Partner to Ghunt 

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

Current Version: 1.0.0 

Release Date: 12 May 2023

## Table of Contents
 - [About](#about)
 - [Trivia](#trivia)
 - [Version](#version)
 - [Setup](#setup)
 - [Transforms](#transforms)
   - [NumVerify](#numverify)
 - [License](#license)

## About
Iridophore is a curated list of Maltego transforms for conducting OSINT investigations. 
This tool is free, open-source, and is not intended for commercial use.
While some features may require API keys, this project will only support those who offer free-tier services.

## Trivia
Iridophores are the cells in the top layer of a chameleon's skin which give it the ability to change color. 
They do so by *transforming* their shape to reflect different colors of light.

## Version
Iridophore releases will be versioned using dotted triples, similar to [Semantic Version](http://semver.org/). For this specific document, we will refer to the respective components of this triple as <major>.<minor>.<patch>. The version number may have additional information, such as "-alpha.1", "-beta.2" to mark alpha and beta versions for earlier access. Such releases will be considered as "pre-releases".
   
| Version                          | Supported          |
|----------------------------------|--------------------| 
| Iridophore-Maltego 1.0.x         | :white_check_mark: |

## Setup
To get started, use the following commands from a terminal:

```
git clone https://github.com/kodamaChameleon/iridophore-maltego.git
cd irodophore-maltego
/usr/bin/python3 setup.py
```
For further information, consult the 🛠️[wiki pages](https://github.com/kodamaChameleon/iridophore-maltego/wiki/Installation).

## Transforms
This list will be updated as new transforms become available.

### NumVerify
NumVerify utilizes the [Numbers Verification API](https://numverify.com/) to return location, carrier, and line type data (API key required). 
Iridophore is not responsible for the validity of the data coming from the numbers verification API. 

<img src="img/numVerify.gif">  

## License
![image](https://img.shields.io/badge/License-GNU%20GPL-blue)

[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.fr.html)
