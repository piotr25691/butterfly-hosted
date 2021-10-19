[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/piotr25691/butterfly-hosted">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">butterfly-hosted</h3>

  <p align="center">
    A project based on butterfly to host your own DDR server on the web.
    <br />
    <a href="https://github.com/piotr25691/butterfly-hosted"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/piotr25691/butterfly-hosted">View Demo</a>
    ·
    <a href="https://github.com/piotr25691/butterfly-hosted/issues">Report Bug</a>
    ·
    <a href="https://github.com/piotr25691/butterfly-hosted/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#about-butterfly">About Butterfly</a></li>
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
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

### About Butterfly

This is **butterfly**, an e-AMUSEMENT server emulator. This is a mostly-fully-featured server, intended for local usage.

### Features:

* Full support for profile creation, score saving, options saving, rivals, etc.
  * Carding in works as expected, and any number of profiles is supported
* User-controllable song lock/unlock via SQL scripts (currently event progress is not tracked / everything is fully unlocked already)
* Can run on Windows/Mac/Linux

### Built With

* [Java](https://www.java.com/en/)
* [Python](https://www.python.org/)

<!-- GETTING STARTED -->
## Getting Started

Clone the repo to get started, then run `main.py`. Optionally, install an SQL database browser like [this one](https://sqlitebrowser.org/).

### Prerequisites

[Python](https://www.python.org/) is necessary for this project to work.


### Installation

When you're ready to deploy this to a webserver, please upload the files onto a server that supports execution of Python scripts **AND DOES NOT FORCE HTTPS OR ELSE DDR WON'T BE ABLE TO CONNECT TO IT!**

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

This project does not have a license attached to it, please take other licenses for the included components in mind.

[contributors-shield]: https://img.shields.io/github/contributors/piotr25691/butterfly-hosted.svg?style=for-the-badge
[contributors-url]: https://github.com/piotr25691/butterfly-hosted/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/piotr25691/butterfly-hosted.svg?style=for-the-badge
[forks-url]: https://github.com/piotr25691/butterfly-hosted/network/members
[stars-shield]: https://img.shields.io/github/stars/piotr25691/butterfly-hosted.svg?style=for-the-badge
[stars-url]: https://github.com/piotr25691/butterfly-hosted/stargazers
[issues-shield]: https://img.shields.io/github/issues/piotr25691/butterfly-hosted.svg?style=for-the-badge
[issues-url]: https://github.com/piotr25691/butterfly-hosted/issues
[license-shield]: https://img.shields.io/github/license/piotr25691/butterfly-hosted.svg?style=for-the-badge
[license-url]: https://github.com/piotr25691/butterfly-hosted/blob/master/LICENSE.txt
[product-screenshot]: images/screenshot.png
