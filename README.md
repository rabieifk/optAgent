# optAgent

Verilog Code Optimizer

# Overview
 This Python-based agent is designed to optimize Verilog code to enhance operational frequency, ensuring improved performance while maintaining the existing functionality. It uses the OpenAI GPT model to generate multiple optimized versions of the input Verilog code.

# Installation
Install required packages:
pip install openai

# Usage

To use this script, you need a Verilog file you wish to optimize. The script takes a single command line argument, which is the path to the Verilog file.

# Run the script as follows:
`python3 agent.py <path_to_verilog_file>`

The script will generate up to 6 optimized versions of the input Verilog file, each aimed at increasing the operational frequency of the design.

# Requirements

- Python 3.6 or later.
- OpenAI API key: This script requires an API key from OpenAI to interact with the GPT model. Set your API key in your environment variables:
export OPENAI_API_KEY='your_api_key_here'

# Output

The optimized Verilog files will be saved in the same directory as the input file, named in the format `optimized_{variant}_{original_filename}`. Each file represents a different optimized version of the input code.

# Notes

- Ensure that your OpenAI API key has appropriate permissions and limits to execute multiple requests.
- The script introduces a delay between API calls to prevent rapid request submission, which might be regulated by OpenAI's usage policies.

# License

