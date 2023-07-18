# Network Information Retrieval

This Python script retrieves network information from the local machine and displays it in a formatted table. 
It gathers data such as network adapter names, their state, physical addresses, and DHCP (Dynamic Host Configuration Protocol) enabled status. 
Additionally, it retrieves the computer's IP address, gateway, and hostname.

## Prerequisites

- Python 3.x
- `tabulate` library: Install it using `pip install tabulate`.
- `re` library: Install it using `pip install re`.
- `subprocess` library: Install it using `pip install subprocess`.

## Usage

1. Ensure that you have Python 3.x installed on your machine.
2. Install the `tabulate` library by executing `pip install tabulate` in your command-line interface.
3. Install the `re` library by executing `pip install re` in your command-line interface.
4. Install the `subprocess` library by executing `pip install subprocess` in your command-line interface.
5. Run the script by executing `python chernetsky.py`.
6. The script will display the network information in a formatted table.

## Output

The script will produce two sections of network information:

1. NIC (Network Interface Card) Information:
   - Adapter Name: Name of the network adapter.
   - State: Media state of the adapter.
   - Physical Address: MAC (Media Access Control) address of the adapter.
   - DHCP Enabled: DHCP status of the adapter.

2. IP (Internet Protocol) Information:
   - IPv4 Address: The IP address assigned to the computer.
   - Gateway: The IP address of the default gateway.
   - HostName: The hostname of the computer.

## Example Output

Computer Information: NIC

╭───────────────────────┬────────────┬─────────────────────┬───────────────╮

│     Name              │ State      │ Physical Address    │ DHCP Enabled  │

├───────────────────────┼────────────┼─────────────────────┼───────────────┤

│ Ethernet Adapter 1    │ Connected  │ 00-11-22-33-44-55   │ Yes           │

│ Ethernet Adapter 2    │ Unknown    │ 66-77-88-99-AA-BB   │ No            │

╰───────────────────────┴────────────┴─────────────────────┴───────────────╯

Computer Information: IP

╭───────────────┬─────────────╮ 

│ IPv4 Address  │ 192.168.1.1 │

│ GateWay       │ 192.168.1.2 │

│ HostName      │ MyComputer  │

╰───────────────┴─────────────╯
