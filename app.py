from embedchain import App

epictetus_bot = App()

epictetus_bot.add("youtube_video",
                  "https://www.youtube.com/watch?v=7nC46z9UgsQ")
epictetus_bot.add("pdf_file", "enchiridion.pdf")

epictetus_bot.add_local(
  "qna_pair", ("Who was Epictetus?", "Epictetus was a Stoic Philosopher."))

print(epictetus_bot.query("What are some nuggets of wisdom?"))
