import os

def handler_exit_program():
    if os.path.exists('.tmp_graph.png'):
        os.remove('.tmp_graph.png')