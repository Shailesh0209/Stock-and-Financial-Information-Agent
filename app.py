import streamlit as st
from langchain import hub
from langchain.agents import create_openai_functions_agent
from langchain_openai.chat_models import ChatOpenAI
from langchain_community.utilities.polygon import PolygonAPIWrapper
from langchain_community.tools import PolygonLastQuote, PolygonTickerNews, PolygonFinancials, PolygonAggregates
from langchain_core.runnables import RunnablePassthrough
from langchain_core.agents import AgentFinish
from langgraph.graph import END, Graph

# Step 1: Define tools
prompt = hub.pull("hwchase17/openai-functions-agent")
llm = ChatOpenAI(model="gpt-4-turbo-preview")

polygon = PolygonAPIWrapper()
tools = [
    PolygonLastQuote(api_wrapper=polygon),
    PolygonTickerNews(api_wrapper=polygon),
    PolygonFinancials(api_wrapper=polygon),
    PolygonAggregates(api_wrapper=polygon),
]

# Step 2: Define agent and helper functions
agent_runnable = create_openai_functions_agent(llm, tools, prompt)
agent = RunnablePassthrough.assign(
    agent_outcome=agent_runnable
)

# Define the function to execute tools
def execute_tools(data):
    agent_action = data.pop('agent_outcome')
    tool_to_use = {t.name: t for t in tools}[agent_action.tool]
    observation = tool_to_use.invoke(agent_action.tool_input)
    data['intermediate_steps'].append((agent_action, observation))
    return data

# Step 3: Define LangGraph
def should_continue(data):
    if isinstance(data['agent_outcome'], AgentFinish):
        return "exit"
    else:
        return "continue"

workflow = Graph()
workflow.add_node("agent", agent)
workflow.add_node("tools", execute_tools)
workflow.set_entry_point("agent")
workflow.add_conditional_edges(
    "agent",
    should_continue,
    {
        "continue": "tools",
        "exit": END
    }
)
workflow.add_edge('tools', 'agent')
chain = workflow.compile()

# Step 4: Streamlit UI
def main():
    st.title("Stock and Financial Information Agent")

    # Input box for user query
    query = st.text_input("Ask a financial query:")

    result = None  # Initialize the result variable

    if query:
        with st.spinner("Processing your query..."):
            result = chain.invoke({"input": query, "intermediate_steps": []})
            output = result['agent_outcome'].return_values["output"]

        # Display the result
        st.write("### Query Result:")
        st.write(output)

    # Optionally, display the intermediate steps or history
    if result and 'intermediate_steps' in result:
        st.write("### Intermediate Steps:")
        for step in result['intermediate_steps']:
            st.write(step)

if __name__ == "__main__":
    main()
