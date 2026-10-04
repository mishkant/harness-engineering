import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

MODEL = "gpt-4o-mini"

client = OpenAI()

def run():
	"""
	გავუშვათ ჩვენი აგენტის ციკლი მანამ სანამ არ ვთხოვთ
	შეჩერდეს: exit ან quit
	"""

	messages = []

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