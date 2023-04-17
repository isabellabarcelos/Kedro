from kedro.pipeline import node
from kedro.pipeline import pipeline
from kedro.io import DataCatalog, MemoryDataSet
from kedro.runner import SequentialRunner

# Prepare first node
def return_greeting():
    return "Hello"

# Prepare second node
def join_statements(greeting):
    return f"{greeting} Kedro!"

return_greeting_node = node(func=return_greeting, inputs=None, outputs="my_salutation")

join_statements_node = node(
    join_statements, inputs="my_salutation", outputs="my_message"
)

# Assemble nodes into a pipeline
greeting_pipeline = pipeline([return_greeting_node, join_statements_node])

# Prepare a data catalog
data_catalog = DataCatalog({"my_salutation": MemoryDataSet()})

# Create a runner to run the pipeline
runner = SequentialRunner()

# Run the pipeline
print(runner.run(greeting_pipeline, data_catalog))