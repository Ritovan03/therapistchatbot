from dotenv import load_dotenv
from mira_sdk import MiraClient, Flow
from mira_sdk.exceptions import FlowError
import os
import glob

load_dotenv()
client = MiraClient(config={"API_KEY": os.getenv("MIRA_API_KEY")})

def deploy_flows():
    # Get all YAML files in the flows directory
    flow_files = glob.glob("flows/*.yaml")

    for flow_file in flow_files:
        try:
            # Create flow from YAML file
            flow = Flow(source=flow_file)

            # Deploy to platform
            client.flow.deploy(flow)

            # Get flow name from filename
            flow_name = os.path.splitext(os.path.basename(flow_file))[0]
            flow_id = f"aahnik/{flow_name}"
            print(f"Flow deployed successfully with ID: {flow_id}")

        except FlowError as e:
            print(f"Error deploying flow {flow_file}: {str(e)}")
        except Exception as e:
            print(f"Unexpected error with {flow_file}: {str(e)}")

def test_flow(flow_id, inputs):
    try:
        # Execute the flow with inputs
        result = client.flow.execute(flow_id, inputs)
        return result
    except FlowError as e:
        print(f"Error running flow: {str(e)}")
        return None

def main():
    # Deploy the flow
    print("Deploying flow...")
    deploy_flows()

    # Test code reviewer
    code_sample = """
    def add(a, b):
        return a + b  # No type hints or error handling
    """
    print("\nTesting code-reviewer flow...")
    result = test_flow("aahnik/code-reviewer", {
        "code": code_sample,
        "language": "python"
    })
    if result:
        print("\nCode Review:")
        print(result)

if __name__ == "__main__":
    main()
