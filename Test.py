import json
import requests

# Function to transcribe audio into text
def transcribe_audio(audio_url):
    headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiM2U4NTljYTEtZTc1MS00ODRmLWEwZmQtOGE3ZDVlNTExNzc1IiwidHlwZSI6ImFwaV90b2tlbiJ9.RU07c_NRnXq34-cLz-8VWdHcvx-PLB8Is3tdO9-C7dM"}
    url = "https://api.edenai.run/v2/audio/speech_to_text_async"
    json_payload = {"providers": "assembly", "language": "en-US", "file_url": audio_url}
    
    response = requests.post(url, json=json_payload, headers=headers)
    result = json.loads(response.text)
    
    return result

# Function to summarize the transcribed text
def summarize_text(transcribed_text):
    headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiM2U4NTljYTEtZTc1MS00ODRmLWEwZmQtOGE3ZDVlNTExNzc1IiwidHlwZSI6ImFwaV90b2tlbiJ9.RU07c_NRnXq34-cLz-8VWdHcvx-PLB8Is3tdO9-C7dM"}
    url = "https://api.edenai.run/v2/text/summarize"
    payload = {"providers": "openai", "language": "en", "text": transcribed_text}
    
    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)
    
    return result['openai']['result']

# Function to prompt for scoring the call
def prompt_for_scoring(summary):
    # Your implementation for prompting and scoring the call goes here
    pass

# Main function to combine the AI models
def combine_ai_models(audio_url):
    # Transcribe audio into text
    transcribed_text = transcribe_audio(audio_url)
    
    # Summarize the transcribed text
    summary = summarize_text(transcribed_text)
    
    # Prompt for scoring the call
    prompt_for_scoring(summary)

# Example usage
audio_url = "https://avasntistorage3000.blob.core.windows.net/survey-upload/fid7yzwtcb4nycp02fp4i9hpkuyi?sp=r&sv=2018-11-09&se=2023-07-26T16%3A42%3A56Z&rscd=attachment%3B+filename%3D%22REe4f8077ea383de4c280afafa64484d4e.wav%22%3B+filename*%3DUTF-8%27%27REe4f8077ea383de4c280afafa64484d4e.wav&rsct=audio%2Fx-wav&sr=b&sig=aheqm0Ny4OsS2t4JBfh917fNPtq6RreMilv5f9CE2EA%3D"
combine_ai_models(audio_url)
