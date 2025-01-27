# Task-1 : Text Generation Using GPT-2

This project demonstrates how to generate text using the GPT-2 model from Hugging Face's Transformers library. It allows users to input a prompt and receive AI-generated text as output.

---

## Features
- Generate coherent and creative text based on a custom prompt.
- Adjust parameters like `max_length`, `temperature`, `top_k`, and `top_p` to control text output.
- Simple and easy-to-use script for text generation.

---

## Installation

### Prerequisites
- Python 3.8 or higher installed on your system.
- A code editor or terminal to run the script.

### Steps
1. Clone or download this repository to your local machine.
2. Install the required Python libraries:
   ```bash
   pip install transformers torch

Usage
1. Open the project folder in your terminal or code editor.    
2.Run the script:
   ```bash
   python text_generation.py

Enter a prompt when prompted (e.g., Once upon a time) and press Enter.
View the generated text in the terminal.

# Task 2: Image Generation Project

This project is focused on setting up an environment for image generation using PyTorch with CPU support.

## Prerequisites

Ensure the following tools are installed on your system:
- Python 3.10 or higher
- Pip (Python package installer)
- A virtual environment tool like `venv`

## Step-by-Step Setup Instructions

### 1. Clone or Create the Project Directory
Create or navigate to the directory where this project will reside:

      mkdir task2-image-generation
      cd task2-image-generation
And Create a file name with your_script.py
      
### 2. Create a Virtual Environment

Set up a virtual environment for the project:
     
      python -m venv env

   Activate the virtual environment:
   Windows:
           
      .\env\Scripts\activate
   Linux/Mac:

         source env/bin/activate
  ### 3. Upgrade Pip
Before installing dependencies, ensure pip is up to date:

      pip install --upgrade pip
### 4. Install PyTorch (CPU Only)
Install the CPU-compatible version of PyTorch, along with torchvision and torchaudio:

         pip install torch==2.0.1 torchvision==0.15.2 torchaudio==2.0.1
### 5. Verify the Installation
Check that PyTorch is installed correctly:

      python -c "import torch; print(torch.__version__); print(torch.cuda.is_available())"
Expected Output:
    The version of PyTorch (e.g., 2.0.1)
    False (indicating CUDA is not available as it's CPU-only)
### if version :

### 6. Additional Dependencies
Install any other dependencies required for your project:
      
      pip install -r requirements.txt
### 7. Run Your Project
After setting up the environment, execute your script or program:

      python your_script.py
Replace your_script.py with the name of your main Python script.

### 8. Deactivating the Virtual Environment
When done, deactivate the virtual environment:

       deactivate

Else : 
Troubleshooting :
Dependency Conflicts: If you encounter errors while installing dependencies, ensure you've uninstalled previous versions of torch, torchvision, and torchaudio:

      pip uninstall torch torchvision torchaudio
Then, retry the installation.
Environment Issues: Ensure you're running the commands inside the activated virtual environment.
Unsupported Version Error: If a specific version isn't found, ensure you're using the correct version of Python (3.10 or higher).
      






