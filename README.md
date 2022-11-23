<br />
<div align="center">
    <img src="https://avatars.githubusercontent.com/u/9819237?v=4" alt="Logo" width="100" height="80">
  </a>

<h3 align="center">Address Creation service</h3>

  <p align="center">
    A simple REST service that allows the creation of blockchain addresses in a simple flask application
    <br />
    <a href="https://purpleblob.net/en/home/#contacto">Contact Us</a>
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>

  </ol>
</details>


### Built With

* [Python](https://www.python.org/)


<p align="right">(<a href="#top">back to top</a>)</p>

---

# Usage

Set your provider address and Mnemonic language in configuration file and rename it to **config.ini**
## Sample request
```shell
curl -X POST -H "Content-Type: application/json" -d '{"password":"somecoolpassword"}' http://<YourHost>:5000/createAddress
```
## Sample launcher script
```shell
#!/bin/sh
export FLASK_APP=./src/app.py
flask --debug run -h 0.0.0.0
```





