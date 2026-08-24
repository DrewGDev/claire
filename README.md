# Claire AI

Claire, your assistent with Artificial intelligence in your terminal. (CLI Agent).

It works like a integration of `langchain` agent in your terminal. 

From dev to devs :)

## Installation

You can use Claire on-the-fly without permanently installing it, or install it globally on your system. We recommend using `uv` or `pipx` for isolated and safe installations.

### Try it without installing (On-the-fly)
If you have [uv](https://docs.astral.sh/uv/) installed, you can run Claire instantly, just like `npx`:

```
uvx claire-ai
```

### Global Installation (Recommended)

Using `uv`:
```
uv tool install claire-ai
```

Using `pipx`:
```
pipx install claire-ai
```

Using standard `pip`:
```
pip install claire-ai
```
> Make sure to use a virtual environment if you choose this method.

---

Once installed, Claire will be available globally in your terminal. You can start using it simply by typing:
```
claire-ai --help
```


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
    - **--copy** (bool): Permission to copy AI response automatically.

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