# Network Traffic Filtering

## 1. Environment & Architecture Overview
To mitigate unauthorized access and safeguard the Student Records Server, traffic filtering rules were implemented using `iptables` in the authorized laboratory environment.

### IP Address and Subnet Allocations
* **Student Records Server IP**: `192.168.10.5`
* **Authorised Staff Network Subnet**: `192.168.10.0/24` (Test Host IP: `192.168.10.20`)
* **Guest Network Subnet**: `192.168.30.0/24` (Test Host IP: `192.168.30.50`)
* **Unfamiliar External Network Subnet**: `192.168.40.0/24` (Test Host IP: `192.168.40.100`)
* **Authorised Service Port**: Port `22` (SSH / Student Records Access Service)

---

## 2. Firewall Rules Implementation

The following `iptables` commands were written and applied to enforce network isolation and explicit service permission control:

```bash
#!/bin/bash
# Clear existing rules and set policies
sudo iptables -F
sudo iptables -X
sudo iptables -P INPUT DROP
sudo iptables -P FORWARD DROP
sudo iptables -P OUTPUT ACCEPT

# Maintain active state connections and loopback
sudo iptables -A INPUT -i lo -j ACCEPT
sudo iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

# ------------------------------------------------------------------------------
# 3a. Block guest network access to the student records server
# ------------------------------------------------------------------------------
sudo iptables -A INPUT -s 192.168.30.0/24 -d 192.168.10.5 -j DROP

# ------------------------------------------------------------------------------
# 3b. Permit authorised staff network access to the service specified (Port 22)
# ------------------------------------------------------------------------------
sudo iptables -A INPUT -p tcp -s 192.168.10.0/24 -d 192.168.10.5 --dport 22 -j ACCEPT

# ------------------------------------------------------------------------------
# 3c. Block other inbound access to that service
# ------------------------------------------------------------------------------
sudo iptables -A INPUT -p tcp --dport 22 -j DROP
