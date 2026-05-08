#!/bin/bash
# This script automates the setup we just did manually
sudo dnf update -y
sudo dnf install git python3 python3-pip nodejs -y
echo "System updated and dependencies installed."
