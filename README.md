
<a id="readme-top"></a>

<p align="center">
	<a href="https://github.com/silvertoken/rest-routeros/graphs/contributors">
    	<img src="https://img.shields.io/github/contributors/silvertoken/rest-routeros.svg?style=for-the-badge" alt="Contributors">
	</a>
	<a href="https://github.com/silvertoken/rest-routeros/network/members">
    	<img src="https://img.shields.io/github/forks/silvertoken/rest-routeros.svg?style=for-the-badge" alt="Forks">
	</a>
	<a href="https://github.com/silvertoken/rest-routeros/stargazers">
    	<img src="https://img.shields.io/github/stars/silvertoken/rest-routeros.svg?style=for-the-badge" alt="Stars">
	</a>
	<a href="https://github.com/silvertoken/rest-routeros/pulse">
    	<img src="https://shields.io/github/commit-activity/m/silvertoken/rest-routeros.svg?style=for-the-badge" alt="Commits">
	</a>
	<a href="https://github.com/silvertoken/rest-routeros/issues">
    	<img src="https://img.shields.io/github/issues/silvertoken/rest-routeros.svg?style=for-the-badge" alt="Issues">
	</a>
</p>

<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">REST RouterOS</h3>

  <p align="center">
    A python module for the RouterOS REST API
    <br />
    <a href="https://github.com/silvertoken/rest-routeros/issues/new?labels=bug">Report Bug</a>
    &middot;
    <a href="https://github.com/silvertoken/rest-routeros/issues/new?labels=enhancement">Request Feature</a>
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

There are many modules I found for the Mikrotik RouterOS.  I didn't find any for the REST API and I have
my router configured to support short lived certs with Hashicorp vault.  Current implementations only
allow for it to manage one certificate service.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [![Python][python-badge]][python-url]
* [![HTTPX][httpx-badge]][httpx-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

Python and HTTPX is required
* HTTPX
  ```sh
  pip install httpx
  ```

### Installation

Install the module using pip

* RestRouterOS
  ```sh
  pip install Rest-RouterOS
  ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

```python
import json
from RestRouterOS.api import RestRouterOS

router = RestRouterOS("hostname", "username", "password")
response = router.identity()
print(json.dumps(response, indent=4))
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Build Complete Roadmap
- [ ] Get Calls For DNS
- [ ] Get Calls For DHCP
- [ ] Build Documentation

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

If you would like to help with development, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Top contributors:

<a href="https://github.com/silvertoken/rest-routeros/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=silvertoken/rest-routeros" alt="contrib.rocks image" />
</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Silvertoken - [https://github.com/silvertoken](https://github.com/silvertoken)

Project Link: [https://github.com/silvertoken/rest-routeros](https://github.com/silvertoken/rest-routeros)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[python-badge]: https://img.shields.io/badge/python-000000?style=for-the-badge&logo=python&logoColor=white
[python-url]: https://www.python.org/
[httpx-badge]: https://img.shields.io/badge/HTTPX-000000?style=for-the-badge
[httpx-url]: https://www.python-httpx.org/