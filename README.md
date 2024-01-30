# Setting up a virtual environment
It's recommended to create a virtual environment. Here, we'll be using Conda.

To create a new Conda environment, use the following command:

```bash
conda create --name llm
```

After creating the environment, activate it using:

```bash
conda activate llm
```

Once the Conda environment is activated, you can install the dependencies from the `requirements.txt` file. Use the following command:

```bash
pip install -r requirements.txt
```

# Usage
To run the code, use the following command:

```bash
streamlit run main.py
```
# Changelog
- 01-2024
  - Change the title to “Chat with your documents”
  - Update readme


- 12-2023
  - Add [[LlamaIndex]] and implement the 1st example
  - Add a sample file cv_tim.txt
  - Add questions related to local file
  - Add 1st version of [[Chroma]]
  - Add streamlit option to upload document
  - Create a [[GitHub]] project and push the 1st version (09-12-2023)