from fastapi import APIRouter, Request
from fastapi.responses import Response
import html

router = APIRouter()

order_state = {}

user_memory = {}


def handle_intent(user_message, chain):
    msg = user_message.lower()

    if "menu" in msg:
        return chain.invoke("Show full menu")

    elif "suggest" in msg or "recommend" in msg:
        return chain.invoke("Suggest best items")

    elif "order" in msg:
        order_state["started"] = True
        return "Great! 😊 What would you like to order?"

    elif order_state.get("started"):
        order_state["items"] = user_message
        return f"Got it 👍 You ordered: {user_message}\n\nAnything else?"

    return chain.invoke(user_message)


def create_webhook(chain):
    @router.post("/webhook")
    async def whatsapp_webhook(request: Request):
        try:
            form = await request.form()
            user_message = form.get("Body")
            user_id = form.get("From")  # unique user

            print("📩 User:", user_message)

            if not user_message:
                reply = "Hey! 👋 What would you like today?"
            else:
                # Create memory for user
                if user_id not in user_memory:
                    user_memory[user_id] = []

                history = user_memory[user_id]

                # Add last 5 messages
                history_text = "\n".join(history[-5:])

                # Send history + current message
                full_input = f"""
Conversation History:
{history_text}

User: {user_message}
"""

                response = chain.invoke(full_input)
                reply = response.content

                # Save memory
                history.append(f"User: {user_message}")
                history.append(f"Bot: {reply}")

                reply = html.escape(reply)

            print("🤖 Bot:", reply)

        except Exception as e:
            print("❌ ERROR:", e)
            reply = "Something went wrong."

        return Response(
            content=f"""
<Response>
    <Message>{reply}</Message>
</Response>
""",
            media_type="application/xml"
        )

    return router