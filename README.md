# Simple Mira Flow

This is a template project for creating Mira flows. Currently implements a text summarizer, but you can easily modify it for your needs.

## Quick Start

1. **Set up environment**
   ```bash
   # Create and activate a Python virtual environment (optional but recommended)
   python -m venv .venv
   source .venv/bin/activate

   # Install dependencies
   pip install -e .
   ```

2. **Add your API key**
   ```bash
   # Create .env file and add your Mira API key
   echo "MIRA_API_KEY=your_api_key_here" > .env
   ```

3. **Modify the flow**
   - Edit `flow.yaml`:
     - Change `metadata.name` to your flow name
     - Change `metadata.author` to your Mira username
     - Modify `inputs`, `model`, and `prompt` for your use case

4. **Update the code**
   - Edit `hello.py`:
     - Change `flow_id` in `deploy_flow()` to match your "author/flow-name"
     - Modify the sample input in `main()` to match your flow's requirements

5. **Run the flow**
   ```bash
   python hello.py
   ```

## Project Structure

- `flow.yaml`: Flow configuration (prompt, model, inputs)
- `hello.py`: Python code to deploy and run the flow
- `.env`: Environment variables (API key)
- `pyproject.toml`: Project dependencies