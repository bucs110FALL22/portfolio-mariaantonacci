article = """
"Hackers breached internal systems at Fast Company magazine Tuesday evening, defacing the company’s main news site and sending racist push notifications through Apple News to iPhone users.
The two-sentence push notifications were attributed to Fast Company and contained the n-word and graphic language, prompting shocked users to post screenshots on Twitter.While breaches at media companies are not unheard of, the notification was one of the biggest violations of Apple’s “walled garden” in memory. There was nothing to indicate that user security was compromised beyond the upsetting wording. “Fast Company’s Apple News account was hacked on Tuesday evening. Two obscene and racist push notifications were sent about a minute apart,” the magazine said by email. “The messages are vile and are not in line with the content of Fast Company. We are investigating the situation and have suspended the feed and shut down FastCompany.com until we are certain the situation has been resolved.” An Apple spokesperson pointed to a tweet from Apple News that said: “An incredibly offensive alert was sent by Fast Company, which has been hacked. Apple News has disabled their channel.” While the magazine’s site was defaced, an article that was labeled sponsored content gave the hackers’ description of how the break-in occurred. That account said the group had gotten into the company’s WordPress program and found keys to functions including the Apple News programming interface."
"""

substitutions = {
  "Apple", "Samsung"
  "Hackers", "Ghosts"
  "Twitter", "TikTok"
  "Media", "Fake"
  "Notification", "Message"
  "News", "Message"
}

for key, value in substitutions.items():
   article = article.replace(key, value) 

print(article) 