import streamlit as st
import openai

# Replace with your actual API key or store in st.secrets
openai.api_key = "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"  # Add your OpenAI key here

# Page config
st.set_page_config(page_title="Impostor Slayer AI", page_icon="🛡️", layout="centered")

st.title("🛡️ Impostor Slayer AI")
st.subheader("Slay self-doubt. Build quiet confidence.")

tab1, tab2, tab3 = st.tabs(["💭 Reframe a Thought", "🌟 Daily Boost", "📈 Weekly Recap"])

def call_openai(prompt, role="You are a supportive, confidence-boosting coach who helps reframe negative self-talk."):
    messages = [
        {"role": "system", "content": role},
        {"role": "user", "content": prompt}
    ]
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    return response.choices[0].message.content.strip()

with tab1:
    st.write("Feeling doubtful? Type your inner critic thought, and I'll help you reframe it.")
    user_input = st.text_area("💬 What's the thought?", height=100)
    if st.button("🔄 Reframe It"):
        if user_input:
            with st.spinner("Reframing your thought..."):
                reframe_prompt = f"Someone just said: '{user_input}'. Help them reframe it with kindness and encouragement."
                response = call_openai(reframe_prompt)
                st.success("Here's a better way to look at it:")
                st.markdown(f"> {response}")
        else:
            st.warning("Please enter a thought to reframe.")

with tab2:
    st.write("Need a boost? Get a quick reminder of your strength and value.")
    if st.button("⚡ Give Me a Boost"):
        with st.spinner("Summoning good vibes..."):
            boost_prompt = "Give a 1-2 sentence, original confidence-boosting affirmation for a remote professional who might be feeling self-doubt today."
            response = call_openai(boost_prompt)
            st.success("Here's your boost:")
            st.markdown(f"**{response}**")

with tab3:
    st.write("Look back on your week. What did you do that you're proud of?")
    weekly_wins = st.text_area("🏆 List your wins or proud moments:", height=150, placeholder="Closed a project, helped a teammate, stayed consistent...")
    if st.button("📋 Generate Recap"):
        if weekly_wins:
            with st.spinner("Writing your confidence recap..."):
                recap_prompt = f"Based on this list of accomplishments: {weekly_wins}, write a short and motivating summary that reflects their growth, effort, and strengths this week."
                response = call_openai(recap_prompt)
                st.success("Your Confidence Recap:")
                st.markdown(f"✅ {response}")
        else:
            st.warning("Add some wins or reflections first.")