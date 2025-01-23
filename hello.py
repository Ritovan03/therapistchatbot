from dotenv import load_dotenv
from mira_sdk import MiraClient, Flow
from mira_sdk.exceptions import FlowError
import os

load_dotenv()
client = MiraClient(config={"API_KEY": os.getenv("MIRA_API_KEY")})

def deploy_flow():
    try:
        # Create flow from YAML file
        flow = Flow(source="flow.yaml")
        
        # Deploy to platform
        client.flow.deploy(flow)
        
        # Get flow ID
        flow_id = "aahnik/text-summarizer"  # author/flow-name format
        print(f"Flow deployed successfully with ID: {flow_id}")
        return flow_id
    except FlowError as e:
        print(f"Error deploying flow: {str(e)}")
        return None
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return None

def test_summarization(flow_id, text):
    try:
        # Execute the flow with input
        result = client.flow.execute(flow_id, {"text": text})
        return result
    except FlowError as e:
        print(f"Error running flow: {str(e)}")
        return None

def main():
    # Deploy the flow
    flow_id = deploy_flow()
    if not flow_id:
        return

    # Test the flow with a sample text
    sample_text = """
    Artificial intelligence (AI) is transforming the way we live and work. 
    It's being used in healthcare to diagnose diseases, in finance to detect fraud, 
    and in transportation to develop self-driving cars. Despite its benefits, 
    AI also raises important ethical concerns about privacy, bias, and job displacement.
    """

    print("\nTesting flow with sample text...")
    result = test_summarization(flow_id, sample_text)
    
    if result:
        print("\nSummary:")
        print(result)

if __name__ == "__main__":
    main()
