text = """
Most of my friends like to stay inside to play video games, read books or watch TV, but I have a good hobby of going outside and playing sports. I play many different sports in my free time; some of them are soccer, swimming, volleyball and basketball. Sometimes I also ride the bikes or do board skating with my cousin in the park. In my opinion, doing sport is one of the rare hobbies that actually have good impacts on me. I am taller than most of my classmates thanks to swimming and basketball lessons that I take during summer time. My muscles are even stronger than my older brother, and I can last longer than most other people in any sport competition. Sports bring me a lot of benefits, and they are also fun things to do at the same time. I love the feeling of the cool water run through my face when I am swimming, and it seems like I am flying whenever I take a dive underwater. When I play soccer, it is very exciting for me or my teammates to score a goal even though we do not take part in any tournament. Both of my physical and mental health become better after I play sports, so it can be considered as the best things to do in my free time. Sports are like a part of my life besides other activities, and I will continue to play sports till I am too weak for them.
"""
dictionary = {}
count = 0
text_list = text.split(" ")
def count_chars(text):
    for line in text_list:
        # Remove the leading spaces and newline character
        line = line.strip()

        # Convert the characters in line to
        # lowercase to avoid case mismatch
        line = line.lower()

        # Remove the punctuation marks from the line
        line = line.replace('.', ' ')
        line = line.replace(',', ' ')
        line = line.replace(';', ' ')

        # Split the line into words
        words = line.split(" ")

        for word in words:

            if word in dictionary:
                dictionary[word] += 1
            else:
                dictionary[word] = 1

    for key in list(dictionary.keys()):
        print(key,":",dictionary[key])
count_chars(text)