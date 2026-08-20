# Claire AI

Claire, your assistent with Artificial intelligence in your terminal. (CLI Agent).

It works like a integration of `langchain` agent in your terminal. 

From dev to devs :)

## Commands

### 1. `configure`

Command to make authentication, just put your api key (any provider), provider model and the name of the model.

- **Options**:
    - **--api-key** (str): API Key for integrate the LLM model with Claire.
    - **--provider-model** (str): Provider from the LLM model.
    - **--llm-model** (str): Name of the model used.

> You can see this and more of this command usage just using the `--help` option.

### 2. `chat`

Command to start conversation with Claire, just ask your query and Claire will post your response.

- **Options**:
    - **--query** (str): Query used to ask Claire.

> Obs.: Depeding on the provider that you configure, maybe, some dependencies are going to be requested. All from `langchain` chat models.

> You can see this and more of this command usage just using the `--help` option.

### 3. `install-dependency`

Command to install a dependency

- **Options**:
    - **--dependency-name** (str): Name of the dependency that you want to install.

> Obs.: If not passing dependency_name, this command will see the provider model that you passed in configuration and will pull the dependency that's needed to Claire works, if it's not installed.

> You can see this and more of this command usage just using the `--help` option.

### 4. `uninstall-dependency`

Command to uninstall a dependency

- **Arguments**:
    - **dependency_name** (str): Name of the dependency that you want to uninstall.

> You can see this and more of this command usage just using the `--help` option.