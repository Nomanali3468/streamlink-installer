#!/bin/bash

# Termux Streamlink Easy Installer
# This script automatically installs Streamlink in Termux without requiring manual chmod

# Print colored text
print_color() {
    case $1 in
        "green") printf "\033[0;32m%s\033[0m\n" "$2" ;;
        "blue") printf "\033[0;34m%s\033[0m\n" "$2" ;;
        "red") printf "\033[0;31m%s\033[0m\n" "$2" ;;
        "yellow") printf "\033[0;33m%s\033[0m\n" "$2" ;;
    esac
}

# Show banner
show_banner() {
    clear
    print_color "blue" "╔══════════════════════════════════════════╗"
    print_color "blue" "║                                          ║"
    print_color "blue" "║      STREAMLINK INSTALLER FOR TERMUX     ║"
    print_color "blue" "║                                          ║"
    print_color "blue" "╚══════════════════════════════════════════╝"
    echo ""
}

# Check if Termux
check_termux() {
    if [ ! -d /data/data/com.termux ]; then
        print_color "red" "Error: This script is designed to run in Termux!"
        exit 1
    fi
}

# Update packages
update_packages() {
    print_color "yellow" "Step 1/4: Updating package lists..."
    pkg update -y && pkg upgrade -y
    if [ $? -ne 0 ]; then
        print_color "red" "Error: Failed to update packages. Please check your internet connection."
        exit 1
    fi
    print_color "green" "✓ Packages updated successfully."
}

# Install dependencies
install_dependencies() {
    print_color "yellow" "Step 2/4: Installing essential dependencies..."
    pkg install -y python python-pip ffmpeg libxml2 libxslt clang make
    if [ $? -ne 0 ]; then
        print_color "red" "Error: Failed to install dependencies."
        exit 1
    fi
    print_color "green" "✓ Dependencies installed successfully."
}

# Set up Python environment
setup_python() {
    print_color "yellow" "Step 3/4: Setting up Python environment..."
    pip install --upgrade pip
    pip install setuptools wheel cython
    if [ $? -ne 0 ]; then
        print_color "red" "Error: Failed to set up Python environment."
        exit 1
    fi
    print_color "green" "✓ Python environment set up successfully."
}

# Install Streamlink
install_streamlink() {
    print_color "yellow" "Step 4/4: Installing Streamlink..."
    pip install streamlink
    if [ $? -ne 0 ]; then
        print_color "red" "Error: Failed to install Streamlink."
        exit 1
    fi
    print_color "green" "✓ Streamlink installed successfully."
}

# Success message
show_success() {
    print_color "green" "╔══════════════════════════════════════════╗"
    print_color "green" "║                                          ║"
    print_color "green" "║    STREAMLINK INSTALLATION COMPLETED     ║"
    print_color "green" "║                                          ║"
    print_color "green" "╚══════════════════════════════════════════╝"
    echo ""
    print_color "yellow" "To use Streamlink, type: streamlink [URL] [QUALITY]"
    echo ""
    print_color "blue" "Version info:"
    streamlink --version
}

# Main function
main() {
    show_banner
    check_termux
    update_packages
    install_dependencies
    setup_python
    install_streamlink
    show_success
}

# Run main function
main
