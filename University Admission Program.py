name = input("Enter your name: ")
print("Welcome, " + name + "!")

jamb_score = float(input("Enter your JAMB score: "))
post_utme_score = float(input("Enter your post-UTME score: "))

agg_score = (jamb_score / 8) + (post_utme_score / 2)

faculty = input("Enter the Faculty of your choice(use S for Science and A for Art): ").lower()


if faculty == 's' or faculty == 'science':
    if agg_score <= 49:
        print("You have failed to meet the admission requirements.")
    elif agg_score >= 50 and agg_score <= 60:
        print("You can apply for the following courses: Agric, Botany, Zoology, Biology")
    elif agg_score >= 61 and agg_score <= 70:
          print("You can apply for the following courses: Computer Science, Statistics, Psychology")
    elif agg_score >= 71 and agg_score <= 80:
        print("You can apply for the following courses: Veterinary, Mathematics, Biochemistry")
    else:
        print("Congratulations, you can apply for the following courses: Medicine and Nursing")

elif faculty == 'a' or faculty == 'art':
    if agg_score <= 49:
        print("You have failed to meet the admission requirements.")
    elif agg_score >= 50 and agg_score <= 60:
        print("You can apply for the following courses: Economics, History and International Studies, Music")
    elif agg_score >= 61 and agg_score <= 70:
          print("You can apply for the following cou5rses: Theatre Art, Political Science, Modern European Languages")
    elif agg_score >= 71 and agg_score <= 80:
        print("You can apply for the following courses: CLA, Linguistics, Religion and Human Relations")
    else:
        print("Congratulations, you can apply for the following courses: Law, Mass Communication, Criminology and Security Studies")
else:
    print("Faculty Loading..., Try Again Later")
    
