import os
import openai
import sys
import time

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def optimize_verilog_code(input_file, num_variants=6):
    try:
        with open(input_file, 'r') as f:
            verilog_code = f.read()

        for variant in range(1, num_variants + 1):
            prompt = f"""
            I have a Verilog design described in the following code:
            ```
            {verilog_code}
            ```
            I want to optimize this design to increase its operational frequency. The goal is to enhance the design's performance by making it capable of running at a higher frequency while preserving all existing functionality.

            Your task:
            - Generate an optimized version of the Verilog code that maintains the same functionality but is optimized for higher frequency.
            - Provide only the optimized Verilog code, and no explanation or comments.
            """

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",  # Use the correct model
                messages=[
                    {"role": "system", "content": "You are an expert in Verilog code optimization."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=2000
            )

            optimized_code = response.choices[0].message.content.strip()

            optimized_code_lines = [line for line in optimized_code.splitlines() if "```" not in line]
            optimized_code_cleaned = "\n".join(optimized_code_lines)

            output_file = f"optimized_{variant}_{os.path.basename(input_file)}"
            with open(output_file, 'w') as f:
                f.write(optimized_code_cleaned)

            print(f"Optimized version {variant} saved to {output_file}")

            time.sleep(2)

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 agent.py <verilog_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    # Optimize the Verilog code to generate multiple variants
    optimize_verilog_code(input_file, num_variants=6)
