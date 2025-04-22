from crewai_tools import WeaviateVectorSearchTool
from crewai import agent, Agent  # Ensure you import the correct agent and Agent classes
# Initialize the tool
tool = WeaviateVectorSearchTool(
    collection_name='example_collections',
    limit=3,
    weaviate_cluster_url="https://your-weaviate-cluster-url.com",
    weaviate_api_key="your-weaviate-api-key",
)

@agent
def search_agent(self) -> Agent:
    '''
    This agent uses the WeaviateVectorSearchTool to search for 
    semantically similar documents in a Weaviate vector database.
    '''
    return Agent(
        config=self.agents_config["search_agent"],
        tools=[tool]
    )
