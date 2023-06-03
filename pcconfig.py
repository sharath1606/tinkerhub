import pynecone as pc

class TodoConfig(pc.Config):
    pass

config = TodoConfig(
    app_name="todo",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)