from groq import Groq
from django.conf import settings

client = Groq(api_key=settings.GROQ_API_KEY)

def generate_daily_schedule(user_data):
    prompt = f"""Generate a daily schedule for a user based on the following information:
    - Wake time: {user_data['wake_time']}
    - Sleep time: {user_data['sleep_time']}
    - Goals: {user_data['goals']}
    
    The schedule should include:
    - Morning routine
    - Work hours
    - Breaks
    - Evening activities
    Please provide the schedule in a structured format with time slots and activity descriptions."""
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",  
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates daily schedules based on user data."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000,
    )
    return response.choices[0].message.content.strip()