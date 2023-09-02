import gradio as gr

block = gr.Blocks()

def run():
  with block:
    gr.Markdown(
    """
    🐣 Please follow me for new updates https://twitter.com/camenduru <br />
    🧬 Please follow me for new updates https://github.com/dhritzz <br />
    🔥 By the way i only remake it :3 dhritzz <br />
    """)
    block.launch(server_name="0.0.0.0", server_port=7860)

if __name__ == "__main__":
    run()