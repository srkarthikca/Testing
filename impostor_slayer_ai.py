import streamlit as st
from openai import OpenAI

# --- OpenAI Setup ---
client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# --- Page Config ---
st.set_page_config(page_title="Impostor Slayer AI", page_icon="🛡️", layout="centered")

# --- Title ---
st.title("🛡️ Impostor Slayer AI")
st.subheader("Slay self-doubt. Build quiet confidence.")

# --- Tabs ---
tab1, tab2, tab3 = st.tabs(["💭 Reframe a Thought", "🌟 Daily Boost", "📈 Weekly Recap"])

# --- Chat Function ---
def call_openai(prompt, role="You are a supportive, confidence-boosting coach who helps reframe negative self-talk."):
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": role},
            {"role": "user", "content": prompt}
        ]
    )
    return chat_completion.choices[0].message.content.strip()

# --- Reframe Tab ---
with tab1:
    st.write("Feeling doubtful? Type your inner critic thought, and I'll help you reframe it.")
    user_input = st.text_area("💬 What's the thought?", height=100)
    if st.button("🔄 Reframe It", key="reframe"):
        if user_input:
            with st.spinner("Reframing your thought..."):
                reframe_prompt = f"Someone just said: '{user_input}'. Help them reframe it with kindness and encouragement."
                response = call_openai(reframe_prompt)
                st.success("Here's a better way to look at it:")
                st.markdown(f"> {response}")
        else:
            st.warning("Please enter a thought to reframe.")

# --- Daily Boost Tab ---
with tab2:
    st.write("Need a boost? Get a quick reminder of your strength and value.")
    if st.button("⚡ Give Me a Boost", key="boost"):
        with st.spinner("Summoning good vibes..."):
            boost_prompt = "Give a short, original confidence-boosting affirmation for a remote professional feeling self-doubt today."
            response = call_openai(boost_prompt)
            st.success("Here's your boost:")
            st.markdown(f"**{response}**")

# --- Weekly Recap Tab ---
with tab3:
    st.write("Look back on your week. What did you do that you're proud of?")
    weekly_wins = st.text_area("🏆 List your wins or proud moments:", height=150, placeholder="Closed a project, helped a teammate, stayed consistent...")
    if st.button("📋 Generate Recap", key="recap"):
        if weekly_wins:
            with st.spinner("Writing your confidence recap..."):
                recap_prompt = f"Based on this list of accomplishments: {weekly_wins}, write a short and motivating summary that reflects their growth, effort, and strengths this week."
                response = call_openai(recap_prompt)
                st.success("Your Confidence Recap:")
                st.markdown(f"✅ {response}")
        else:
            st.warning("Add some wins or reflections first.")

# --- Sidebar Disclaimer ---
with st.sidebar:
    st.markdown("---")
    st.markdown("#### ⚠️ Disclaimer")
    st.markdown(
        "*Impostor Slayer AI is an AI-powered tool for encouragement and mindset support.*\n\n"
        "*It is **not** a substitute for professional mental health care or coaching.*\n\n"
        "*If you're struggling with serious mental health concerns, please seek support from a qualified professional.*"
    )
    st.markdown("---")
    st.caption("🔋 Powered by OpenAI's GPT model. Outputs are AI-generated and for informational use only.")
