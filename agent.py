from openai import OpenAI

client = OpenAI(api_key="api_key")
import os
import time
import argparse
import sys

def generate_optimized_verilog(original_code, num_variants=3, model="gpt-4"):
    """
    Generates multiple optimized versions of the input Verilog code using OpenAI's API.

    Parameters:
        original_code (str): The original Verilog code to optimize.
        num_variants (int): The number of optimized variants to generate.
        model (str): The OpenAI model to use (e.g., "gpt-4").

    Returns:
        List[str]: A list containing the optimized Verilog code variants.
    """
    optimized_codes = []
    for variant in range(1, num_variants + 1):
        prompt = f"""
You are an expert in Verilog code optimization.

Your task is to optimize the following Verilog code to achieve better performance, such as higher frequency, while ensuring that the optimized code is logically equivalent to the original.

Original Verilog Code:
```verilog
{original_code}
"""
        try:
            response = client.chat.completions.create(model=model,
            messages=[
                {"role": "system", "content": "You are an expert Verilog code optimizer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=1500,
            n=1,
            stop=["```"])
            optimized_code = response.choices[0].message.content.strip()
            optimized_codes.append(optimized_code)
            print(f"Variant {variant} optimized successfully.")
            time.sleep(1)
        except Exception as e:
            print(f"An error occurred while generating variant {variant}: {e}")
            break
    return optimized_codes

def main():
    parser = argparse.ArgumentParser(description="Optimize Verilog code using OpenAI's API.")
    parser.add_argument('input_file', type=str, help='Path to the input Verilog file.')
    parser.add_argument('-n', '--num_variants', type=int, default=3, help='Number of optimized versions to generate (default: 3).')
    parser.add_argument('-o', '--output_dir', type=str, default="optimized_verilog", help='Directory to save optimized Verilog codes (default: "optimized_verilog").')
    parser.add_argument('-m', '--model', type=str, default="gpt-4", help='OpenAI model to use (default: "gpt-4").')

    args = parser.parse_args()

    input_file = args.input_file
    output_dir = args.output_dir
    num_variants = args.num_variants
    model = args.model

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable not set.")
        print("Please set your OpenAI API key as an environment variable.")
        print("Example (Linux/macOS): export OPENAI_API_KEY='your-api-key-here'")
        print("Example (Windows): setx OPENAI_API_KEY \"your-api-key-here\"")
        sys.exit(1)


    if not os.path.exists(output_dir):
        try:
            os.makedirs(output_dir)
            print(f"Created directory: {output_dir}")
        except Exception as e:
            print(f"Failed to create directory '{output_dir}': {e}")
            sys.exit(1)

    try:
        with open(input_file, 'r') as f:
            original_code = f.read()
        print(f"Read original Verilog code from '{input_file}'.")
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found. Please ensure the file exists.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading '{input_file}': {e}")
        sys.exit(1)

    print(f"Generating {num_variants} optimized variant(s)...")
    optimized_codes = generate_optimized_verilog(original_code, num_variants, model)

    if not optimized_codes:
        print("No optimized codes were generated due to an error.")
        sys.exit(1)

    for idx, code in enumerate(optimized_codes, 1):
        output_file = os.path.join(output_dir, f"optimized_code_{idx}.v")
        try:
            with open(output_file, 'w') as f:
                f.write(code)
            print(f"Optimized Verilog code saved to '{output_file}'.")
        except Exception as e:
            print(f"Failed to write optimized code to '{output_file}': {e}")

if __name__ == "__main__":
    main()
