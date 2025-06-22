# Temperature Converter CLI using Python

A simplePython CLI tool to convert temperatures between **Celsius** and **Fahrenheit**.

## Features

- Convert Celsius to Fahrenheit in CLI
- Convert Fahrenheit to Celsius in CLI

## Quick Start

### Prerequisites

Make sure Python 3.6+ is installed on your system:

```bash
python --version
```

### Installation

1. Download the `converter.py` script or clone the repo
 ```bash
git clone https://github.com/thanavreddy/cliconverterpy/
  ```
2. Navigate to the directory containing the script
3. Run the converter using the commands below

## Usage

### Convert Celsius to Fahrenheit

```bash
python converter.py --c2f <temperature_in_celsius>
```
### Convert Farenheit to Celsius

```bash
python converter.py --f2c <temperature_in_farenheit>
```



### Get Help

```bash
python converter.py --help
```



## ! Important

- You must specify **either** `--c2f` or `--f2c`, but not both
- The tool accepts decimal numbers (e.g., `25.5`, `-10.3`)
- If invalid arguments are provided, a helpful usage message will be displayed



---

*Built with Python 3 and the argparse library*
