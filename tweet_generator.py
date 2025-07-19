# tweet_generator.py
import random

class SimpleTweetGenerator:
    def __init__(self):
        # Simple templates - you can add more!
        self.positive_templates = [
            "{company} is making waves in {industry}! 🚀",
            "Big news from {company} today in {industry}!"
        ]
        self.negative_templates = [
            "Rough patch for {company} in {industry} sector. 😟",
            "{company} is facing criticism in the {industry} space."
        ]
        self.neutral_templates = [
            "{company} shares updates on {industry}.",
            "Steady progress from {company} in {industry}."
        ]
        self.templates = {
            'announcement': [
                "🚀 Exciting news from {company}! {message}",
                "Big announcement: {company} is {message} 🎉",
                "Hey everyone! {company} has {message} ✨"
            ],
            'question': [
                "What do you think about {topic}? Let us know! 💬",
                "Quick question: How do you feel about {topic}? 🤔",
                "{company} wants to know: What's your take on {topic}? 🗣️"
            ],
            'general': [
                "Check out what {company} is up to! {message} 🌟",
                "{company} update: {message} 💯",
                "From the {company} team: {message} 🔥"
            ]
        }
    
    def generate_smart_tweet(self, company, industry, word_count_target, sentiment_target, has_media):
        # 1. Choosing template based on sentiment
        if sentiment_target > 0.5:
            templates = self.positive_templates
        elif sentiment_target < -0.5:
            templates = self.negative_templates
        else:
            templates = self.neutral_templates

        # 2. Picking a base template and filling it
        base_tweet = random.choice(templates).format(company=company, industry=industry)
        words = base_tweet.split()

     
        # 3. Add media mention
        if has_media:
            tweet = " ".join(words)
            tweet += " 📸"
        else:
            return base_tweet

        return tweet[:280]  # Ensure it doesn't exceed Twitter limit
    def generate_tweet(self, company, tweet_type="general", message="Something awesome!", topic="innovation"):
       # Pick a random template
            template_list = self.templates.get(tweet_type, self.templates['general'])
            template = random.choice(template_list)
            
            # Fill in the template
            tweet = template.format(
                company=company,
                message=message,
                topic=topic
            )
            
            # Make sure it's not too long (Twitter limit is 280 characters)
            if len(tweet) > 280:
                tweet = tweet[:277] + "..."
            
            return tweet
     
# Test it out!
generator = SimpleTweetGenerator()
test_tweet = generator.generate_tweet("Nike", "announcement", "launching new running shoes")
smart_test_tweet=generator.generate_smart_tweet("Nike", "sportswear",300,-0.7,False)
print(test_tweet)
print(smart_test_tweet)