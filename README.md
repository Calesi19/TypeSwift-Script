![TypeSwift Banner](/docs/banner.png)

# TypeSwift

TypeSwift is a lightweight and user-friendly text expander tool that aims to enhance your typing experience. It allows you to create and utilize custom keyboard shortcuts for frequently used phrases and expressions, significantly reducing your typing time and effort.

## Features

- **Custom Shortcuts**: Easily define your own shortcuts for long phrases or frequently typed text.
- **Intuitive Interface**: Planning a GUI for seamless addition, removal, and editing of shortcuts.
- **Real-time Expansion**: Text expansions occur as you type, ensuring a smooth workflow.
- **Cross-platform Compatibility**: Designed to work across various operating systems.

## Getting Started

To get started with TypeSwift, clone this repository and install the necessary dependencies.
```
pip install -r requirements.txt
```

## Usage
After installing TypeSwift, you can run the script to start using your custom shortcuts. The script will run in the background, listening for your defined shortcuts and expanding them in real-time as you type.

```
python src
```

## Create Virtual Environment
If you want to isolate the dependencies for this program away from the python dependencies installed on your machine, you can create a a virtual environmnent by running the following command:
```
python -m venv myenv
```
Then activate the environment by running the following command:
```
source myenv/bin/activate
```
Then install the dependencies.
```
pip install -r requirements.txt
```
Exit the environment anytime by running the command:
```
deactivate
```