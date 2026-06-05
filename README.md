# Advanced Network Vulnerability Scanner

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![Security](https://img.shields.io/badge/Security-Pentesting-red)
![License](https://img.shields.io/badge/license-MIT-green)

A fast, multi-threaded network scanner built in Python. Unlike basic port scanners, this tool implements **Banner Grabbing** to actively identify the underlying services and their versions running on open ports, which is a critical first step in vulnerability assessment.

## Features

* **High-Speed Scanning:** Uses `concurrent.futures` for multi-threading, scanning hundreds of ports in seconds.
* **Banner Grabbing:** Attempts to extract service information (e.g., Apache/2.4.41, OpenSSH 8.2) to detect outdated software.
* **Professional UI:** Utilizes the `rich` library to generate clean, readable, and color-coded terminal tables.
* **Stealthy timeouts:** Optimized socket connections to avoid hanging on filtered ports.

## Quick Start

### Prerequisites
You need Python 3 installed and the `rich` library for the interface.
```bash
pip install rich
