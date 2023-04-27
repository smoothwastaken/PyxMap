<p align="center">

<br>

<a href="" rel="noopener">

<img width=100% height=100% src="https://upload.wikimedia.org/wikipedia/commons/4/45/BB-ASCII-art-screenshot-zebra.png" alt="PyxMap illustration"></a>

</p>

  

<h3 align="center">PyxMap</h3>

  

<div align="center">

  

[![Status](https://img.shields.io/badge/status-development-important.svg)]()

[![GitHub Issues](https://img.shields.io/github/issues/smoothwastaken/PyxMap)](https://github.com/smoothwastaken/PyxMap/issues)

[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/smoothwastaken/PyxMap)](https://github.com/smoothwastaken/PyxMap/pulls)

[![License](https://img.shields.io/badge/license-GPLv3-blue.svg)](/LICENSE)

  

</div>

  

---

  

<p align="center"> A custom ASCII art application using camera input.

<br>

</p>

  

## 📝 Table of Contents

  

- [About](#about)

- [Getting Started](#getting_started)

- [Installation and Usage Protocol](#usage)

- [Authors](#authors)

  

## 🧐 About <a name = "about"></a>

  

PyxMap is a project that captures images from a camera, converts them into ASCII art, and stores them in a database. It also includes QR code reading functionality to identify users.

  

## 🏁 Getting Started <a name = "getting_started"></a>

  

Install all the required packages and launch the Python `main.py` file!

  

## 🎈 Installation and Usage Protocol <a name="usage"></a>

### Prerequisites

1. Make sure you have Python 3.6 or later installed on your system. You can download the latest version of Python from the [official website](https://www.python.org/downloads/).

2. Install the required packages:

   You can install the necessary packages using the `requirements.txt` file. Open a terminal or command prompt, navigate to the project directory, and run the following command:

   ```bash
   pip3 install -r requirements.txt
   ```

   This will install all the required packages and their versions needed to run the application.

3. Install the Pyzbar library:

   The Pyzbar library installation is different depending on the computer you are using. You can also learn more from [Pyzbar’s official documentation](https://pypi.org/project/pyzbar/) page.

   - **Mac OS version:**

     ```bash
     brew install zbar
     ```

   - **Windows OS version:**

     ```bash
     python -m pip install pyzbar
     ```

### Usage Protocol

1. Set up your environment variables and API keys (if necessary) for any external services used in the project, such as Google Cloud services.

2. Ensure that the `config.json` file contains the appropriate configuration settings for the application.

3. Run the `main.py` script:

   Open a terminal (Linux) or command prompt (Windows) and navigate to the project directory. Then, run the following command:

   ```bash
   python main.py
   ```

   This will start the main application loop, which captures QR codes, processes the images, saves the ASCII images, and adds them to the database.

4. To stop the application, press `Ctrl+C` in the terminal or command prompt.

Please note that some features, such as text-to-speech, may be available only on specific platforms (e.g., macOS). The application will automatically detect the platform and enable or disable these features accordingly.

  

## ✍️ Authors <a name = "authors"></a>

  

- Cléry Arque-Ferradou

- Nathanaël Lejuste

- De Beaumont du Repaire Carla

- Chasseigne Ulysse