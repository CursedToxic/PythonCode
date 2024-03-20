import random

responses = [
        'It is certain.', 'It is decidedly so.', 'Without a doubt.',
        'Yes - definitely.', 'You may rely on it.', 'As I see it, yes.',
        'Most likely.', 'Outlook good!', 'Yes.', 'Signs point to yes.',
        'Reply hazy, try again.', 'Ask again later...',
        'Better not tell you now.', 'Cannot predict now.',
        "Don't count on it.", 'My reply is no.', 'My sources say no.',
        'Outlook not so good.', 'Very doubtful.']

def ball():
  print("i am a magic 8 ball")
  input("ask question please:")
  print(f"🎱 {random.choice(responses)} 🎱")
  Repeat()
  
def Repeat():
  while True:
    try:
      reply = input("Do you have another question? [Y/N]: ")
      if reply.upper == "Y" or "YES":
        ball()
      elif reply.upper == "N" or "NO":
        exit()
        break
    except ValueError:
        print("PLEASE TRY AGAIN")
        Repeat()