# Simple Mira Flow

This is a template project for creating Mira flows. Currently implements a text summarizer, but you can easily modify it for your needs.

## Quick Start

**Before you start, please [sign up](https://flows.mira.network/) using invitation code `SRICITY` and get your Mira API key.**

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
   - Check your deployed flow at https://flows.mira.network/factory

## Project Structure

- `flow.yaml`: Flow configuration (prompt, model, inputs)
- `hello.py`: Python code to deploy and run the flow
- `.env`: Environment variables (API key)
- `pyproject.toml`: Project dependencies


## Ideas

- AI DJ that generates music based on your dance moves
- AI that generates recipe based on the ingredients you have at home
- AI that generates a song based on your favorite lyrics
- AI that predicts your mood based on your tone of voice
- AI that generates a workout routine based on your fitness goals
- AI that generates a poem based on your emotions
- AI that generates a video game based on your favorite games
- AI that generates a personalized meditation based on your brain waves
- AI that generates a fashion outfit based on your style
- AI that generates a personalized book based on your reading habits
