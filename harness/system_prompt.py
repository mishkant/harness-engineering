import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

MODEL = "gpt-4o-mini"

client = OpenAI()

# სისტემური პრომპტი — Harness-ის პირველი პრიმიტივი.
# ყოველ წინადადებას თავისი საქმე აქვს: იდენტობა, შესაძლებლობა, შეზღუდვა ან ფორმატი.
SYSTEM_PROMPT = """
You are a coding assistant running in a developer's terminal, helping with software engineering tasks.
You have no tools yet: you cannot read files, run commands, or change anything on the user's machine. If a request needs a tool, say so in one sentence and ask the user to paste the relevant content.
Be concise: prefer short, direct answers. When asked for code, return the code with minimal explanation unless more is requested.
Use fenced code blocks with a language tag. Explain in Georgian; keep code, commands and technical terms in English.
"""

def run():
	"""
	გავუშვათ ჩვენი აგენტის ციკლი მანამ სანამ არ ვთხოვთ
	შეჩერდეს: exit ან quit
	"""

	# ისტორია სისტემური პრომპტით იწყება — ის ყოველ გამოძახებაზე მოდელთან იგზავნება
	messages = [{
		"role": "system",
		"content": SYSTEM_PROMPT
		}]

	print("აგენტი მზადყოფნაშია. თუ გსურთ მისი შეჩერება დაწერეთ 'exit' ან 'quit'\n")

	while True:

		# 1. მივიღოთ მომხმარებლისგან input
		user_input = input("user>> ").strip()

		# 2. გამოსვლის ალამის დაფიქსირება
		if user_input in {"exit", "quit"}:
			print("მშვიდობით!")
			break

		# 3. სიცარიელეზე შემოწმება
		if not user_input:
			continue

		# 4. მომხმარებლის მესიჯის ისტორიაში შეტანა
		messages.append({
			"role": "user",
			"content": user_input
			})

		# 5. სრული ინფორმაციის მოდელისკენ გადაგზავნა
		response = client.responses.create(
			model = MODEL,
			input = messages
			)

		# 6. ასისტენტის პასუხის ამოღება
		agent_message = response.output_text

		# 7. ასისტენტის/აგენტის პასუხის შეტანა ისტორიაში
		messages.append({
			"role": "assistant",
			"content": agent_message
			})

		# 8. პასუხის გამოტანა
		print(f"\nagent>> {agent_message}\n")


if __name__ == "__main__":
	run()