# scapof

![image](https://github.com/user-attachments/assets/99f62ee9-e4a2-4f25-81b4-178928cde336)

**Scapof** is a network packet crafting and spoofing tool built using Scapy. It provides users with a simple CLI to create and manipulate ARP packets for network testing and spoofing purposes. The tool is designed to be versatile and user-friendly, allowing you to test network security and troubleshoot network issues effectively.

## Installation

To install Scapof and its dependencies, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/scapof.git
    cd scapof
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To use Scapof, you can run the `scapof.py` script with the appropriate command-line arguments. Below are some examples of how to use the tool:

### Build and Send an ARP Packet

```bash
python scapof.py -sm 00:11:22:33:44:55 -dm ff:ff:ff:ff:ff:ff -si 192.168.1.100 -di 192.168.1.1 --op 2
