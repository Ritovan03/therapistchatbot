from dotenv import load_dotenv
from mira_sdk import MiraClient, Flow
from mira_sdk.exceptions import FlowError
import os
import glob

# Load environment variables
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

            # Get flow name from the flow object
            flow_id = f"ritovan/{flow.name}"
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

    # Test therapist flow
    print("\nTesting therapist flow...")
    result = test_flow("ritovan/therapist", {
        "user_profile": "User is a 25-year-old experiencing mild anxiety and work stress.",
        "goals": "Reduce anxiety, improve focus, and establish better work-life balance.",
        "preferences": "Preference for CBT methods and digital solutions; budget-friendly options."
    })
    if result:
        print("\nTherapist Flow Result:")
        print(result)

if __name__ == "__main__":
    main()
