
# from streamlit_webrtc import webrtc_streamer, RTCConfiguration
# import av
# import cv2
# import streamlit as st
# import io
# from PIL import Image
# import google.generativeai as genai

# # Set the API key before creating an instance of GenerativeModel
# genai.configure(api_key="AIzaSyBZAan2Q2NR66k4mAJYqhao4bKNJi0OoQY")

# cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# class VideoProcessor:
#     def __init__(self):
#         self.genai_model = genai.GenerativeModel('gemini-pro-vision')

#     def recv(self, frame):
#         frm = frame.to_ndarray(format="bgr24")

#         faces = cascade.detectMultiScale(cv2.cvtColor(frm, cv2.COLOR_BGR2GRAY), 1.1, 3)

#         for x, y, w, h in faces:
#             cv2.rectangle(frm, (x, y), (x + w, y + h), (0, 255, 0), 3)

#         # Convert frame to PIL Image for processing with the gemini model
#         pil_image = Image.fromarray(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))
#         input_image = pil_image.resize((256, 256))  # Adjust the size as needed

#         # Get the input prompt from Streamlit text_input
#         input_prompt = st.text_input("Input Prompt:", "Describe the detected faces in the video.")

#         # Get response from Gemini model
#         response = self.get_gemini_response(input_prompt, input_image)

#         st.text(response)  # Display response in Streamlit app

#         return av.VideoFrame.from_ndarray(frm, format='bgr24')

#     def get_gemini_response(self, input_prompt, input_image):
#         # Convert PIL Image to bytes for model input
#         input_image_bytes = self.image_to_bytes(input_image)

#         # Prepare model input
#         image_parts = [
#             {
#                 "mime_type": "image/jpeg",
#                 "data": input_image_bytes
#             }
#         ]

#         # Generate response from Gemini model
#         response = self.genai_model.generate_content([input_prompt], image_parts=image_parts)
#         return response.text

#     def image_to_bytes(self, image):
#         img_byte_array = io.BytesIO()
#         image.save(img_byte_array, format='JPEG')
#         return img_byte_array.getvalue()


# st.set_page_config(page_title="AI Project with Video and Gemini")

# st.header("AI Project with Live Video and Gemini")
# webrtc_streamer(key="example", video_processor_factory=VideoProcessor,
#                  rtc_configuration=RTCConfiguration(
#                      {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
#                  ))




