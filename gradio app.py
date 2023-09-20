import gradio as gr


gr.Interface(fn=to_predict,
             inputs=gr.Image(),
             outputs=gr.Label(num_top_classes=3),
             examples=[])